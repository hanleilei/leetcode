# subarray sum equals k

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

利用字典cnt统计前N项和出现的个数:

    遍历数组nums：
    在cnt中将sums的计数+1
    累加前N项和为sums
    将cnt[sums - k]累加至答案

想到这种解法，对于目前的我而言（Nov 2017），有点难度，需要把这类问题再理一下。


```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        ans = sums = 0
        cnt = collections.Counter()
        for num in nums:
            cnt[sums] += 1
            sums += num
            ans += cnt[sums - k]
        return ans
```
