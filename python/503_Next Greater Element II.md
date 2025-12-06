# Next Greater Element II

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

Constraints:

1 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9

单调栈

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n  # 初始化结果数组，默认值为 -1
        stack = []  # 单调栈，存储元素索引  
        # 遍历两遍数组，模拟环形
        for i in range(2 * n):
            num = nums[i % n]  # 使用取模运算实现环形访问
            # 当栈不为空且当前元素大于栈顶元素时，更新结果
            while stack and nums[stack[-1]] < num:
                index = stack.pop()
                res[index] = num
            # 只在第一次遍历时将索引入栈
            if i < n:
                stack.append(i)
        return res
```

## 复杂度分析

- 时间复杂度：O(n)，其中 n 是数组的长度。每个元素最多入栈和出栈各一次。
- 空间复杂度：O(n)，用于存储栈和结果数组。
- 算法思路：
  1. 使用单调栈存储元素索引，栈内元素对应的值保持递减。
  2. 遍历数组两次，模拟环形数组的效果。
  3. 当遇到比栈顶元素大的元素时，弹出栈顶元素并更新其下一个更大元素。
  4. 最终返回结果数组。
  5. 如果某个元素没有找到下一个更大元素，结果数组中对应位置仍为 -1。
  6. 通过取模运算实现环形访问，确保每个元素都能找到下一个更大元素（如果存在）。
  7. 只在第一次遍历时将索引入栈，避免重复处理。
  8. 最终返回结果数组。

再来一个反向的：

```python
        n = len(nums)
        res = [-1] * n 
        stack = list()
        for i in range(n*2 - 1, -1, -1):
            x = nums[i % n]
            while stack and x >= stack[-1]:
                stack.pop()
            if stack and i < n:
                res[i] = stack[-1]
            stack.append(x)

        return res
```
