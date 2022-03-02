from collections import UserList
from functools import partial


class KeysAndValues(UserList):
    def __init__(self, sequence=None):
        if sequence:
            self.data = list(deduplicate(sequence))
        else:
            self.data = []
        # self.data = list(deduplicate(sequence)) if sequence else []
        # self.data = list(deduplicate(sequence)) if sequence or []
        # self.data = list(deduplicate(sequence or []))


def deduplicate(sequence, keys=None, values=None):
    keys = keys or []
    values = values or []
    update = partial(_update, keys, values)
    append = partial(_append, keys, values)

    for key, value in sequence:
        if key in keys:
            update(key, value)
        else:
            append(key, value)
        # update(key, value) if key in keys else append(key, value)

    return zip(keys, values)


def _append(keys, values, key, value):
    keys.append(key)
    values.append(value)


def _update(keys, values, key, value):
    index = keys.index(key)
    values[index] = value
