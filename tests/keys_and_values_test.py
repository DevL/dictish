from dictish.keys_and_values import KeysAndValues, deduplicate


def test_creating_an_empty_key_value_pair_list():
    assert KeysAndValues() == []


def test_creating_an_populated_key_value_pair_list():
    assert KeysAndValues([("a", 1), ("b", 2)]) == [("a", 1), ("b", 2)]


def test_creating_a_populated_key_value_pair_list_deduplicates():
    assert KeysAndValues([("a", 1), ("a", 2)]) == [("a", 2)]


def test_deduplicating_and_merging_with_existing_keys_and_values():
    result = deduplicate(KeysAndValues([("a", 4), ("c", 3)]), keys=["a", "b"], values=[1, 2])
    assert list(result) == [("a", 4), ("b", 2), ("c", 3)]
