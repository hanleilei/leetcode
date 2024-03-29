# range sum query

[[prefix sum]]

Given an integer array nums, handle multiple queries of the following type:

1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

## Example 1

```text
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

## Constraints

```text
    1 <= nums.length <= 104
    -105 <= nums[i] <= 105
    0 <= left <= right < nums.length
    At most 104 calls will be made to sumRange.
```

## 思路

先保存一个数组，数组中的每个元素都是从零到当前位置的数值之和。然后在后续直接遍历这个数组，如果求一段数字，只需要做两个数组元素的差值就可以了。

```python
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.res = nums[:]
        size = len(nums)
        for i in range(1, size):
            self.res[i] = self.res[i - 1] + nums[i]


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.res[j]
        return self.res[j] - self.res[i-1]
```

提炼了一下：

```python
class NumArray:
    def __init__(self, nums: List[int]):
        self.res = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.res[i+1] = self.res[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.res[right+1] - self.res[left]
```
