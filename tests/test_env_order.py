"""Where credentials are read from, and who wins.

The user's own ~/.needythreads/.env must beat any .env found in the working
folder, so a downloaded folder cannot route the user's drafts to another
Publora account.
"""
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

try:
    import dotenv  # noqa: F401
except ImportError:  # the loader is a no-op without python-dotenv
    dotenv = None

from lib import _env

NAMES = ("PUBLORA_API_KEY", "THREADS_PLATFORM_ID", "THREADS_SKILLS_CUSTOM_POSTER")


def write_env(folder: Path, text: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / ".env"
    path.write_text(text, encoding="utf-8")
    return path


@unittest.skipIf(dotenv is None, "python-dotenv is not installed")
class EnvOrderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.home_env = root / "home" / ".needythreads" / ".env"
        self.work = root / "work"
        self.work.mkdir()

        clean = {k: v for k, v in os.environ.items() if k not in NAMES}
        patcher = mock.patch.dict(os.environ, clean, clear=True)
        patcher.start()
        self.addCleanup(patcher.stop)
        patcher = mock.patch.object(_env, "user_env_path", return_value=self.home_env)
        patcher.start()
        self.addCleanup(patcher.stop)
        old = os.getcwd()
        os.chdir(self.work)
        self.addCleanup(os.chdir, old)

    def load(self):
        _env.load_env(force=True)

    def test_home_file_comes_first(self):
        self.assertEqual(_env.env_candidates()[0], self.home_env)

    def test_home_key_beats_project_key(self):
        write_env(self.home_env.parent, "PUBLORA_API_KEY=sk_home\nTHREADS_PLATFORM_ID=threads-1\n")
        write_env(self.work, "PUBLORA_API_KEY=sk_stranger\nTHREADS_PLATFORM_ID=threads-999\n")
        self.load()
        self.assertEqual(os.environ["PUBLORA_API_KEY"], "sk_home")
        self.assertEqual(os.environ["THREADS_PLATFORM_ID"], "threads-1")

    def test_ignored_project_credentials_are_reported(self):
        write_env(self.home_env.parent, "PUBLORA_API_KEY=sk_home\n")
        stray = write_env(self.work, "PUBLORA_API_KEY=sk_stranger\n")
        self.load()
        self.assertEqual(_env.ignored_credentials(), [("PUBLORA_API_KEY", str(stray))])
        self.assertEqual(_env.env_source("PUBLORA_API_KEY"), str(self.home_env))

    def test_project_file_still_fills_what_home_lacks(self):
        write_env(self.home_env.parent, "THREADS_PLATFORM_ID=threads-1\n")
        write_env(self.work, "PUBLORA_API_KEY=sk_project\n")
        self.load()
        self.assertEqual(os.environ["PUBLORA_API_KEY"], "sk_project")
        self.assertEqual(os.environ["THREADS_PLATFORM_ID"], "threads-1")

    def test_launch_environment_beats_every_file(self):
        write_env(self.home_env.parent, "PUBLORA_API_KEY=sk_home\n")
        with mock.patch.dict(os.environ, {"PUBLORA_API_KEY": "sk_launch"}):
            self.load()
            self.assertEqual(os.environ["PUBLORA_API_KEY"], "sk_launch")
            self.assertEqual(_env.env_source("PUBLORA_API_KEY"), "environment")

    def test_a_project_file_cannot_name_an_executable(self):
        write_env(self.work, "THREADS_SKILLS_CUSTOM_POSTER=calc.exe\nPUBLORA_API_KEY=sk_x\n")
        self.load()
        self.assertNotIn("THREADS_SKILLS_CUSTOM_POSTER", os.environ)


if __name__ == "__main__":
    unittest.main()
