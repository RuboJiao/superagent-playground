"""Tiny demo module for the dsh-superagent playground.

`greet` accepts any text name, including non-ASCII ones, and normalises it to
Unicode NFC so canonically equivalent spellings produce identical greetings.

Run it as a script to greet a name: `python3 greet.py <name>`.
"""

import sys
import unicodedata


def greet(name: str) -> str:
    """Return a greeting for `name`, normalised to Unicode NFC."""
    return f"Hello, {unicodedata.normalize('NFC', name)}!"


def main(argv=None) -> int:
    """Print the greeting for the single name in `argv` and return an exit code."""
    args = sys.argv[1:] if argv is None else list(argv)
    if len(args) != 1:
        print("usage: python3 greet.py <name>", file=sys.stderr)
        return 2
    print(greet(args[0]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
