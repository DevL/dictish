from dictish_step_7 import Dictish as BrokenDictish
from dictish_step_7a import Dictish


def test_deduplicating_the_entire_input_is_not_enough():
    broken_dictish = BrokenDictish([("a", 1), ("a", 2)])

    assert list(broken_dictish.items()) == [("a", 1), ("a", 2)]


def test_creating_a_dictish_deduplicates_the_keys_retaining_the_last_value():
    a_dictish = Dictish([("a", 1), ("a", 2)])
    another_dictish = Dictish([("a", 2)])

    assert list(a_dictish.items()) == [("a", 2)]
    assert list(another_dictish.items()) == [("a", 2)]
    assert a_dictish == another_dictish
