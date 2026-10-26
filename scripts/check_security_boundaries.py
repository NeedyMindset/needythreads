#!/usr/bin/env python3
"""Three trust boundaries this bundle is not allowed to reopen.

These are enforced by this script so they stay closed.

1. **A project .env may not name an executable.** load_env() once copied every
   variable it found into the environment, and the DIY tier reads
   THREADS_SKILLS_CUSTOM_POSTER from there and runs it through subprocess. A .env
   that arrives with a clone, or lands in a parent directory, was therefore a
   command this bundle would execute. Only credentials load now.
2. **No module may load a .env behind load_env's back.** A direct load_dotenv()
   call reopens boundary 1 for whatever imports it.
3. **Authenticated requests may not follow redirects.** The Publora key rides a
   custom header and the Apify token rides a query parameter; requests strips
   Authorization across hosts but not either of those, so a redirect hands the
   credential, and on POST the body, to whoever answered.

4. **The user's own credentials file wins.** `~/.needythreads/.env` is read
   before any .env found in the working folder, so a folder that arrives with a
   .env of its own can never swap the key and send the user's drafts to someone
   else's Publora account.

Run from the repo root:

    python3 scripts/check_security_boundaries.py
"""
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENV = ROOT / "lib" / "_env.py"
POSTER = "THREADS_SKILLS_CUSTOM_POSTER"
CLIENTS = ("publora_client.py", "apify_client.py", "youtube_client.py", "pixfaro_client.py")
DOTENV_CALL = re.compile(r"load_dotenv\s*\(")
CALL = re.compile(r"((?:self\._session|requests)\.(?:get|post|put|delete)\()")


def call_bodies(source: str):
    """(offset, body) for every HTTP call, parens matched so multi-line is fine."""
    for match in CALL.finditer(source):
        depth, i = 1, match.end()
        while depth and i < len(source):
            if source[i] == "(":
                depth += 1
            elif source[i] == ")":
                depth -= 1
            i += 1
        yield match.start(), source[match.end():i - 1]


def main() -> int:
    problems = []

    env = ENV.read_text(encoding="utf-8")
    if "_DOTENV_VARIABLES" not in env:
        problems.append(
            "lib/_env.py has no _DOTENV_VARIABLES allowlist, so a project .env can set "
            "anything, including the command the DIY tier executes.")
    if DOTENV_CALL.search(env):
        problems.append(
            "lib/_env.py calls load_dotenv(), which loads every variable in the file. "
            "Read the allowlisted names with dotenv_values() instead.")
    if POSTER in env:
        problems.append(
            f"lib/_env.py names {POSTER}. The variable the bundle executes must come "
            f"from the launch environment, never from a file on disk.")

    for path in sorted((ROOT / "scripts").glob("*.py")) + sorted((ROOT / "lib").glob("*.py")):
        if path.name in ("_env.py", pathlib.Path(__file__).name):
            continue
        if DOTENV_CALL.search(path.read_text(encoding="utf-8")):
            problems.append(
                f"{path.relative_to(ROOT)} calls load_dotenv() directly, which bypasses the "
                f"allowlist in lib/_env.py. Import from lib instead.")

    for name in CLIENTS:
        path = ROOT / "lib" / name
        if not path.is_file():
            continue
        source = path.read_text(encoding="utf-8")
        for offset, body in call_bodies(source):
            if "allow_redirects" not in body:
                line = source[:offset].count("\n") + 1
                problems.append(
                    f"lib/{name}:{line}: an authenticated request without "
                    f"allow_redirects=False. A redirect would forward the credential.")

    # Boundary 4: load lib/_env.py on its own (it only needs the standard library)
    # and check that the user's file is the first place credentials are read from.
    spec = importlib.util.spec_from_file_location("needythreads_env_check", ENV)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        candidates = module.env_candidates()
        if not candidates or candidates[0] != module.user_env_path():
            problems.append(
                "lib/_env.py reads a .env from the working folder before "
                "~/.needythreads/.env. A stray .env could then replace the user's key.")
    except Exception as exc:  # a broken module is itself a boundary failure
        problems.append(f"lib/_env.py could not be checked: {exc!r}")

    if problems:
        print("Security boundaries:\n" + "\n".join("  " + p for p in problems))
        return 1

    print("OK: .env cannot name an executable, nothing loads it behind load_env, the user's "
          "own file is read first, and no authenticated request follows redirects.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
