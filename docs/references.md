# API References

All about concise API references manual for `pure-datastructures`, with the detail about classes, function, return types or arguments.

### *`procedure_search_obj(**kwargs)`*

- Search any value / elements through Stack, List and Queue. return `False` if there's a value otherwise return `True`.
- Throwing `missing {} required positional arguments` if not set the value.

### *`procedure_push(**kwargs)`*

- Set a value through List and Queue, like a basic insertion or appending a value. For `OrderedList()`, new value didn't stored in `temporary` variables, likewise, for `UnorderedList()` new value would be stored in `temporary` variables (since `UnorderedList()` is using **0(n)** for append a value).

### *`procedure_pop(**kwargs)`*

- Same function like `procedure_push()`, the different this will raise an `IndexError` if stack is empty or has no value. Only work in Stack references.

### *`procedure_expand_size()`*

- Expanding or double length of array (formula: array + `None` * size of array) . Work in all data structures references. Automatically return `None` if an array doesn't have a value.

### *`procedure_peek()`*

- Check the top-most of any elements in array.

### *`is_empty()`*

- Check whether an array does have a value or not. In Stack case, will return `False` if stack is empty and return `True` if not empty, for List and Queue, will not return any value except `None`.

### *`procedure_enqueue(**kwargs)`*

- Push new object or value to queue.

### *`procedure_dequeue()`*

- Remove first object or value from queue.