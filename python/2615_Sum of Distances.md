# Sum of Distances

You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

Example 1:

Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation:
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5.
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3.
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4.
When i = 4, arr[4] = 0 because there is no other index with value 2.

Example 2:

Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9

先将相同值的索引分组，然后对于每个分组，计算每个索引与其他索引的距离之和。可以使用前缀和来优化计算。

```python
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)

        for a in d.values():
            n = len(a)
            s = sum(x - a[0] for x in a)
            res[a[0]] = s
            for i in range(1, n):
                s += (i * 2 - n) * (a[i] - a[i-1])
                res[a[i]] = s
        return res
```

使用前缀和来计算距离之和：

```python
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)

        for a in d.values():
            n = len(a)
            s = list(accumulate(a, initial=0))
            for j, target in enumerate(a):
                left = target * j - s[j]
                right = s[n] - s[j]- target * (n - j)
                res[target] = left + right
        return res
```
