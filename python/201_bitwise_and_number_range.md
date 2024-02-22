# bitwise and numbers range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# Example 1

```text
Input: [5,7]
Output: 4
```

# Example 2

```text
Input: [0,1]
Output: 0
```

```python
class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        length = (m ^ n)#.bit_length()
        n >>= length
        return n << length
```

```python
class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        length = (m ^ n).bit_length()
        n >>= length
        return n << length
```

```python
class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i
```

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right-1)
        return left & right
```
