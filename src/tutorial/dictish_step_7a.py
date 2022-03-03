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

    def __eq__(self, other):
        """
        Two dictish are equal if they contain the same key-value pairs, regardless of order.
        """
        return all((key_and_value in self.items() for key_and_value in other.items()))

    def items(self):
        return iter(self.keys_and_values)
