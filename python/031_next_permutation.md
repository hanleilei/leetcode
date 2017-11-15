# next permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

思路和cpp的版本不是非常的一致：
1. 两两相比，找到最后一个递增的子序列，返回左边的位置k
2. 如果是递减的序列，则直接求逆序
3. 从k的下一个元素开始，遍历，找到最后一个大于位置k的值，位置为l
4. 交换位置k和位置l的值。
5. 对于位置k之后的值求逆序。

```python
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                k = i

        if k == -1:
            nums.reverse()
            return

        for i in range(k + 1, len(nums)):
            if nums[i] > nums[k]:
                l = i

        nums[k], nums[l] = nums[l], nums[k]
        nums[k + 1:] = nums[:k:-1]
```
