# Count Nice Pairs in an Array

You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

## Example 1

```text
Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
```

## Example 2

```text
Input: nums = [13,10,35,24,76]
Output: 4
```

## Constraints

```text
1 <= nums.length <= 105
0 <= nums[i] <= 109
```

方法很简单，换个思路：

```text
A[i] + rev(A[j]) == A[j] + rev(A[i])
A[i] - rev(A[i]) == A[j] - rev(A[j])
B[i] = A[i] - rev(A[i])
```

Then it becomes an easy question that,
how many pairs in B with B[i] == B[j]

```python
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res = 0
        d = defaultdict(int)
        for i in nums:
            j = int(str(i)[::-1])
            d[i-j]+= 1
        for a in d.values():
            res += (a - 1) * a // 2
        return res % (10 ** 9 + 7)
```
