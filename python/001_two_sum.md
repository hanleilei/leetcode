# Two Sum

[[hashtable]]

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

```text
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
```

O(n) runtime, O(n) space – Hash table:

We could reduce the runtime complexity of looking up a value to O(1) using a hash map that maps a value to its index

use hash table is default solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            d[target - n] = i
```

this will execute in less than 60 ms
