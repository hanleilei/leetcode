# Find Triangular Sum of an Array

You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.


Example 1:

![](https://assets.leetcode.com/uploads/2022/02/22/ex1drawio.png)

Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.
Example 2:

Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 9

目前，我只能手搓一个时间复杂度O(n^2)的方法：

```python
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            for i in range(n - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            n -= 1
        return nums[0]
```

再来一个O(N)的方法：

组合数 $C(n, k)$ 表示从 n个元素中选 k个的组合数，计算公式为：$C(n, k) = \frac{n!}{k!(n-k)!}$

在代码中，comb的初始值是 C(n-1, 0) = 1。然后通过递推关系计算下一个组合数：$C(n-1, i+1) =C(n-1, i) * \frac{(n - 1 - i)}{i + 1}$

代码中更新 comb的公式为：$comb = comb * \frac{(m - i)}{(i + 1)}$

其中：
m=n−1
i是当前元素的索引（从 0 开始）
示例计算

对于 nums = [1, 2, 3, 4, 5]，n=5，m=4：
初始：comb=C(4,0)=1
迭代过程：
- i = 0: $comb = 1 * \frac{4 - 0}{0 + 1}$
- i = 1: $comb = 4 * \frac{4 - 1}{1 + 1}$
- i = 2: $comb = 6 * \frac{4 - 2}{2 + 1}$
- i = 3: $comb = 4 * \frac{4 - 3}{3 + 1}$
- i = 4: $comb = 1 * \frac{4 - 4}{4 + 1}$

最终结果: $res = (\sum_{i=0}^{n}C(n-1, i)* nums[i]) \mod 10$



```python
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        comb = 1        # C(n-1,0)
        m = n - 1
        for i, x in enumerate(nums):
            res = (res + comb * x) % 10
            if i < m:
                comb = comb * (m - i) // (i + 1)  # 整数除法，结果为下一个二项式系数
        return res
```
