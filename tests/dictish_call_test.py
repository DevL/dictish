from dictish import Dictish

LETTER_TO_NUMBER = Dictish([("a", 1), ("b", 2), ("c", 3)])


def test_a_dictish_called_with_a_missing_key_returns_None():
    assert LETTER_TO_NUMBER("d") is None


def test_a_dictish_called_with_a_missing_key_returns_the_default():
    assert LETTER_TO_NUMBER("d", 4) == 4


def test_a_dictish_called_with_an_existing_key_returns_its_value():
    assert LETTER_TO_NUMBER("b") == 2
