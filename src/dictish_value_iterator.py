class DictishValueIterator:
    def __init__(self, dictish):
        self.dictish = dictish
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_value = self.dictish.keys_and_values[self.current_index][1]
            self.current_index += 1
            return next_value
        except IndexError:
            raise StopIteration
