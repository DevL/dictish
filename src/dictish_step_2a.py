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
        return DictishKeyIterator(self)


class DictishKeyIterator:
    def __init__(self, dictish):
        self.dictish = dictish
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_key = self.dictish.keys_and_values[self.current_index][0]
            self.current_index += 1
            return next_key
        except IndexError:
            raise StopIteration
