"""Tiny demo module for the dsh-superagent playground.

Deliberately incomplete: `greet` only handles plain ASCII names and has no
tests, so an agent has something real to improve on its first ticket.
"""


def greet(name: str) -> str:
    """Return a greeting for `name`."""
    return f"Hello, {name}!"
