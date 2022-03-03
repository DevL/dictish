from tutorial.dictish_step_6 import Dictish


def test_two_empty_dictish_are_equal():
    assert Dictish() == Dictish()


def test_two_dictish_with_same_key_value_pairs_in_the_same_order_are_equal():
    a_dictish = Dictish([("a", 1), ("b", 2)])
    another_dictish = Dictish([("a", 1), ("b", 2)])

    assert a_dictish == another_dictish


def test_two_dictish_with_same_key_value_pairs_in_different_order_are_equal():
    a_dictish = Dictish([("a", 1), ("b", 2)])
    another_dictish = Dictish([("b", 2), ("a", 1)])

    assert a_dictish == another_dictish


def test_two_dictish_with_different_key_value_pairs_are_not_equal():
    a_dictish = Dictish([("a", 1), ("b", 2)])
    another_dictish = Dictish([("a", 1), ("b", 3)])

    assert a_dictish != another_dictish
