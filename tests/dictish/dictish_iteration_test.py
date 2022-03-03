from dictish import Dictish

DICTISH = Dictish([("a", 1), ("b", 2), ("c", 3)])


def test_a_dictish_can_be_iterated_over_its_keys_implicitly():
    assert list(Dictish([("a", 1), ("b", 2), ("c", 3)])) == ["a", "b", "c"]


def test_a_dictish_can_be_iterated_over_its_keys():
    assert list(DICTISH.keys()) == ["a", "b", "c"]


def test_a_dictish_can_be_iterated_over_its_values():
    assert list(DICTISH.values()) == [1, 2, 3]


def test_a_dictish_can_be_iterated_over_its_items():
    assert list(DICTISH.items()) == [("a", 1), ("b", 2), ("c", 3)]
