# Tuple with Same Product

[[hashtable]]

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.

```python
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        freq = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                key = nums[i] * nums[j]
                res += freq[key]
                freq[key] += 1
        return res * 8
```

假设存在 n 组数，对于其中任意两组数 a,b 和 c,d，均满足 `a * b = c * d` 的条件，则这样的组合一共有 `n * (n - 1) / 2` 个。

根据题意每一组满足上述条件的组合可以构成 8 个满足题意的元组，故将各个相同乘积的组合数乘以 8 相加（等价于：左移 3 位）即可得到结果。

```python
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for i in range(1, len(nums)):
            for j in range(i):
                x = nums[i] * nums[j]
                cnt[x] += 1
        return sum(v * (v - 1) // 2 for v in cnt.values()) << 3
```
