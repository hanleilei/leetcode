# 132 Pattern

[[stack]]

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

## Example 1

```text
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
```

## Example 2

```text
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
```

## Example 3

```text
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
```

## Constraints

```text
n == nums.length
1 <= n <= 2 * 105
-109 <= nums[i] <= 109
```

这个O(N)的方法，就是正确答案：

```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        flag = float('-inf')
        stack = list()
        for i in nums[::-1]:
            if i < flag:
                return True
            while stack and stack[-1] < i:
                flag = stack.pop()
            stack.append(i)
        return False
```
