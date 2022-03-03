import pytest
from dictish import Dictish

DICTISH = Dictish([("a", 1), ("b", 2), ("c", 3)])


def test_a_dictish_is_subscriptable():
    assert DICTISH["b"] == 2


def test_subscript_with_a_missing_key():
    with pytest.raises(KeyError, match="missing"):
        DICTISH["missing"]


def test_get_a_value_from_a_dictish():
    assert DICTISH.get("c") == 3


def test_get_a_missing_value_from_a_dictish():
    assert DICTISH.get("missing") is None


def test_get_a_missing_value_from_a_dictish_using_a_default():
    assert DICTISH.get("missing", "default") == "default"
