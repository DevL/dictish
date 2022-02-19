from dictish import Dictish

SOME_DATA = Dictish([("a", 1), ("b", 2)])
MORE_DATA = Dictish([("a", 2), ("c", 3)])


def test_merging_two_dictish():
    expected = Dictish([("a", 2), ("b", 2), ("c", 3)])
    assert SOME_DATA | MORE_DATA == expected
