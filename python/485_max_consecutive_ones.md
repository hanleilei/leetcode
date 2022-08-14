# max consecutive ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

#### 照旧一个计数器就可以

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
