from dictish_step_2 import Dictish

# from dictish_step_2a import Dictish


def test_a_dictish_can_be_created_using_a_list_of_tuples():
    Dictish([("a", 1), ("b", 2), ("c", 3)])


def test_a_dictish_can_be_iterated_over_its_keys_implicitly():
    assert list(Dictish([("a", 1), ("b", 2), ("c", 3)])) == ["a", "b", "c"]


def test_a_populated_dictish_is_truthy():
    assert bool(Dictish([("a", 1)])) is True


def test_the_length_of_a_populated_dictish():
    assert len(Dictish([("a", 1), ("b", 2), ("c", 3)])) is 3
