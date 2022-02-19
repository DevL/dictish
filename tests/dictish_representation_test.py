from dictish import Dictish


AN_EMPTY_DICTISH = Dictish()
LETTER_TO_NUMBER = Dictish([("a", 1), ("b", 2), ("c", 3)])


def test_representing_an_empty_dictish():
    assert repr(AN_EMPTY_DICTISH) == "Dictish()"
    assert str(AN_EMPTY_DICTISH) == "Dictish()"


def test_representing_a_populated_dictish():
    assert repr(LETTER_TO_NUMBER) == "Dictish([('a', 1), ('b', 2), ('c', 3)])"
    assert str(LETTER_TO_NUMBER) == "Dictish([('a', 1), ('b', 2), ('c', 3)])"
