class Dictish:
    def __init__(self, *args):
        """
        Example: Dictish([("first", 1), ("second", 2)])
        """
        if args:
            self.keys_and_values = list(_deduplicate(args[0], [], []))
        else:
            self.keys_and_values = []

    def __repr__(self):
        keys_and_values = self.keys_and_values if self.keys_and_values else ""
        return f"{self.__class__.__name__}({keys_and_values})"

    def __str__(self):
        pairs = (f"'{key}': {value}" for key, value in self.items())
        return "{" + ", ".join(pairs) + "}"

    def items(self):
        return iter(self.keys_and_values)


def _deduplicate(keys_and_values, keys, values):
    for key, value in keys_and_values:
        if key in keys:
            index = keys.index(key)
            values[index] = value
        else:
            keys.append(key)
            values.append(value)
    return zip(keys, values)
