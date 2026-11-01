"""Tests for the `greet` helper in greet.py."""

import subprocess
import sys
from pathlib import Path

import pytest

from greet import greet

GREET_SCRIPT = Path(__file__).with_name("greet.py")


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(GREET_SCRIPT), *args],
        capture_output=True,
        text=True,
    )


@pytest.mark.parametrize(
    "name",
    ["world", "Ada Lovelace", "José", "李雷", "Ω", "🙂", ""],
)
def test_greet_returns_greeting(name):
    assert greet(name) == f"Hello, {name}!"


def test_greet_normalizes_decomposed_non_ascii_names():
    # Canonically equivalent spellings must greet identically: "e" followed by
    # COMBINING ACUTE ACCENT (U+0301) is the same name as the composed "é".
    assert greet("Jose\u0301") == "Hello, José!"


def test_cli_prints_greeting_for_a_name():
    result = run_cli("Ada Lovelace")
    assert result.returncode == 0
    assert result.stdout == "Hello, Ada Lovelace!\n"
    assert result.stderr == ""


def test_cli_without_a_name_prints_usage_and_exits_2():
    result = run_cli()
    assert result.returncode == 2
    assert result.stdout == ""
    assert result.stderr.strip() == "usage: python3 greet.py <name>"
