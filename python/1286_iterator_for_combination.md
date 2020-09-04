# iterator of combination

Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.


Example:
```java
CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 ```

Constraints:
```
1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
```

简单，直接上itertools：

```Python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        from itertools import combinations
        self.iter = combinations(characters, combinationLength)
        self.res = list()


    def next(self) -> str:
        if len(self.res) == 0:
            return ''.join(next(self.iter))
        else:
            return ''.join(self.res.pop())


    def hasNext(self) -> bool:
        try:
            self.res.insert(0, next(self.iter))
            return True
        except:
            return len(self.res) > 0
```

或者来一个更加简洁的：

```Python
class CombinationIterator:

    def __init__(self, c: str, combinationLength: int):
        self.combs = list(map(''.join, itertools.combinations(c, combinationLength)))[::-1]

    def next(self) -> str:
        return self.combs.pop(-1)

    def hasNext(self) -> bool:
        return bool(self.combs)
```
