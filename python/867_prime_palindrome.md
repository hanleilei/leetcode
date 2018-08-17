# Prime Palindrome

Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

For example, 12321 is a palindrome.

 

Example 1:
```
Input: 6
Output: 7
```

Example 2:
```
Input: 8
Output: 11
```

Example 3:
```
Input: 13
Output: 101
```

简单的说：偶数的情况只需要考虑11，

```python
class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        All palindrome with even digits is multiple of 11.

		11 % 11 = 0
		1111 % 11 = 0
		111111 % 11 = 0
		11111111 % 11 = 0

		1001 % 11 = (1111 - 11 * 10) % 11 = 0
		100001 % 11 = (111111 - 1111 * 10) % 11 = 0
		10000001 % 11 = (11111111 - 111111 * 10) % 11 = 0

		for any palindrome with even digits:
		abcdeedcba % 11
		= (a * 10000001 + b * 100001 * 10 + c * 1001 * 100 + d * 11 * 1000) % 11
		= 0

		All palindrome with even digits is multiple of 11.
		So among them, 11 is the only one prime
		if (8 <= N <= 11) return 11
		For other, we consider only palindrome with odd dights.
        """
        def isPrime(x):
            if x < 2 or x % 2 == 0: return x == 2
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0: return False
            return True
        if 8 <= N <= 11: return 11
        for x in range(10 ** (len(str(N)) // 2), 10**5):
            y = int(str(x) + str(x)[-2::-1])
            if isPrime(y) and y >= N: return y
        

```