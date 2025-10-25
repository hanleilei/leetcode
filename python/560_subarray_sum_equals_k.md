# subarray sum equals k

[[prefixSum]]

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 10 ** 4
-1000 <= nums[i] <= 1000
-10 ** 7 <= k <= 10 ** 7


利用字典cnt统计前N项和出现的个数:

    遍历数组nums：
    在cnt中将sums的计数+1
    累加前N项和为sums
    将cnt[sums - k]累加至答案

其实我们大可以把 cur 作为我们字典中的key，然后value设置成为 cur 出现次数，我们在迭代的时候，只需要查找 cur - target在不在字典里面，在的话，返回值增值即可，思路和two sum完全一样。这里我们字典里之所以存储出现次数，是为了解决出现重复数字的问题


```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, cur, res = {0: 1}, 0, 0
        for v in nums:
            cur += v
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res
```

经典的前缀和问题

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 1 if nums[0] == k else 0
        
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(1, n+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]

        seen = defaultdict(int)
        res = 0
        for s in pre_sum:
            res += seen[s - k] #关键
            seen[s] += 1
        return res
```
