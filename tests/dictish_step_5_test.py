from dictish_step_5 import Dictish

DICTISH = Dictish([("a", 1), ("b", 2), ("c", 3)])


def test_get_a_value_from_a_dictish():
    assert DICTISH.get("c") == 3


def test_get_a_missing_value_from_a_dictish():
    assert DICTISH.get("missing") is None


def test_get_a_missing_value_from_a_dictish_using_a_default():
    assert DICTISH.get("missing", "default") == "default"
