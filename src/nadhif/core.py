"""Core Arabic text-cleaning functions."""

import re

# Arabic diacritics (tashkeel): fathatan .. sukun, plus superscript alef.
_TASHKEEL_RE = re.compile("[ً-ْٰ]")

_TATWEEL = "ـ"

_NORMALIZE_TABLE = str.maketrans(
    {
        "أ": "ا",
        "إ": "ا",
        "آ": "ا",
        "ة": "ه",
        "ى": "ي",
    }
)

# Arabic-Indic (٠-٩) and Extended Arabic-Indic / Persian (۰-۹) digits.
_DIGITS_TABLE = str.maketrans(
    "٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹",
    "01234567890123456789",
)

_WHITESPACE_RE = re.compile(r"\s+")


def remove_tashkeel(text: str) -> str:
    """Remove Arabic diacritics (harakat), e.g. ``"مُحَمَّد"`` -> ``"محمد"``."""
    return _TASHKEEL_RE.sub("", text)


def remove_tatweel(text: str) -> str:
    """Remove tatweel/kashida (ـ), e.g. ``"مـــحمد"`` -> ``"محمد"``."""
    return text.replace(_TATWEEL, "")


def normalize(text: str) -> str:
    """Normalize letters: أ/إ/آ -> ا, ة -> ه, ى -> ي."""
    return text.translate(_NORMALIZE_TABLE)


def to_english_digits(text: str) -> str:
    """Convert Arabic-Indic and Persian digits to Western digits (0-9)."""
    return text.translate(_DIGITS_TABLE)


def clean(text: str) -> str:
    """Apply all cleaning steps and collapse/trim extra whitespace."""
    text = remove_tashkeel(text)
    text = remove_tatweel(text)
    text = normalize(text)
    text = to_english_digits(text)
    return _WHITESPACE_RE.sub(" ", text).strip()
