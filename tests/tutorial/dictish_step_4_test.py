import pytest
from tutorial.dictish_step_4 import Dictish

DICTISH = Dictish([("a", 1), ("b", 2), ("c", 3)])


def test_a_dictish_is_subscriptable():
    assert DICTISH["b"] == 2


def test_subscript_with_a_missing_key():
    with pytest.raises(KeyError, match="missing"):
        DICTISH["missing"]
