# Find the difference

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

### 这个算是抖了个机灵，完全利用了collections库里面的Counter函数。

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = Counter(t) - Counter(s)
        return list(d.keys())[0]
```

再来一个：

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)
```
换个思路，既然两个字符串就差一个字母，也就把他们合并起来分别求异或。还可以更简单：

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(ord(i) for i in t)-sum(ord(i) for i in s))
```

在来一个求字典差异的方法，很不错：

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = collections.Counter(s), collections.Counter(t)
        return (set(s.items()) ^ set(t.items())).pop()[0]
```
或者：

```python
from collections import Counter


class Solution(object):
    def findTheDifference(self, s, t):
        return (Counter(t) - Counter(s)).popitem()[0]
```

顺着这个思路：

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = collections.Counter(s+t)
        for k, v in d.items():
            if v % 2 == 1:
                return k
```
