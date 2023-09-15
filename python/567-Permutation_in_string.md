# permutation in string

[[sliding window]]

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

## Example 1

```text
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
```

## Example 2

```text
Input:s1= "ab" s2 = "eidboaoo"
Output: False
```

## Note

```text
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
```

完全遵照题目意思，建立两个字典，或者Python中内建的 Counter，然后比较结果。

```Python
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1, d2 = Counter(s1), Counter(s2[:len(s1)])
        for start in range(len(s1), len(s2)):
            if d1 == d2: return True
            d2[s2[start]] += 1
            d2[s2[start-len(s1)]] -= 1
            if d2[s2[start-len(s1)]] == 0:
                del d2[s2[start-len(s1)]]
        return d1 == d2
```

再来一个类似的写法，先将转换成字典。

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False
```

再看看labuladong的模板方法：

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        windows, need = defaultdict(int), Counter(s1)
        valid = 0
        start = 0
        size = len(s1)

        while right < len(s2):
            c = s2[right]
            right += 1

            if c in need:
                windows[c] += 1
                if windows[c] == need[c]: #通过这种方法判断字典元素相同，则valid加一
                    valid += 1
            
            while valid == len(need):  # 如果此时valid和need是想等的，则两个字典就相等
                if right - left == size:
                    return True
                
                d = s2[left]
                left += 1
                if d in need:
                    if windows[d] == need[d]:
                        valid -= 1
                    windows[d] -= 1
        return False
```

