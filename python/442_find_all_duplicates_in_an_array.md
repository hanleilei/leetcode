# Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.

很简单，一个集合，一个列表。。

```python
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        res = list()
        for i in nums:
            if i in s:
                res.append(i)
            else:
                s.add(i)
        return res
```

换个思路：

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set(nums)
        res = list()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                res.append(i)
        return res
```

再来一个：

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        return [k for k, v in d.items() if v == 2]
```
