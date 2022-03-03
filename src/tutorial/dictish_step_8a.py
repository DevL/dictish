class Dictish:
    def __init__(self, *args):
        """
        Example: Dictish([("first", 1), ("second", 2)])
        """
        if args:
            self.keys_and_values = list(_deduplicate(args[0], [], []))
        else:
            self.keys_and_values = []

    def __eq__(self, other):
        """
        Two dictish are equal if they contain the same key-value pairs, regardless of order.
        """
        return all((key_and_value in self.items() for key_and_value in other.items()))

    def __or__(self, other):
        return self.__class__(_deduplicate(other.items(), list(self.keys()), list(self.values())))

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
