from dictish_step_1 import Dictish


def test_an_empty_dictish_can_be_created():
    Dictish()


def test_an_empty_dictish_can_be_iterated():
    assert list(Dictish()) == []


def test_an_empty_dictish_is_falsey():
    assert bool(Dictish()) is False


def test_the_length_of_an_empty_dictish_is_zero():
    assert len(Dictish()) == 0
