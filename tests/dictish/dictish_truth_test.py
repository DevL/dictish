from dictish import Dictish

AN_EMPTY_DICTISH = Dictish()
LETTER_TO_NUMBER = Dictish([("a", 1), ("b", 2), ("c", 3)])


def test_an_empty_dictish_is_falsey():
    assert bool(AN_EMPTY_DICTISH) is False


def test_a_populated_dictish_is_truthy():
    assert bool(LETTER_TO_NUMBER) is True
