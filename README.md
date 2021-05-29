# Pure Data Structures

![Build](https://github.com/sodrooome/pure-datastructures/workflows/Build/badge.svg) ![Downloads](https://pepy.tech/badge/pure-datastructures) ![PyPI - Status](https://img.shields.io/pypi/status/pure-datastructures) ![PyPI](https://img.shields.io/pypi/v/pure-datastructures)

Data structures package for python, written in pure python code, not dependent on any other libraries or built-in function.

## List of Data Structures

- Stack
- Stack + Linked List
- Queue
- List
- List + Ordered List

## Installation

You can install this package with command :

`pip install pure-datastructures`

## Usage

A quick introduction using `pure-datastructures`. Using `OrderedList()` built-in method :

```python
import ds

scenario = ds.OrderedList()

# basic insertion
scenario.procedure_push(70)
scenario.procedure_push(13)
scenario.procedure_push(-3)

# calculate size of array with `size()`
# return length of array
print(scenario.procedure_expand_size())

# searching value through array with `search_obj()`
# return False if value is not founds
print(scenario.procedure_search_obj(5))
```

## Documentation

For documentation read in [pure-datastructures](https://sodrooome.github.io/pure-datastructures/).

