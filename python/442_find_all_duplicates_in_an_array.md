# Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

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
