# Count Equal and Divisible Pairs in an Array

Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
 

Example 1:

Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
Example 2:

Input: nums = [1,2,3,4], k = 1
Output: 0
Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i], k <= 100

我自己手搓出来的，用的函数多了点。

```python
from operator import mul
from itertools import starmap, combinations

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)
        res = 0
        for _, v in d.items():
            if len(v) > 1:
                for j in starmap(mul, combinations(v, 2)):
                    if j % k == 0:
                        res += 1
        return res
```

deepseek 用了gcd，然后用了一个字典来记录每个gcd出现的频率。结果速度并没有我快。

```python

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)
        
        res = 0
        for indices in d.values():
            n = len(indices)
            # 统计每个gcd出现的频率
            freq = defaultdict(int)
            for i in indices:
                g = gcd(i, k)
                # 与之前记录的gcd配对
                for g_prev, cnt in freq.items():
                    if (g * g_prev) % k == 0:
                        res += cnt
                freq[g] += 1
        return res
```

```python
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)
        res = 0
        for key in d:
            indices = d[key]
            n = len(indices)
            for i in range(n):
                for j in range(i + 1, n):
                    if (indices[i] * indices[j]) % k == 0:
                        res += 1
        return res
```
