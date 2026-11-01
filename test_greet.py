"""Tests for the `greet` helper in greet.py."""

import pytest

from greet import greet


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
