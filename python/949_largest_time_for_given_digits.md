# largest time for given digits

Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59. Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5. If no valid time can be made, return an empty string.

Example 1:

```
Input: [1,2,3,4]
Output: "23:41"
```

Example 2:

```
Input: [5,5,5,5]
Output: ""
```

Note:

```
A.length == 4
0 <= A[i] <= 9
```

排列组合，数组里面的四个数字要组成两个数，一个是 01 到 24 之间:

```Python
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        return max(["%d%d:%d%d" % t for t in itertools.permutations(A) if t[:2] < (2, 4) and t[2] < 6] or [""])
```

也是 lee215 的方案，绝大多数都是使用 permutations 这个方法实现。。
