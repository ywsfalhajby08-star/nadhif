# nadhif · نظيف

مكتبة Python بسيطة لتنظيف النص العربي.
A simple Python library for cleaning Arabic text.

[العربية](#العربية) · [English](#english)

---

## العربية

<div dir="rtl">

### التثبيت

```bash
pip install .
```

### الدوال

| الدالة | الوصف |
|---|---|
| `remove_tashkeel(text)` | حذف التشكيل (الفتحة، الضمة، الكسرة، الشدة، السكون، التنوين...) |
| `remove_tatweel(text)` | حذف التطويل (ـ) |
| `normalize(text)` | توحيد الحروف: أ إ آ ← ا، ة ← ه، ى ← ي |
| `to_english_digits(text)` | تحويل الأرقام العربية (٠-٩) والفارسية (۰-۹) إلى أرقام إنجليزية (0-9) |
| `clean(text)` | تطبيق كل ما سبق مع حذف المسافات الزائدة |

### مثال

```python
from nadhif import clean, remove_tashkeel, normalize

remove_tashkeel("مُحَمَّد")      # 'محمد'
normalize("أحمد في المدرسة")    # 'احمد في المدرسه'
clean("  أَهْلاً   بِكُمْ فـــي   المَدْرَسَة رقم ٤٢  ")
# 'اهلا بكم في المدرسه رقم 42'
```

### تشغيل الاختبارات

```bash
pip install -e ".[dev]"
pytest
```

### الرخصة

MIT — راجع ملف [LICENSE](LICENSE).

</div>

---

## English

### Installation

```bash
pip install .
```

### Functions

| Function | Description |
|---|---|
| `remove_tashkeel(text)` | Remove Arabic diacritics (fatha, damma, kasra, shadda, sukun, tanween, ...) |
| `remove_tatweel(text)` | Remove tatweel / kashida (ـ) |
| `normalize(text)` | Normalize letters: أ إ آ → ا, ة → ه, ى → ي |
| `to_english_digits(text)` | Convert Arabic-Indic (٠-٩) and Persian (۰-۹) digits to Western digits (0-9) |
| `clean(text)` | Apply all of the above and collapse extra whitespace |

### Example

```python
from nadhif import clean, remove_tashkeel, normalize

remove_tashkeel("مُحَمَّد")      # 'محمد'
normalize("أحمد في المدرسة")    # 'احمد في المدرسه'
clean("  أَهْلاً   بِكُمْ فـــي   المَدْرَسَة رقم ٤٢  ")
# 'اهلا بكم في المدرسه رقم 42'
```

### Running tests

```bash
pip install -e ".[dev]"
pytest
```

### License

MIT — see [LICENSE](LICENSE).
