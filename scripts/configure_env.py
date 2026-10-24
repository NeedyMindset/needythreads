#!/usr/bin/env python3
"""Fill in .env without opening it: ask for the Publora key, find the Threads ID.

The key is typed hidden, checked against Publora before anything is written,
and never printed. The Platform ID is read from your connected Threads account,
so there is nothing to copy by hand. Safe to run again: values that are already
set are kept.

Run from the repo root (setup.ps1 and setup.sh call it for you):

    python3 scripts/configure_env.py
"""
from __future__ import annotations

import getpass
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

ENV_FILE = ROOT / ".env"
TEMPLATE = ROOT / ".env.example"
KEY_PLACEHOLDER = "sk_your_key_here"
ID_PLACEHOLDER = "threads-your_id_here"
ID_PATTERN = re.compile(r"^threads-[A-Za-z0-9_-]+$")


def read_value(lines: list[str], name: str) -> str:
    for line in lines:
        if line.startswith(name + "="):
            return line.split("=", 1)[1].strip()
    return ""


def set_value(lines: list[str], name: str, value: str) -> list[str]:
    out, done = [], False
    for line in lines:
        if line.startswith(name + "="):
            ending = line[len(line.rstrip("\r\n")):]
            out.append(f"{name}={value}{ending or chr(10)}")
            done = True
        else:
            out.append(line)
    if not done:
        if out and not out[-1].endswith("\n"):
            out[-1] += "\n"
        out.append(f"{name}={value}\n")
    return out


def choose_connection(connections: list[dict]) -> str:
    if len(connections) == 1:
        c = connections[0]
        print(f"Found your Threads account: @{c.get('username', '?')}")
        return str(c["platformId"])
    print("Several Threads accounts are connected:")
    for i, c in enumerate(connections, 1):
        print(f"  {i}. @{c.get('username', '?')}  ({c['platformId']})")
    while True:
        answer = input("Which one do you want to use? Type its number: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(connections):
            return str(connections[int(answer) - 1]["platformId"])


def ask_platform_id() -> str:
    while True:
        answer = input("Paste your Threads Platform ID (threads-...), or press Enter to skip: ").strip()
        if not answer or ID_PATTERN.match(answer):
            return answer
        print("That does not look right. It starts with threads- followed by numbers.")


def main() -> int:
    if not sys.stdin.isatty():
        print("Not an interactive terminal, skipping the key setup. Edit .env by hand instead.")
        return 0

    if not ENV_FILE.exists():
        if not TEMPLATE.exists():
            print("No .env.example found. Run this from the needythreads folder.")
            return 1
        shutil.copyfile(TEMPLATE, ENV_FILE)

    with open(ENV_FILE, encoding="utf-8", newline="") as handle:
        lines = handle.readlines()

    key = read_value(lines, "PUBLORA_API_KEY")
    platform_id = read_value(lines, "THREADS_PLATFORM_ID")
    key_set = bool(key) and key != KEY_PLACEHOLDER
    id_set = bool(platform_id) and platform_id != ID_PLACEHOLDER

    if key_set and id_set:
        print(".env already has a Publora key and a Threads Platform ID. Nothing to do.")
        return 0

    if not key_set:
        key = getpass.getpass("Paste your Publora API key (hidden, Enter to skip): ").strip()
        if not key:
            print("Skipped. Posts will stay in draft mode until you add a key to .env.")
            return 0

    from lib import PubloraClient, PubloraError

    try:
        connections = PubloraClient(api_key=key).threads_connections()
    except PubloraError as exc:
        print(f"Publora refused the key, nothing was saved. {exc}")
        return 1
    except Exception as exc:  # network down, DNS, timeout
        print(f"Could not reach Publora, nothing was saved ({type(exc).__name__}). Try again.")
        return 1

    if not id_set:
        if connections:
            platform_id = choose_connection(connections)
        else:
            print("The key works, but no Threads account is connected yet.")
            print("In Publora: Channels > Add Channel > Threads, then run this again.")
            platform_id = ask_platform_id()

    lines = set_value(lines, "PUBLORA_API_KEY", key)
    if platform_id:
        lines = set_value(lines, "THREADS_PLATFORM_ID", platform_id)

    with open(ENV_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.writelines(lines)

    print(f"Saved to {ENV_FILE}")
    if platform_id:
        print("Publishing is ready.")
    else:
        print("The key is saved. Add THREADS_PLATFORM_ID once Threads is connected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
