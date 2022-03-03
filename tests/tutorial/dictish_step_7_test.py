from tutorial.dictish_step_7 import Dictish


def test_creating_a_dictish_deduplicates_the_input():
    a_dictish = Dictish([("a", 1), ("a", 1)])

    assert a_dictish == Dictish([("a", 1)])
    assert list(a_dictish.items()) == [("a", 1)]
