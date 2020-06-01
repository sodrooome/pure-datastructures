# Pure Data Structures

![Build](https://github.com/sodrooome/pure-datastructures/workflows/Build/badge.svg) ![PyPI - Status](https://img.shields.io/pypi/status/pure-datastructures) ![PyPI](https://img.shields.io/pypi/v/pure-datastructures) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/5baa29c0e53c4897acffcc3d99e02ccb)](https://www.codacy.com/manual/sodrooome/pure-datastructures?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sodrooome/pure-datastructures&amp;utm_campaign=Badge_Grade)

Data structures package for python, written in pure python code, not dependent on any other libraries or built-in function.

## List of Data Structures

- Stack
- Stack + Linked List
- Queue
- List
- List + Ordered List

## Installation

This package only work in python 3.6 or higher :

`pip3 install pure-datastructures`

## Usage

A quick introduction using `pure-datastructures`. Using `OrderedList()` references and integer input-type :

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

