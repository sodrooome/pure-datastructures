# Drawbacks

Since this package is alpha/beta development, currently there's a major drawback if using several data structures API.

## Performance is not measured

The biggest changing are performance is not coverage enough for production release. Since, this package is currently on alpha/beta development, any performance is not measured enough (or you can benchmark yourself using `cProfile`). Even though, i'm pretty confident this scenarios are using Big-O-Notation references (has a average - worst scenario for time complexity).

## Immutable data structures

Limiting size only, you can't change the default data-types, length of some arrays or any value if want to declare it, in your existing code. I have set a `maxsize` for each data structures params, this also has a valid reason to limit the space of API itself, since python is dynamic programming and as if it shows a static array. Limit size is 10.

## Non-recursive for searching

Being developed, the idea of ​​using recursive on every data structure allows to store all values ​​in a function and not delete those values ​​if we do a `pop`.