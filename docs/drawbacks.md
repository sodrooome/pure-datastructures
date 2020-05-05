# Drawbacks

Since this package is alpha/beta development, currently there's a major drawback if using several data structures API.

## Performance is not measured

The biggest changing are performance is not coverage enough for production release. Since, this package is currently on alpha/beta development, any performance is not measured enough (or you can benchmark yourself using `cProfile`). Even though, i'm pretty confident this scenarios are using Big-O-Notation references (has a average - worst scenario for time complexity).

## Limited input size

Limiting size only, you can change the default data-types, but you can't initialize length of some arrays or any value, in your existing code. I have set a `maxsize` for each data structures params, this also has a valid reason to limit the space of API itself, since python is dynamic programming and as if it shows a static array. Limit size is 10.

## Non-recursive for searching

Being developed, the idea of ​​using recursive on every data structure allows to store all values ​​in a function and not delete those values ​​if we do a `pop`.

## Handling exception

Unfortunately, for throwing exceptions are not yet fully available (and still being developed). If you have any error if perform or when executing the code, the default error that appears is the default exception from python. Although there are some events that bringing up an raise `IndexError` if the stack is empty.