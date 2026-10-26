"""Internal helper to load .env when python-dotenv is available."""
from __future__ import annotations

import os
from pathlib import Path

_ENV_LOADED = False
#: The only variables a project .env may set. Anything the bundle *executes*
#: or routes traffic through has to come from the launch environment: a .env
#: that arrives with a clone, or that lands in a parent directory, is not a
#: trusted source for the name of a command to run.
_DOTENV_VARIABLES = (
    "APIFY_TOKEN", "PUBLORA_API_KEY", "THREADS_PLATFORM_ID", "PIXFARO_TOKEN", "PIXFARO_API_KEY",
)

#: Where each variable came from: a file path, or "environment" when it was
#: already set before the bundle looked at any file.
_SOURCES: dict[str, str] = {}
#: Credentials a lower-priority .env also defines with a different value. They
#: are ignored, and reported so the user can see a stray file.
_IGNORED: list[tuple[str, str]] = []


def user_env_path() -> Path:
    """The per-user credentials file, found from any working directory."""
    return Path.home() / ".needythreads" / ".env"


def env_candidates() -> list[Path]:
    """Where `load_env` looks, most trusted first.

    1. `~/.needythreads/.env`, the file the user owns.
    2. A `.env` found upward from the working directory.
    3. A `.env` at the repository root (this file's parent's parent).

    The first source to define a name wins. A `.env` that arrives in a
    downloaded or cloned folder therefore can never replace the user's own key:
    it could otherwise route the user's drafts to someone else's Publora account.
    """
    out: list[Path] = [user_env_path()]
    try:
        from dotenv import find_dotenv

        found = find_dotenv(usecwd=True)
        if found:
            path = Path(found)
            if path not in out:
                out.append(path)
    except ImportError:
        cur = Path.cwd()
        for d in [cur, *cur.parents]:
            if (d / ".env").is_file():
                path = d / ".env"
                if path not in out:
                    out.append(path)
                break
    root = Path(__file__).resolve().parents[1] / ".env"
    if root not in out:
        out.append(root)
    return out


def env_source(name: str) -> str | None:
    """Where `name` was read from: a file path, "environment", or None."""
    return _SOURCES.get(name)


def ignored_credentials() -> list[tuple[str, str]]:
    """(variable, file) pairs a lower-priority .env defined with another value."""
    return list(_IGNORED)


def load_env(force: bool = False) -> None:
    """Load environment variables from .env if python-dotenv is installed.

    Safe no-op if python-dotenv is missing, preserving Tier 0 (manual)
    zero-dependency operation. Reads `~/.needythreads/.env` first, then the
    working directory, then the repository root. Only bundle API credentials and
    the platform id are loaded. Executables and transport settings must come
    from the launch environment. Existing environment variables are preserved.
    """
    global _ENV_LOADED
    if _ENV_LOADED and not force:
        return

    _SOURCES.clear()
    _IGNORED.clear()
    for name in _DOTENV_VARIABLES:
        if name in os.environ:
            _SOURCES[name] = "environment"

    try:
        from dotenv import dotenv_values

        for path in env_candidates():
            if not path.is_file():
                continue
            values = dotenv_values(path)
            for name in _DOTENV_VARIABLES:
                value = values.get(name)
                if value is None:
                    continue
                if name in os.environ:
                    if os.environ[name] != value and _SOURCES.get(name) != str(path):
                        _IGNORED.append((name, str(path)))
                    continue
                os.environ[name] = value
                _SOURCES[name] = str(path)
    except ImportError:
        pass

    _ENV_LOADED = True
