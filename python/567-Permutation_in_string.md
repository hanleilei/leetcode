# permutation in string

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



# Example 1:
```
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
```
# Example 2:
```
Input:s1= "ab" s2 = "eidboaoo"
Output: False
```

# Note:
```
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
