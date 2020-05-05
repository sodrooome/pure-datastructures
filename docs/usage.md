# Quick sample

A quick introduction using `pure-datastructures`. Using `OrderedList()` references and integers input-type :

```python
import ds

scenario = ds.OrderedList()

# basic insertion
scenario.add(70)
scenario.add(13)
scenario.add(-3)

# calculate size of array with `size()`
# return length of array
print(scenario.size())

# searching value through array with `search_obj()`
# return False if value is not founds
print(scenario.search_obj(5))
```

Another example using basic `Stack()`, and string as input-type :

```python
import ds

scenario = ds.Stack()

# basic insertion
scenario.procedure_push('json')

# the function same as the above
# return length of array
print(scenario.procedure_size())

# check the top-most element of stack
# return value of element
print(scenario.procedure_peek())
```