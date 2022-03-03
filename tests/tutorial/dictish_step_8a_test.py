from tutorial.dictish_step_8a import Dictish


def test_merging_two_dictish():
    some_data = Dictish([("a", 1), ("b", 2)])
    more_data = Dictish([("a", 2), ("c", 3)])
    expected = Dictish([("a", 2), ("b", 2), ("c", 3)])
    assert some_data | more_data == expected
