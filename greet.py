"""Tiny demo module for the dsh-superagent playground.

`greet` accepts any text name, including non-ASCII ones, and normalises it to
Unicode NFC so canonically equivalent spellings produce identical greetings.
"""

import unicodedata


def greet(name: str) -> str:
    """Return a greeting for `name`, normalised to Unicode NFC."""
    return f"Hello, {unicodedata.normalize('NFC', name)}!"
