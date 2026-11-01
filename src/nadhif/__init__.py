"""nadhif (نظيف) — a small library for cleaning Arabic text."""

from .core import (
    clean,
    normalize,
    remove_tashkeel,
    remove_tatweel,
    to_english_digits,
)

__all__ = [
    "clean",
    "normalize",
    "remove_tashkeel",
    "remove_tatweel",
    "to_english_digits",
]

__version__ = "0.1.0"
