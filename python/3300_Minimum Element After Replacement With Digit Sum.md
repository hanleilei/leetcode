# Minimum Element After Replacement With Digit Sum

You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

Example 1:

Input: nums = [10,12,13,14]

Output: 1

Explanation:

nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

Example 2:

Input: nums = [1,2,3,4]

Output: 1

Explanation:

nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

Example 3:

Input: nums = [999,19,199]

Output: 10

Explanation:

nums becomes [27, 10, 19] after all replacements, with minimum element 10.

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 10^4

```python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sum_all(n: int) -> int:
            res = 0
            while n > 0:
                n, b = divmod(n, 10)
                res += b
            return res + n
        return min([sum_all(i) for i in nums])
```

```python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = inf
        for n in nums:
            digit = 0
            while n > 0:
                digit += n % 10
                n  //= 10
            if digit < res:
                res = digit
        return res
```
