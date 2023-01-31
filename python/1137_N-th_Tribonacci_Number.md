## N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

```
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

Example 2:

```
Input: n = 25
Output: 1389537
```

Constraints:

```
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
```

感觉我是猪。。

Explanation

```
Calculate next element d = a + b + c,
let (a,b,c) = (b,c,d).
Repeat this process n - 2 times;

We can loop n times and return i0.
It can remove the special cases for n < 2.
But I did n - 2 loop on purpose.
i1 and i2 will get overflow.
Though it won't throw an error in Java. Hardly say it's a right answer.

A possibly better solution is to start with the number before i0,i1,i2.
As I did in python,
i[-2] = 1
i[-1] = 1
i[0] = 0
Then it won't have this problem.

Complexity
Time O(N)
Space O(1)
```

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(n):
            dp[i % 3] = sum(dp)
        return dp[n % 3]
```

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 1, 0, 0
        for _ in range(n): a, b, c = b, c, a + b + c
        return c
```

过了几个月，感觉自己不是那么猪头了：

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0, 1, 1]
        if n < 3: 
            return nums[n]
        else:
            while len(nums) < n + 1:
                nums.append(nums[-1] + nums[-2] + nums[-3])
        return nums[-1]

```