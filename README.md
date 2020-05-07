# Pure Data Structures

Data structures package for python, written in pure python code, not dependent on any other libraries or built-in function. Any performance is not measured enough (or you can benchmark yourself using `cProfile`). Even though, i'm pretty confident this scenarios are using Big-O-Notation references (average - worst scenario for time complexity).

## List of Data Structures

- Stack
- Stack + Linked List
- Queue
- List
- List + Ordered List

## Installation

For python 2.7 :

`pip install pure-datastructures`

For python 3.6 or higher :

`pip3 install pure-datastructures`

If you facing a trouble while perform installation, make sure :

- You already activated virtual environment (**Recommended**)
- Using root access (**Not Recommended**)
- Or, using verbosity flag `--user`

## Usage

Quick example using Ordered List :

```python
import ds

scenario = ds.OrderedList()

# basic insertion
scenario.add(70)
scenario.add(13)
scenario.add(-3)

# calculate size of array with `size()`
print(scenario.size())

# searching value through array with `search_obj()`
print(scenario.search_obj(5))
```

## Documentation

For documentation read in [pure-datastructures doc](https://sodrooome.github.io/pure-datastructures/)

