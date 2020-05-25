## API References

All about concise API references manual for `pure-datastructures`, with the detail about classes, function, return types, arguments and throwing exception.

### `procedure_search_obj(**kwargs)`

- Search any value / elements through List. return `False` if there's a value otherwise return `True`.
- Throwing `missing {} required positional arguments` if not set the value.

### `procedure_push(**kwargs)`

- Set a value through `List` and `Queue`, like a basic insertion or appending a value. For `OrderedList()`, new value didn't stored in `temporary` variables, likewise, for `UnorderedList()` new value would be stored in `temporary` variables (since `UnorderedList()` is using **0(n)** for append a value).

### `procedure_pop()`

- Same function like `procedure_push()`, the different this will raise an `IndexError` if stack is empty or has no value. Only work in Stack references.

### `procedure_expand_size()`

- Expanding or double length of array (formula: array + `None` * size of array) . Work in all data structures references. Automatically return `None` if an array doesn't have a value.

### `procedure_peek()`

- Check the top-most of any elements in array.

### `procedure_enqueue(**kwargs)`

- Push new object or value to queue.

### `procedure_dequeue()`

- Remove first object or value from queue.
- Raise an `IndexError` if you have not set a value before popped out. As a for concern, `dequeue` process in basic `Queue` and `CircularQueue` is different.

### `is_empty()`

- Check whether an array does have a value or not. In `Stack` and `Queue` case, will return `False` if stack/queue is empty and return `True` if not empty.
- For `List`, will not return any value except `None`.

### `is_full()`

- Check whether an array does have a value or not. Only available in `Stack` and `Queue`, throwing exceptions work out same as like `is_empty()`.

### `is_balanced()`

- Check if an array does have a same balanced through inputted value, available in `Stack` and `Queue` only. Inputted value only works with parenthesis like.

### `DsIndexError()`

- Throwing exception, one of the basic and common error in this package. This will raise if inputted value is attempt to access the outside that index of list. Error message :

    ```sh
    Stack / List / Queue is empty, set a value first.
    ```

### `DsPeekIndexError()`

- Throwing exception, the difference with `DsIndexError()`, it will raise if `procedure_peek()` process didn't find any value from that index of list. Error message :

    ```sh
    Stack / List / Queue is empty, you either must be popped or not set a value.
    ```

### `DsValueError()`

- Throwing exception, that indicates the data-type or value is not correct. Error message :

    ```sh
    Value error, either your argument or inputted value is not correct.
    ```