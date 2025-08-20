# Number of Zero-Filled Subarrays

[[2points]]

Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
Example 3:

Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.

Constraints:

`1 <= nums.length <= 105`
`-10**9 <= nums[i] <= 10**9`

本来是经典的双指针，后来发现用一个变量就可以搞定。

```python
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeros = 0
        res = 0

        for i in nums:
            if i == 0:
                zeros += 1
            else:
                if zeros > 0:
                    res += zeros * (zeros+1) // 2
                    zeros = 0
        return res + zeros * (zeros+1) // 2 if zeros > 0 else res
```

再来一个更简洁的：

```python
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                j = i + 1
            res += i - j + 1
        return res
```

或者：

```python
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeros = 0
        res = 0

        for i in nums:
            if i == 0:
                zeros += 1
                res += zeros
            else:
                zeros = 0
        return res
```
