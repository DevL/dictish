# Dictish

## Design Goals

* Implement a `dict`-like object without relying on `dict`.
* Implement enough of `dict`'s behaviour to make it useful.
* Avoid mutation.
* Extend the functionality beyond what's available in `dict` in Python 3.8.
  * Supporting merging two `dictish` through `or`:ing them (`d | other`).
  * Supporting appending to a `dictish` by `add`:ing to it (`d + key_value_pair`).
  * Behaving like a function (callable).
  * Supporting subset and superset comparisons of two `dictish`.

## Tutorial Steps

1. Basic, empty `dictish`.
2. Basic `dictish` with key-value pairs.
3. Iterating over keys, values, and items.
4. Supporting subscript (`d["key"]`).
5. Supporting `get` (`d.get("key")`).
6. Equality.
7. Deduplicating key-value pairs.
8. Supporting `|` and `+`.
9. Representation (`repr` and `str`).

## Going Further

10. Hello doctests!
11. Extracting a helper collection class.
12. A bit of inspiration taken from Clojure.
13. Subset and superset comparisons.


## Stretch Goals

14. A word on hashing.
15. A word on Abstract Base Classes.
