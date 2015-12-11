## Contains duplicate
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct

#### 就是看数组中是否有重复的参数，直接用集合的概念搞定

```python
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
```
