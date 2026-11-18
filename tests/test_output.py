"""Run the same checks as `python build.py --check` on the committed output."""
from frontbuild import warehouse
from frontbuild.checks import run_checks


def test_built_output_passes_checks():
    lock = warehouse.read_lock()
    problems, _ = run_checks(warehouse.ensure_warehouse(lock["url"], lock["sha"]))
    assert problems == []
