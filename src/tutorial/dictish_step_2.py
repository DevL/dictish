class Dictish:
    def __init__(self, *args):
        """
        Example: Dictish([("first", 1), ("second", 2)])
        """
        self.keys_and_values = args[0] if args else []

    def __bool__(self):
        return bool(self.keys_and_values)

    def __iter__(self):
        return (key for key, value in self.keys_and_values)

    def __len__(self):
        return len(self.keys_and_values)
