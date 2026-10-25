import pytest

from analyzer import analyze_text, count_characters, count_sentences, count_words


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        ("  \t\n", 0),
        ("Hola mundo", 2),
        ("¡Hola, México!", 2),
        ("Python 3", 2),
        ("uno-dos_tres", 3),
        ("...😀", 0),
        ("cafe\u0301", 1),
    ],
)
def test_words(text, expected):
    assert count_words(text) == expected


@pytest.mark.parametrize(
    ("text", "spaces", "expected"),
    [
        ("", True, 0),
        ("a b", True, 3),
        ("a b", False, 2),
        ("a\t\nb", False, 2),
        ("cafe\u0301", True, 4),
        ("😀", True, 1),
    ],
)
def test_characters(text, spaces, expected):
    assert count_characters(text, include_spaces=spaces) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        ("...?!", 0),
        ("Hola", 1),
        ("Hola. Adiós! ¿Bien?", 3),
        ("Hola!!! Sí...", 2),
        (" \n ", 0),
        ("😀", 0),
        ("123.", 1),
    ],
)
def test_sentences(text, expected):
    assert count_sentences(text) == expected


@pytest.mark.parametrize("function", [count_words, count_characters, count_sentences, analyze_text])
@pytest.mark.parametrize("invalid", [None, 123, [], {}, True])
def test_invalid_text(function, invalid):
    with pytest.raises(TypeError, match="cadena"):
        function(invalid)


def test_invalid_spaces_option():
    with pytest.raises(TypeError, match="booleano"):
        count_characters("Hola", include_spaces="no")


def test_summary():
    assert analyze_text("Hola mundo.") == {
        "words": 2,
        "characters": 11,
        "characters_without_spaces": 10,
        "sentences": 1,
    }


def test_empty_summary():
    assert analyze_text("") == {
        "words": 0,
        "characters": 0,
        "characters_without_spaces": 0,
        "sentences": 0,
    }
