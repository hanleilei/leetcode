# find all numbers disappeared in an array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

## 理解题目，从 1 到数组长度范围内，然后用集合解决。

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        min_num = 1
        max_num = len(nums)
        return list(set([n for n in range(1, len(nums)+1)]) - set(nums))
```

遍历数组的方式解决：

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]
```
