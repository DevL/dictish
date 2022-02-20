class Dictish:
    def __init__(self, *args):
        """
        Example: Dictish([("first", 1), ("second", 2)])
        """
        if args:
            self.keys_and_values = list(_deduplicate(args[0], [], []))
        else:
            self.keys_and_values = []

    def __add__(self, key_and_value):
        return self | self.__class__([key_and_value])

    def __bool(self):
        """
        Redundant as __len__ is defined.
        """
        return bool(self.keys_and_values)

    def __contains__(self, key):
        """
        Supports the "in" keyword. Redundant as __iter__ is defined.
        """
        return key in self.keys()

    def __eq__(self, other):
        """
        Two dictish are equal if they contain the same key-value pairs, regardless of order.
        """
        return all((key_and_value in self.items() for key_and_value in other.items()))

    def __getitem__(self, lookup_key):
        try:
            return next(value for key, value in self.items() if key == lookup_key)
        except StopIteration:
            # FIXME: get should not exercise __missing__
            return self.__missing__(lookup_key)

    def __iter__(self):
        return self.keys()

    def __len__(self):
        return len(self.keys_and_values)

    def __missing__(self, key):
        """
        Behave like a defaultdict.
        """
        raise KeyError(key)

    def __or__(self, other):
        return self.__class__(_deduplicate(other.items(), list(self.keys()), list(self.values())))
        # keys = list(self.keys())
        # values = list(self.values())
        # for key, value in other.items():
        #     if key in keys:
        #         index = keys.index(key)
        #         values[index] = value
        #     else:
        #         keys.append(key)
        #         values.append(value)
        # return Dictish(zip(keys, values))

    def __repr__(self):
        keys_and_values = self.keys_and_values if self.keys_and_values else ""
        return f"{self.__class__.__name__}({keys_and_values})"

    def __str__(self):
        pairs = (f"'{key}': {value}" for key, value in self.items())
        return "{" + ", ".join(pairs) + "}"

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def items(self):
        return iter(self.keys_and_values)

    def keys(self):
        return (key for key, value in self.keys_and_values)

    def values(self):
        return (value for key, value in self.keys_and_values)


def _deduplicate(keys_and_values, keys, values):
    for key, value in keys_and_values:
        if key in keys:
            index = keys.index(key)
            values[index] = value
        else:
            keys.append(key)
            values.append(value)
    return zip(keys, values)
