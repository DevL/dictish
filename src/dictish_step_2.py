class Dictish:
    def __init__(self, *args):
        """
        Example: Dictish([("first", 1), ("second", 2)])
        """
        self.keys_and_values = args[0] if args else []

    def __bool__(self):
        return bool(self.keys_and_values)

    def __iter__(self):
        """
        https://docs.python.org/3/library/stdtypes.html#typeiter
        """
        return (key for key, value in self.keys_and_values)
