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
