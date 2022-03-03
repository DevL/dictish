from .keys_and_values import KeysAndValues, deduplicate


class Dictish:
    def __init__(self, key_value_pairs=None):
        """
        Creates a new Dictish.

        >>> Dictish()
        Dictish()

        Given a sequence of key-value pairs, the input is deduplicated on the keys.

        >>> Dictish([("a", 1), ("b", 2), ("a", 3)])
        Dictish([('a', 3), ('b', 2)])
        """
        self.keys_and_values = KeysAndValues(key_value_pairs)

    def __add__(self, key_and_value):
        """
        >>> Dictish([("a", 1), ("b", 2)]) + ("c", 3)
        Dictish([('a', 1), ('b', 2), ('c', 3)])
        """
        return self | self.__class__([key_and_value])

    def __call__(self, key, default=None):
        """
        >>> Dictish([("a", 1), ("b", 2)])("a")
        1

        >>> Dictish([("a", 1), ("b", 2)])("c") is None
        True

        >>> Dictish([("a", 1), ("b", 2)])("c", 3)
        3
        """
        return self.get(key, default)

    def __eq__(self, other):
        """
        Two Dictish are equal if they contain the same key-value pairs, regardless of order.

        >>> Dictish([("a", 1), ("b", 2)]) == Dictish([("b", 2), ("a", 1)])
        True

        >>> Dictish([("a", 1)]) == Dictish([("b", 2), ("a", 1)])
        False

        >>> Dictish([("a", 1), ("b", 2)]) == Dictish([("b", 2)])
        False
        """
        return len(self) == len(other) and all(
            (key_and_value in self.items() for key_and_value in other.items())
        )

    def __ge__(self, other):
        """
        Tests whether this dictish is a superset of another object responding to items.
        """
        return set(self.items()) >= set(other.items())

    def __gt__(self, other):
        """
        Tests whether this dictish is a strict superset of another object responding to items.
        """
        return set(self.items()) > set(other.items())

    def __getitem__(self, lookup_key):
        """
        >>> Dictish([("a", 1), ("b", 2)])["a"]
        1
        """
        try:
            return next(value for key, value in self.items() if key == lookup_key)
        except StopIteration:
            raise KeyError(lookup_key)

    def __iter__(self):
        """
        Iterates over the keys of the Dictish.

        >>> list(iter(Dictish([("key", "value")])))
        ['key']
        """
        return self.keys()

    def __le__(self, other):
        """
        Tests whether this dictish is a subset of another object responding to items.
        """
        return set(self.items()) <= set(other.items())

    def __len__(self):
        """
        >>> len(Dictish([("key", "value")]))
        1
        """
        return len(self.keys_and_values)

    def __lt__(self, other):
        """
        Tests whether this dictish is a strict subset of another object responding to items.
        """
        return set(self.items()) < set(other.items())

    def __or__(self, other):
        """
        >>> Dictish([("a", 1), ("b", 2)]) | Dictish([("a", 4), ("c", 3)])
        Dictish([('a', 4), ('b', 2), ('c', 3)])
        """
        return self.__class__(deduplicate(other.items(), list(self.keys()), list(self.values())))

    def __repr__(self):
        """
        >>> repr(Dictish([("a", 1), ("b", 2)]))
        "Dictish([('a', 1), ('b', 2)])"
        """
        keys_and_values = self.keys_and_values if self.keys_and_values else ""
        return f"{self.__class__.__name__}({keys_and_values})"

    def __str__(self):
        """
        >>> str(Dictish([("a", 1), ("b", 2)]))
        "{'a': 1, 'b': 2}"
        """
        pairs = (f"'{key}': {value}" for key, value in self.items())
        return "{" + ", ".join(pairs) + "}"

    def get(self, key, default=None):
        """
        >>> Dictish([("a", 1), ("b", 2)]).get("a")
        1

        >>> Dictish([("a", 1), ("b", 2)]).get("c") is None
        True

        >>> Dictish([("a", 1), ("b", 2)]).get("c", 3)
        3
        """
        try:
            return self[key]
        except KeyError:
            return default

    def items(self):
        """
        >>> list(Dictish([("a", 1), ("b", 2)]).items())
        [('a', 1), ('b', 2)]
        """
        return iter(self.keys_and_values)

    def keys(self):
        """
        >>> list(Dictish([("a", 1), ("b", 2)]).keys())
        ['a', 'b']
        """
        return (key for key, value in self.keys_and_values)

    def values(self):
        """
        >>> list(Dictish([("a", 1), ("b", 2)]).values())
        [1, 2]
        """
        return (value for key, value in self.keys_and_values)
