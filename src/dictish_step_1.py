class Dictish:
    def __bool__(self):
        return False

    def __iter__(self):
        """
        https://docs.python.org/3/library/stdtypes.html#typeiter
        """
        return self

    def __next__(self):
        """
        https://docs.python.org/3/library/stdtypes.html#typeiter
        """
        raise StopIteration

    def __len__(self):
        return 0
