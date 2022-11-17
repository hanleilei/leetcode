# guess number higher or lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
1 : My number is higher
0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
Subscribe to see which companies asked this question

#### binary search

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == 1:
                left = mid + 1
            elif res == -1:
                right = mid - 1
            else:
                return mid
        return -1
```

```python
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1

        while left <= n:
            mid = left + (n - left) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                n = mid - 1
        return -1
```
