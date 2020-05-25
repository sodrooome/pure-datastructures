# Release history

Using semantic versioning and based on PEP 440 (version identification and dependency specification). All of release history (binary / numbers only) can be found in [PyPi changelog](https://pypi.org/project/pure-datastructures/)

## Changelog

### Pure-datastructures 0.1.4 (2020-25-05)
Highlights :

- Adding `benchmark` decorators for measure code performance
- Adding `DoubleLinkedList`
- Adding custom exception for `List`
- Fixed inserting new object in `Stack`, `Queue`, `CircularQueue` and `List`

Issues :

- Inserting new object in `PriorityQueue` not working
- Inserting new object in `OrderedStack` will return empty list, this shouldn't be have an object or list

### Pure-datastructures 0.1.3 (2020-14-05)
Highlights :

- Adding custom exception for Queue and Stack

### Pure-datastructures 0.1.2 (2020-10-05)
Highlights :

- Dropped support for python 2.7 or below
- Adding `is_balanced()` in `Stack` and `Queue`
- Providing delete node on `List` using `procedure_delete_node()`

### Pure-datastructures 0.1.1 (2020-07-05)
Highlights :

- Fixed `is_empty()` only return `False`
- Fixed `unittest` not discover of all test
- Adding `is_full()` in `Stack` and `Queue`
- Adding `CircularQueue()`
- Adding `IndexError` in `Queue`
- Depth coverage about throwing exceptions in `Queue` and `Stack`


### Pure-datastructures 0.1.0 (2020-05-05)
Highlights :

- Fixed iteration in `LinkedList`
- Reorganize all data structures
- Adding `UnorderedList`
- `size()` functions are changing into `expand_size()`

### Pure-datastructures 0.0.8 (2020-04-05)
Highlights :

- Adding `search_obj()` for `List`.
- Adding basic queueing (perform `enqueue`, `dequeue` and `is_empty`)

### Pure-datastructures 0.0.5 (2020-04-05)
Highlights :

- Remove mock test in every references

### Pure-datastructures 0.0.1 (2020-04-05)
- Pre-release for pure-datastructures
