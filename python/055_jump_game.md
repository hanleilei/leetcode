# jump game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

注意max的哪一行语句用到的贪心算法, 即：**每一次遍历都取前面所有遍历元素所能到达最远位置的最大值，如果该最大值大于或等于给定数组nums的长度，则说明游戏成功，反之则失败。** 这一题其实是要比之前的跳跃游戏II要简单许多，因为你不要求出具体的跳跃步骤，只需要给出答案即可，这一题的难点就是对于0元素的处理，因为出现了0说明这一步是不跳的，那么0出现在哪个位置就要好好考虑了。



```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
```
再来一个做减法的思路：
```python
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mingood = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= mingood:
                mingood = i

        return mingood == 0
```
