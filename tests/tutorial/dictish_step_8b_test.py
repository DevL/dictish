from tutorial.dictish_step_8b import Dictish


SOME_DATA = Dictish([("a", 1), ("b", 2)])


def test_adding_a_new_key_value_pair():
    expected = Dictish([("a", 1), ("b", 2), ("c", 3)])
    assert SOME_DATA + ("c", 3) == expected


def test_adding_an_existing_key():
    expected = Dictish([("a", 1), ("b", 4)])
    assert SOME_DATA + ("b", 4) == expected
