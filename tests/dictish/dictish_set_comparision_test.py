from dictish import Dictish

AN_EMPTY_DICTISH = Dictish()
LETTER_TO_NUMBER = Dictish([("a", 1), ("b", 2)])
A_STRICT_SUBSET = Dictish([("a", 1)])
A_STRICT_SUPERSET = Dictish([("a", 1), ("b", 2), ("c", 3)])


def test_being_a_subset():
    assert LETTER_TO_NUMBER <= LETTER_TO_NUMBER
    assert LETTER_TO_NUMBER <= A_STRICT_SUPERSET
    assert not (LETTER_TO_NUMBER <= A_STRICT_SUBSET)


def test_being_a_strict_subset():
    assert LETTER_TO_NUMBER < A_STRICT_SUPERSET
    assert not LETTER_TO_NUMBER < LETTER_TO_NUMBER


def test_being_a_superset():
    assert LETTER_TO_NUMBER >= LETTER_TO_NUMBER
    assert LETTER_TO_NUMBER >= A_STRICT_SUBSET
    assert not (LETTER_TO_NUMBER >= A_STRICT_SUPERSET)


def test_being_a_strict_superset():
    assert LETTER_TO_NUMBER > A_STRICT_SUBSET
    assert not LETTER_TO_NUMBER > LETTER_TO_NUMBER
