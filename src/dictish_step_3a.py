from dictish_key_iterator import DictishKeyIterator
from dictish_value_iterator import DictishValueIterator


class Dictish:
    def __init__(self, *args):
        """
        Example: Dictish([("first", 1), ("second", 2)])
        """
        self.keys_and_values = args[0] if args else []

    def __iter__(self):
        return self.keys()

    def __len__(self):
        return len(self.keys_and_values)

    def items(self):
        return iter(self.keys_and_values)

    def keys(self):
        return DictishKeyIterator(self)

    def values(self):
        return DictishValueIterator(self)
