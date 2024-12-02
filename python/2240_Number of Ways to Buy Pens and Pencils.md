# [ Number of Ways to Buy Pens and Pencils](https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/)

You are given an integer `total` indicating the amount of money you have. You are also given two integers `cost1` and `cost2` indicating the price of a pen and pencil respectively. You can spend **part or all** of your money to buy multiple quantities (or none) of each kind of writing utensil.

Return *the **number of distinct ways** you can buy some number of pens and pencils.*

**Example 1:**

<pre><strong>Input:</strong> total = 20, cost1 = 10, cost2 = 5
<strong>Output:</strong> 9
<strong>Explanation:</strong> The price of a pen is 10 and the price of a pencil is 5.
- If you buy 0 pens, you can buy 0, 1, 2, 3, or 4 pencils.
- If you buy 1 pen, you can buy 0, 1, or 2 pencils.
- If you buy 2 pens, you cannot buy any pencils.
The total number of ways to buy pens and pencils is 5 + 3 + 1 = 9.
</pre>

**Example 2:**

<pre><strong>Input:</strong> total = 5, cost1 = 10, cost2 = 10
<strong>Output:</strong> 1
<strong>Explanation:</strong> The price of both pens and pencils are 10, which cost more than total, so you cannot buy any writing utensils. Therefore, there is only 1 way: buy 0 pens and 0 pencils.
</pre>

**Constraints:**

* `1 <= total, cost1, cost2 <= 10<sup>6</sup>`

```python
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        for i in range(total // cost1 + 1):
            res += (total - i * cost1) // cost2 + 1
        return res
```

效率感人，主要问题在于 total // cost1 的时候，如果比例很大，则计算时间太长，下面是网上最快的版本：

```python
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:

        cheap = cost1
        expensive = cost2

        if cost1 > total and cost2 > total: return 1
        if cost1 > total: return (total // cost2) + 1
        if cost2 > total: return (total // cost1) + 1
        # if cost1 == cost2 == total: return 3

        if cost1 == cost2:
            x = math.ceil((total + 1) / cost1)
            return x * (x + 1) // 2

        if cheap > expensive:
            cheap, expensive = expensive, cheap

        ways = 0
        for i in range(total // expensive + 1):
            ways += (total -i * expensive) // cheap + 1

        return ways
```

或者：

```python
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        n = 1 + total // cost1
        return n + sum((total - cost1 * i) // cost2 for i in range(n))
```
