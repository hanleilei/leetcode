# missing positive

[[math]]

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

还是用哪个经典的替换方法来实现。简单，但是好慢。。

```python
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [i for i in nums if i > 0]
        if nums == []:
            return 1

        a = [0] * (max(nums)+2)
        for i in nums:
            a[i-1] = i
        for i in range(len(a)):
            if a[i] == 0:
                return i+1
```

现在上面的方法，不能ac了，加了一个测试用例：[2**32-1]

再来一个讨论群用 cpp 写，点赞最多的：

```python
class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        for i in range(len(nums)):
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1 # key point
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
```

再来一个速度不但快，而且是最简单的：

```python
class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        n=1
        nums = set(nums)
        while n in nums:
            n=n+1
        return n
```

感觉自己的智商被碾压了。。

或者：

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        c = 1
        while s:
            if c not in s:
                return c
            c += 1
```

如果观察要求，O(n) 时间和 O(1) 空间，说明不能使用额外的空间来存储数据结构，所以只能在原数组上进行操作。我们可以将每个正整数放到它应该在的位置上，例如将数字 1 放到索引 0 的位置，数字 2 放到索引 1 的位置，以此类推。这样做之后，我们再遍历一次数组，找到第一个位置 i 上的数字不等于 i+1 的情况，那么 i+1 就是缺失的最小正整数。如果所有位置都正确，那么缺失的最小正整数就是 n+1。

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
```
