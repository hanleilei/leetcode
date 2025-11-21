# jump game

[[Micorsoft]]

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

注意 max 的哪一行语句用到的贪心算法, 即：**每一次遍历都取前面所有遍历元素所能到达最远位置的最大值，如果该最大值大于或等于给定数组 nums 的长度，则说明游戏成功，反之则失败。** 这一题其实是要比之前的跳跃游戏 II 要简单许多，因为你不要求出具体的跳跃步骤，只需要给出答案即可，这一题的难点就是对于 0 元素的处理，因为出现了 0 说明这一步是不跳的，那么 0 出现在哪个位置就要好好考虑了。

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

再来一个单行的 python2 版本：

```python
class Solution:
    def canJump(self, nums):
        return reduce(lambda m, (i, n): max(m, i+n) * (i <= m), enumerate(nums, 1), 1) > 0
```

We start travering the array from start
While traversing, we keep a track on maximum reachable index and update it accordingly. If we reach the maxium reachable index we get out of loop.
At last, if maxium reachable index is greater than or equal to last index of the array, means we can reach the last element else return false.

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableIndex = 0
        for curr in range(len(nums)):
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr]
            if curr == reachableIndex:
                break

        return reachableIndex >= len(nums) - 1
```

或者：

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        rightmost=0
        for i in range(n):
            if i <= rightmost:
                rightmost=max(rightmost,i+nums[i])
                if rightmost>=n-1:
                    return True
        return False
```

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxPos = 0;
        for (int i = 0; i < nums.size(); i++){
            if (i > maxPos) return false;
            maxPos = max(i + nums[i], maxPos);
        }
        return true;
    }
};
```

