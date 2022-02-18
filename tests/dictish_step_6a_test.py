from dictish_step_6 import Dictish


def test_here_is_a_problem():
    a_dictish = Dictish([("a", 1), ("a", 1)])
    another_dictish = Dictish([("a", 1)])

    assert a_dictish == another_dictish
    assert sorted(a_dictish.items()) != sorted(another_dictish.items())
