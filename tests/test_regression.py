from analyzer import count_words


def test_regresion_palabras():
    assert count_words("Hola mundo") == 3
