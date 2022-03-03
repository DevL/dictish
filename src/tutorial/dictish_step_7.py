class Dictish:
    def __init__(self, *args):
        """
        Example: Dictish([("first", 1), ("second", 2)])
        """
        self.keys_and_values = []
        if args:
            for key_and_value in args[0]:
                if key_and_value not in self.keys_and_values:
                    self.keys_and_values.append(key_and_value)

    def __eq__(self, other):
        """
        Two dictish are equal if they contain the same key-value pairs, regardless of order.
        """
        return all((key_and_value in self.items() for key_and_value in other.items()))

    def items(self):
        return iter(self.keys_and_values)
