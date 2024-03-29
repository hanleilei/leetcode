# set mismatch

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

一个很巧妙的方式找到两个元素的位置：

```python
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        count = [0] * (size+1)
        for i in nums:
            count[i] += 1

        for i in range(1, size + 1):
            if count[i]== 2:
                twice = i
            if count[i] == 0:
                never = i
        return twice, never
```

还是看看 stefan 大大的方法：

```python
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]
```

现在 2023-10-25， 我也能直接撸出来上面的方法了。

再来一个官方的方法，从 Java 翻译过来：

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        dup = -1
        missing = 1
        for i in nums:
            if nums[abs(i) - 1] < 0:
                dup = abs(i)
            else:
                nums[abs(i) - 1] *= -1
        for j in range(len(nums)):
            if nums[j] > 0:
                missing = j + 1
        return [dup, missing]
```

讲真，这个题目蛮蠢的，还是 stefan 的方法最好，直截了当的击中要害。

现在理解题目的意思，直接上，发现也能搞出来 stefan 的方法了。。

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]
```
