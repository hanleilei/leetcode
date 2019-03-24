# gray code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

```
00 - 0
01 - 1
11 - 3
10 - 2
```
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

很简单的算法，了解了就好，gray code其实就是先0， 1，然后在根据最下面的一行做镜像翻转。左边不足补1。

参考算法心得（hacker's delight）269页。
```python
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = list()
        for i in range(2**n):
            ans.append(i^(i>>1))
        return ans
```
或者，下面的两种写法都okay：

```python
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #return [i^(i>>1) for i in range(2**n)]
        return [i^(i>>1) for i in range(1<<n)]
```

上面的速度还凑合，参考下面的方法更快一些：
```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0, 1]
        for i in range(1, n):
            res = res + [2**i + j for j in res[::-1]]
        return res
```
