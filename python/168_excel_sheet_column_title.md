# Excel Sheet Column title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
```

需要对于python中的chr和ord函数非常了解，然后很多就很好做。

```python
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""

        while n:
            result += chr((n - 1) % 26 + ord('A'))
            n = (n - 1) // 26

        return result[::-1]

```

再来一个速度快一点的：

```python
class Solution(object):
    def __init__(self):
        self.alpha = {i+1: v for i, v in enumerate(ascii_uppercase)}
        self.alpha[0] = 'Z'

    def convertToTitle(self, n: 'int') -> 'str':

        if n in self.alpha:
            return self.alpha[n]

        res = ''
        if n % 26 == 0:
            res += self.convertToTitle(n // 26 - 1)
        else:
            res += self.convertToTitle(n // 26)

        res += self.alpha.get(n % 26)

        # 下面的这段代码有点莫名其妙
        # if n not in self.alpha:
        #     self.alpha[n] = res
        return res
```

上面的方法，有点不是太容易理解，再来一个简单点的：

```Python
class Solution:
    def convertToTitle(self, n: int) -> str:
        capitals = string.ascii_uppercase
        result = []
        while n > 0:
            result.append(capitals[(n-1)%26])
            n = (n-1) // 26
        result.reverse()
        return ''.join(result)
```
