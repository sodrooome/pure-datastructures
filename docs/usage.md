# Quick sample

A quick introduction using `pure-datastructures`. Using `OrderedList()` references and integers input-type :

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

Another example using basic `Stack()`, and string as input-type :

```python
import ds

scenario = ds.Stack()

# basic insertion
scenario.procedure_push('json')

# the function same as the above
# return length of array
print(scenario.procedure_expand_size())

# check the top-most element of stack
# return value of element
print(scenario.procedure_peek())
```

Or you can iterate Stack, to push a new value using for-loop. This is also applies to all data structures :

```python
import ds

scenario = ds.Stack()

# iterate push new value to stack
for x in range(1,4):
	scenario.procedure_push(x)

print(scenario.procedure_peek())
```

An example using Queue :

```python
import ds

scenario = ds.Queue()

# check an array
# return None if has no value
print(scenario.is_empty())

# push new value to queue
scenario.procedure_enqueue(3)
```

For more complete example will be written very soon.