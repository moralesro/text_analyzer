"""Análisis sencillo y determinista de texto Unicode."""

import re
import unicodedata


def _validate(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("El texto debe ser una cadena.")
    return unicodedata.normalize("NFC", text)


def count_words(text: str) -> int:
    """Cuenta grupos alfanuméricos; guiones y signos separan palabras."""
    return len(re.findall(r"[^\W_]+", _validate(text)))


def count_characters(text: str, include_spaces: bool = True) -> int:
    """Cuenta puntos de código normalizados; opcionalmente omite espacios blancos."""
    normalized = _validate(text)
    if not isinstance(include_spaces, bool):
        raise TypeError("include_spaces debe ser booleano.")
    if include_spaces:
        return len(normalized)
    return sum(not char.isspace() for char in normalized)


def count_sentences(text: str) -> int:
    """Cuenta segmentos con letras o números separados por punto, ! o ?."""
    return sum(
        any(char.isalnum() for char in fragment)
        for fragment in re.split(r"[.!?]+", _validate(text))
    )


def analyze_text(text: str) -> dict[str, int]:
    """Devuelve el resumen del texto; una cadena vacía produce ceros."""
    return {
        "words": count_words(text),
        "characters": count_characters(text),
        "characters_without_spaces": count_characters(text, include_spaces=False),
        "sentences": count_sentences(text),
    }
