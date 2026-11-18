"""Build the Bharatnomy front repo from the pinned warehouse commit.

Usage:
    python build.py                 # build with the SHA in config/warehouse.lock
    python build.py --check         # build checks only, on the files already in states/
    python build.py --update-lock   # move the lock to the warehouse's latest main, then build

The code lives in the frontbuild/ package; this file only handles the command line.
"""
from __future__ import annotations

import argparse
import json
import sys

from frontbuild import warehouse
from frontbuild.checks import run_checks
from frontbuild.docs import append_changelog, changelog_entry
from frontbuild.pipeline import BUILD_INFO, BUILD_REPORT, run_build


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="only run checks on the existing output")
    parser.add_argument("--update-lock", action="store_true", help="pin the latest warehouse main, then build")
    args = parser.parse_args()

    lock = warehouse.read_lock()
    old_sha = lock["sha"]
    old_info = json.loads(BUILD_INFO.read_text()) if BUILD_INFO.exists() else None
    if args.update_lock:
        new_sha = warehouse.remote_main_sha(lock["url"])
        print(f"Lock: {lock['sha'][:12]} -> {new_sha[:12]}")
        warehouse.write_lock(lock["url"], new_sha)
        lock["sha"] = new_sha

    wh = warehouse.ensure_warehouse(lock["url"], lock["sha"])
    if not args.check:
        report = run_build(wh, lock["sha"])
        print(f"Built from warehouse {lock['sha'][:12]}. See {BUILD_REPORT.name}.")
        if args.update_lock and lock["sha"] != old_sha:
            append_changelog(changelog_entry(old_sha, lock["sha"], old_info, json.loads(BUILD_INFO.read_text())))
            print("Added a CHANGELOG.md entry.")
        if report.sections.get("Errors"):
            print("Build finished WITH ERRORS (see the 'Errors' section).")
    problems, warnings = run_checks(wh)
    for w in warnings:
        print(f"WARN  {w}")
    for p in problems:
        print(f"FAIL  {p}")
    print("Checks passed." if not problems else f"{len(problems)} check(s) failed.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
