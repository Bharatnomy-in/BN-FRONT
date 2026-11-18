"""Get the warehouse repo at the commit pinned in config/warehouse.lock.

The clone lives in .cache/warehouse/ (git-ignored). It is a partial, sparse clone:
every dataset folder plus _reference/, but from _sources/ only the DataMeet
district boundaries we need for the GeoJSON.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK_FILE = ROOT / "config" / "warehouse.lock"
CACHE_DIR = ROOT / ".cache" / "warehouse"

# Sparse-checkout patterns (gitignore syntax, "non-cone" mode):
# take everything, drop _sources/, then add back the boundary files.
SPARSE_PATTERNS = ["/*", "!/_sources/", "/_sources/datameet-maps/raw/", "/_sources/datameet-maps/README.md"]


def read_lock() -> dict[str, str]:
    """Return {'url': ..., 'sha': ...} from the lock file."""
    lock: dict[str, str] = {}
    for line in LOCK_FILE.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            lock[key.strip()] = value.strip()
    return lock


def write_lock(url: str, sha: str) -> None:
    LOCK_FILE.write_text(f"url={url}\nsha={sha}\n")


def _git(*args: str, cwd: Path | None = None) -> str:
    result = subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def remote_main_sha(url: str) -> str:
    """Latest commit on the warehouse's main branch (used by --update-lock)."""
    line = _git("ls-remote", url, "refs/heads/main")
    return line.split()[0]


def ensure_warehouse(url: str, sha: str) -> Path:
    """Clone (or update) the warehouse in .cache/ and check out exactly `sha`."""
    if not (CACHE_DIR / ".git").exists():
        CACHE_DIR.parent.mkdir(parents=True, exist_ok=True)
        # blob:none = download file contents only when checked out; --no-checkout so
        # sparse rules apply before any files are written.
        _git("clone", "--filter=blob:none", "--no-checkout", url, str(CACHE_DIR))
        _git("sparse-checkout", "set", "--no-cone", *SPARSE_PATTERNS, cwd=CACHE_DIR)
    else:
        _git("sparse-checkout", "set", "--no-cone", *SPARSE_PATTERNS, cwd=CACHE_DIR)
    try:
        _git("cat-file", "-e", f"{sha}^{{commit}}", cwd=CACHE_DIR)
    except subprocess.CalledProcessError:
        _git("fetch", "--filter=blob:none", "origin", cwd=CACHE_DIR)
    _git("-c", "advice.detachedHead=false", "checkout", "--force", sha, cwd=CACHE_DIR)
    actual = _git("rev-parse", "HEAD", cwd=CACHE_DIR)
    if actual != sha:
        raise RuntimeError(f"Warehouse is at {actual}, expected {sha}")
    return CACHE_DIR
