# API References

All about concise API references manual for `pure-datastructures`, with the detail about classes, function, return types or arguments.

### `procedure_search_obj(**kwargs)`

- Search any value / elements through List. return `False` if there's a value otherwise return `True`.
- Throwing `missing {} required positional arguments` if not set the value.
- References :

```python
def procedure_search_obj(self, item):
    """Searching value through list."""
    current = self.head
    found = False
    stop = False

    while current != None and not found and not stop:
        if current.getData() == item:
            found = True
        else:
            if current.getData() > item:
                stop = True
            else:
                current = current.getNext()
    return found
```

### `procedure_push(**kwargs)`

- Set a value through List and Queue, like a basic insertion or appending a value. For `OrderedList()`, new value didn't stored in `temporary` variables, likewise, for `UnorderedList()` new value would be stored in `temporary` variables (since `UnorderedList()` is using **0(n)** for append a value).
- A reference for push new value in Stack :

```python
def procedure_push(self, item):
	self.top = self.top + 1
	if self.top == len(self.array):
		self.expand_size()
	self.array[self.top] = item
```

### `procedure_pop()`

- Same function like `procedure_push()`, the different this will raise an `IndexError` if stack is empty or has no value. Only work in Stack references.
- References :

```python
def procedure_pop(self):
	if self.is_empty():
		raise IndexError("Stack is empty")
	item = self.array[self.top]
	self.top = self.top - 1
	return item
```

### `procedure_expand_size()`

- Expanding or double length of array (formula: array + `None` * size of array) . Work in all data structures references. Automatically return `None` if an array doesn't have a value.
- References doubled size in List :

```python
def procedure_expand_size(self):
    """Expand value of list."""
    current = self.head
    count = 0
    while current != None:
        count = count + 1
        current = current.getNext()
    return count
```

### `procedure_peek()`

- Check the top-most of any elements in array.
- References :

```python
def procedure_peek(self):
	"""Check the top-most element of the stack."""
	if self.is_empty():
		raise IndexError("Stack is empty")
	return self.array[self.top]
```

### `procedure_enqueue(**kwargs)`

- Push new object or value to queue.
- References :

```python
def procedure_enqueue(self, value):
	"""Enqueue maintains two pointers, rear and front."""
    if self.rear == len(self.size):
        self.procedure_expand_size()
    self.size[self.rear] = item
    self.rear = self.rear + 1
    self.value = self.value + 1
```

### `procedure_dequeue()`

- Remove first object or value from queue.
- Raise an `IndexError` if you have not set a value before popped out.
- References in CircularQueue, (for noted, `dequeue` process in basic Queue and CircularQueue is different) :

```python
def procedure_dequeue(self):
    if self.is_empty():
        raise IndexError("Queue is empty, set a value first.")
    value = self.front.value
    if self.front is self.rear:
        self.front = None
        self.rear = None
    else:
        self.front = self.front.next
    self.size = self.size - 1
    return value
```

### `is_empty()`

- Check whether an array does have a value or not. In Stack and Queue case, will return `False` if stack/queue is empty and return `True` if not empty.
- For List, will not return any value except `None`.
- References :

```python
def is_empty(self):
    if self.top < 1:
        return True
    else:
        return False
```

### `is_full()`

- Check whether an array does have a value or not. Only available in Stack and Queue, throwing exceptions work out same as like `is_empty()`.
- References `is_full()` in Queue :

```python
def is_full(self):
    if self.rear == len(self.size) - 1:
        return True
    else:
        return False
```
