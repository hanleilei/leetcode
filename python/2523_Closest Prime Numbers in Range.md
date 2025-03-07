# Closest Prime Numbers in Range

Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

Constraints:

1 <= left <= right <= 106

自己手搓的代码，慢的一批：

```python
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            """判断一个数是否是质数"""
            if not isinstance(n, int):
                return False
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            max_divisor = math.isqrt(n)
            for d in range(3, max_divisor + 1, 2):
                if n % d == 0:
                    return False
            return True
        prime = [i for i in range(left, right + 1) if is_prime(i)]
        l, r = -1, -1
        if len(prime) < 2:
            return [l, r]
        diff = defaultdict(list)
        for i in range(len(prime) - 1):
            diff[prime[i+1] - prime[i]].append((prime[i], prime[i+1]))
        min_key = min(diff.keys())
        return list(diff[min_key][0])
```

来个快的：

```python
import math


def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for divisor in range(2, math.isqrt(num) + 1):
        if num % divisor == 0:
            return False
    return True


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        primes = []
        for candidate in range(left, right + 1):
            if is_prime(candidate):
                if primes and candidate <= primes[-1] + 2:
                    return [primes[-1], candidate]  # twin or [2, 3]
                primes.append(candidate)
        
        gaps = ([primes[i - 1], primes[i]]
                for i in range(1, len(primes)))

        return min(gaps,
                   key=lambda gap: (gap[1] - gap[0], gap[0]),
                   default=[-1, -1])
```
