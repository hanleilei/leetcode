# max consecutive ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

照旧一个计数器就可以

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        m = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                counter = 0
            m = max(m, counter)
        return m
```

再来一个单行的版本：

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max([len(i) for i in bytearray(nums).split(b'\x00')])
```

拆开来就是这样：

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = ''.join([str(i) for i in nums]).split("0")
        return len(max(n, key=len))
```

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(max(''.join([str(i) for i in nums]).split('0'), key=len))
```

再来一个快一点的：

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                res = max(count, res)
                count = 0
        return max(res, count)
```
