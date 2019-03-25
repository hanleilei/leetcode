# random pick with blacklist

Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

### Note:

1. 1 <= N <= 1000000000
2. 0 <= B.length < min(100000, N)
3. [0, N) does NOT include N. See interval notation.

### Example 1:
```
Input:
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]
```
### Example 2:
```
Input:
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]
```
### Example 3:
```
Input:
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
```
### Example 4:
```
Input:
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
```
### Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

```python
import random
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        blacklist = sorted(blacklist)
        self.b = set(blacklist)
        self.m = {}
        self.length = N - len(blacklist)
        j = 0
        for i in range(self.length, N):
            if i not in self.b:
                self.m[blacklist[j]] = i
                j += 1

    def pick(self) -> int:
        i = random.randint(0, self.length - 1)
        return self.m[i] if i in self.m else i

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
```
再来一个速度快的：

```python
import random
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.b = set(blacklist)
        self.n = N
        self.curr = 0
        self.used = set()

    def pick(self) -> 'int':
        while self.curr in self.b:
            self.curr += 1
        if self.curr >= self.n:
            res = self.used.pop()
        else:
            res = self.curr
            self.curr += 1
        self.used.add(res)
        return res
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()

```
