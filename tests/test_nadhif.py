import pytest

from nadhif import (
    clean,
    normalize,
    remove_tashkeel,
    remove_tatweel,
    to_english_digits,
)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("مُحَمَّد", "محمد"),
        ("السَّلَامُ عَلَيْكُمْ", "السلام عليكم"),
        ("كِتَابٌ", "كتاب"),
        ("رَحْمٰن", "رحمن"),
        ("بدون تشكيل", "بدون تشكيل"),
        ("", ""),
    ],
)
def test_remove_tashkeel(text, expected):
    assert remove_tashkeel(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("مـــحمد", "محمد"),
        ("الســـلام", "السلام"),
        ("ـــ", ""),
        ("عادي", "عادي"),
    ],
)
def test_remove_tatweel(text, expected):
    assert remove_tatweel(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("أحمد", "احمد"),
        ("إسلام", "اسلام"),
        ("آمن", "امن"),
        ("مدرسة", "مدرسه"),
        ("مستشفى", "مستشفي"),
        ("أإآ ة ى", "ااا ه ي"),
    ],
)
def test_normalize(text, expected):
    assert normalize(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("٠١٢٣٤٥٦٧٨٩", "0123456789"),
        ("۰۱۲۳۴۵۶۷۸۹", "0123456789"),
        ("عام ٢٠٢٦", "عام 2026"),
        ("123", "123"),
    ],
)
def test_to_english_digits(text, expected):
    assert to_english_digits(text) == expected


def test_clean_combines_everything():
    text = "  أَهْلاً   بِكُمْ فـــي   المَدْرَسَة رقم ٤٢  "
    assert clean(text) == "اهلا بكم في المدرسه رقم 42"


def test_clean_whitespace_kinds():
    assert clean("\tمرحبا\n\nبالعالم  ") == "مرحبا بالعالم"


def test_clean_empty():
    assert clean("") == ""
    assert clean("   ") == ""
