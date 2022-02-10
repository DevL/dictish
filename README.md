# Dictish

[![Python package](https://github.com/DevL/dictish/actions/workflows/python-package.yml/badge.svg)](https://github.com/DevL/dictish/actions/workflows/python-package.yml)

Lecture material for implementing a dict-like object in Python.

## Steps

* `Creating`
* `__bool__`
* `__getitem__`
* `__iter__`
* `get`
* `items`
* `keys`
* `values`
* `pop`


## dict dump

https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

`>>> sorted(dir(dict()))

- [ ] `__class__`
- [x] `__contains__`
- [ ] `__delattr__`
- [ ] `__delitem__`
- [ ] `__dir__`
- [ ] `__doc__`
- [x] `__eq__`
- [ ] `__format__`
- [ ] `__ge__`
- [ ] `__getattribute__`
- [x] `__getitem__`
- [ ] `__gt__`
- [ ] `__hash__`
- [x] `__init__`
- [ ] `__init_subclass__`
- [x] `__iter__`
- [ ] `__le__`
- [x] `__len__`
- [ ] `__lt__`
- [ ] `__ne__`
- [ ] `__new__`
- [ ] `__reduce__`
- [ ] `__reduce_ex__`
- [x] `__repr__`
- [x] `__reversed__`
- [ ] `__setattr__`
- [ ] `__setitem__`
- [ ] `__sizeof__`
- [x] `__str__`
- [ ] `__subclasshook__`
- [ ] `clear`
- [ ] `copy`
- [ ] `fromkeys`
- [x] `get`
- [x] `items`
- [x] `keys`
- [ ] `pop`
- [ ] `popitem`
- [ ] `setdefault`
- [ ] `update`
- [x] `values`



## Truthiness

By default, an object is considered true unless its class defines either a __bool__() method
that returns False or a __len__() method that returns zero, when called with the object.


## Implementing merging by supporting +

__add__`

## Missing key handling

https://docs.python.org/3/library/collections.html#defaultdict-objects

`__missing__`


## Implementing missing 3.9 functionality


d | other

    Create a new dictionary with the merged keys and values of d and other, which must both be dictionaries. The values of other take priority when d and other share keys.

d |= other

    Update the dictionary d with keys and values from other, which may be either a mapping or an iterable of key/value pairs. The values of other take priority when d and other share keys.

## View Objects and simplifications

https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects


## Using an Abstract Base Class

https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes

1. Creating an empty Dictish
    1. Truth
    2.
2.
3.
4.
5.
