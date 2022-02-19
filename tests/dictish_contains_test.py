from dictish import Dictish


AN_EMPTY_DICTISH = Dictish()
LETTER_TO_NUMBER = Dictish([("a", 1), ("b", 2), ("c", 3)])


def test_an_empty_dictish_contains_nothing():
    assert ("a" in AN_EMPTY_DICTISH) is False


def test_a_populated_dictish_contains_some_keys():
    assert ("a" in LETTER_TO_NUMBER) is True


def test_a_populated_dictish_does_not_contain_a_missing_key():
    assert ("z" in LETTER_TO_NUMBER) is False
