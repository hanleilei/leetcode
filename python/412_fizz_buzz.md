# Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

## 符合人类的思维习惯。

```python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for x in range(1, n + 1):
            n = str(x)
            if x % 15 == 0:
                n = "FizzBuzz"
            elif x % 3 == 0:
                n = "Fizz"
            elif x % 5 == 0:
                n = "Buzz"
            ans.append(n)
        return ans
```
