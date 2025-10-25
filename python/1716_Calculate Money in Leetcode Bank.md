# Calculate Money in Leetcode Bank

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

## Example 1

```text
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
```

## Example 2

```text
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
```

## Example 3

```text
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
```

## Constraints

```text
1 <= n <= 1000
```

纯粹的数学问题，想清楚逻辑。。

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        count = 0
        weeks = n//7+1

        for week in range(weeks):
            if week == weeks-1:
                for day in range(1,n%7+1):
                    count += week + day
            else:
                for day in range(1,8):
                    count += week + day

        return count
```

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        f = n // 7
        d = n % 7
        return (49 + 7 * f) * f // 2 + (2 * f + d + 1) * d // 2
```

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        x, y = divmod(n, 7)
        return x * sum(range(1, 8)) +  x * (x - 1) // 2 * 7 + x * y + sum(range(1, y + 1))
```
