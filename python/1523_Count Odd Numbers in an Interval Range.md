# Count Odd Numbers in an Interval Range

[[math]]

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

Constraints:

0 <= low <= high <= 10^9

数学计算

```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        计算区间内奇数的数量
        时间复杂度：O(1)，空间复杂度：O(1)
        """
        return (high + 1) // 2 - low // 2
```
