# Smallest All-Ones Multiple

You are given a positive integer k.

Find the smallest integer n divisible by k that consists of only the digit 1 in its decimal representation (e.g., 1, 11, 111, ...).

Return an integer denoting the number of digits in the decimal representation of n. If no such n exists, return -1.

 

Example 1:

Input: k = 3

Output: 3

Explanation:

n = 111 because 111 is divisible by 3, but 1 and 11 are not. The length of n = 111 is 3.

Example 2:

Input: k = 7

Output: 6

Explanation:

n = 111111. The length of n = 111111 is 6.

Example 3:

Input: k = 2

Output: -1

Explanation:

There does not exist a valid n that is a multiple of 2.

 

Constraints:

2 <= k <= 10^5

1. 如果 k 包含因子 2 或 5，则不可能有全1的数能被 k 整除，因为全1的数都是奇数且末尾不是0或5。
2. 使用取模运算来避免处理过大的数字。我们可以通过不断构造全1的数的取模值，直到找到一个取模值为0的情况，或者发现循环（即出现重复的取模值）。
3. 最多尝试 k 次，因为根据鸽巢原理，取模值最多有 k 种可能（0 到 k-1）。如果在 k 次尝试内没有找到取模值为0的情况，说明不存在这样的全1数。

```python
class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        base = 0
        res = 0

        for _ in range(10**5):
            base = (base * 10 + 1) % k
            res += 1
            if base == 0:
                return res
        return -1
```

1. 使用集合记录已经出现过的取模值，避免重复计算。
2. 每次计算新的全1数的取模值时，检查是否已经出现过该取模值。如果出现过，说明进入了循环，不可能找到取模值为0的情况。
3. 如果找到取模值为0，则返回当前全1数的长度。

```python
class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        seen = set()
        x = 1
        while x and x not in seen:
            seen.add(x)
            x = (x * 10 + 1) % k
        return -1 if x else len(seen) + 1
```
