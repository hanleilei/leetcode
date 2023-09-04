# Minimum Replacements to Sort the Array

You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.

Example 1:

```text
Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.
```

Example 2:

```text
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0. 
```

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109

```python
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[-1]
        res = 0

        for i in range(n - 2, -1, -1):
            noOfTime = nums[i] // prev
            if nums[i]% prev != 0:
                noOfTime += 1
                prev = nums[i] // noOfTime
            res += noOfTime - 1
        return res
```

再来一个 Lee215的简洁写法：

Explanation
Reversely iterate the array A.
x is the current upper bound.
init x with a big enough value.

For element A[i],
If A[i] % x == 0,
then we can divide A[i] all into x with count k = A[i] / x.
with k - 1 operations,
the upper bound is still x
(// means integer division)

If A[i] % x > 0,
then we can divide A[i] all into x with count k = A[i] / x + 1.
with k - 1 operations,
the upper bound is A[i] / k.
(// means integer division)

```python
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = nums[-1]
        res = 0

        for a in reversed(nums):
            k = (a + prev - 1) //  prev
            prev = a // k
            res += k - 1
        return res
```
