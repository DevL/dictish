class Dictish:
    def __init__(self, *args):
        """
        Example: Dictish([("first", 1), ("second", 2)])
        """
        keys = []
        values = []
        if args:
            for key, value in args[0]:
                if key in keys:
                    index = keys.index(key)
                    values[index] = value
                else:
                    keys.append(key)
                    values.append(value)
        self.keys_and_values = list(zip(keys, values))

    def __add__(self, key_and_value):
        return self | self.__class__([key_and_value])

    def __eq__(self, other):
        """
        Two dictish are equal if they contain the same key-value pairs, regardless of order.
        """
        return all((key_and_value in self.items() for key_and_value in other.items()))

    def __getitem__(self, lookup_key):
        try:
            return next(value for key, value in self.keys_and_values if key == lookup_key)
        except StopIteration:
            raise KeyError(lookup_key)

    def __iter__(self):
        return self.keys()

    def __len__(self):
        return len(self.keys_and_values)

    def __or__(self, other):
        keys = list(self.keys())
        values = list(self.values())
        for key, value in other.items():
            if key in keys:
                index = keys.index(key)
                values[index] = value
            else:
                keys.append(key)
                values.append(value)
        return Dictish(zip(keys, values))

    def __repr__(self):
        keys_and_values = self.keys_and_values if self.keys_and_values else ""
        return f"{self.__class__.__name__}({keys_and_values})"

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
