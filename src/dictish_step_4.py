class Dictish:
    def __init__(self, *args):
        """
        Example: Dictish([("first", 1), ("second", 2)])
        """
        self.keys_and_values = args[0] if args else []

    def __bool__(self):
        return bool(self.keys_and_values)

    def __getitem__(self, lookup_key):
        try:
            return next(value for key, value in self.keys_and_values if key == lookup_key)
        except StopIteration:
            raise KeyError(lookup_key)

    def __iter__(self):
        return self.keys()

    def items(self):
        return iter(self.keys_and_values)

    def keys(self):
        return (key for key, value in self.keys_and_values)

    def values(self):
        return (value for key, value in self.keys_and_values)
