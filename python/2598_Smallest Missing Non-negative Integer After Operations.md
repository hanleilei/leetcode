# Smallest Missing Non-negative Integer After Operations

You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

 

Example 1:

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.
Example 2:

Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
Explanation: One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve.
 

Constraints:

1 <= nums.length, value <= 10**5
-109 <= nums[i] <= 10**9

好蛋疼的一个题目，主要在于：
1. 

```python
class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        # 1. 统计所有元素模 value 后的余数频率
        # Python 的 % 运算符对于负数的结果：-10 % 5 = 0，这是对的。
        # 但 -10 % 7 = 4。 如果我们希望余数总是在 [0, value-1] 范围内：
        # 对于非负数 x: x % value
        # 对于负数 x: (x % value + value) % value
        # 幸运的是，Python 中 (a % n + n) % n 这种形式对于正负数都适用，
        # 但对于 value > 0 的情况，直接使用 a % value 即可得到在 [0, value-1] 范围内的余数。
        # 例如: -10 % 5 = 0; -10 % 7 = 4。 这正是我们需要的余数 r = i % value
        
        # 因此，直接对所有元素取模 value 并统计频率
        
        # 优化：因为 i % value 永远在 [0, value-1] 范围内，
        # 我们可以只统计这 value 种余数的频率，使用一个大小为 value 的数组即可。
        
        remainder_counts = [0] * value
        for x in nums:
            # Python 的 % 运算符的结果符号与 divisor 一致。
            # x % value 结果在 [0, value-1] 范围内。
            r = x % value
            remainder_counts[r] += 1
            
        # 2. 贪心构造 MEX
        i = 0
        while True:
            # 目标数 i 所需的余数 r 
            r = i % value
            
            # 检查是否有可用余数
            if remainder_counts[r] > 0:
                # 有，消耗一个余数，继续尝试构造 i+1
                remainder_counts[r] -= 1
                i += 1
            else:
                # 没有可用余数，当前 i 就是最小的缺失非负整数 (MEX)
                return i
```

再来一个速度快的：

```python
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        if value == 1:
            return n
            
        dp = [0] * value

        for n in nums:
            dp[n % value] += 1

        rounds = min(dp)

        #This approach is faster than the one below.
        for i in range(value):
            if dp[i] - rounds == 0:
                return (rounds * value) + i
        
```

看下lee215:

```python
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = Counter(a % value for a in nums)
        stop = 0
        for i in range(value):
            if count[i] < count[stop]:
                stop = i
        return value * count[stop] + stop
```
