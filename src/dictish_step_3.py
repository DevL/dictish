class Dictish:
    def __init__(self, *args):
        """
        Example: Dictish([("first", 1), ("second", 2)])
        """
        self.keys_and_values = args[0] if args else []

    def items(self):
        return iter(self.keys_and_values)

    def keys(self):
        return (key for key, value in self.keys_and_values)

    def values(self):
        return (value for key, value in self.keys_and_values)
