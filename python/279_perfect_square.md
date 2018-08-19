# perfect square

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
```
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
```
Example 2:
```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

本题目是考察四平方和定理，根据四平方和定理，任意一个正整数均可表示为4个整数的平方和，其实是可以表示为4个以内的平方数之和，那么就是说返回结果只有1,2,3或4其中的一个，首先我们将数字化简一下，由于一个数如果含有因子4，那么我们可以把4都去掉，并不影响结果，比如2和8,3和12等等，返回的结果都相同，读者可自行举更多的栗子。还有一个可以化简的地方就是，如果一个数除以8余7的话，那么肯定是由4个完全平方数组成，这里就不证明了，因为我也不会证明，读者可自行举例验证。那么做完两步后，一个很大的数有可能就会变得很小了，大大减少了运算时间，下面我们就来尝试的将其拆为两个平方数之和，如果拆成功了那么就会返回1或2，因为其中一个平方数可能为0. (注：由于输入的n是正整数，所以不存在两个平方数均为0的情况)。

```python
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        def isSquare(n):
            if int(math.sqrt(n)) ** 2 == n: return 1

        if isSquare(n): return 1

        # 4**k(8i+7)
        while n & 3 == 0:
            n >>= 2

        if n & 7 == 7:
            return 4

        for i in range(1, int(math.sqrt(n))+1):
            if isSquare(n - i ** 2):
                return 2

        return 3
```

先来一个bfs的方法：

```python
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue:
            i, step = queue.popleft()
            step += 1
            for j in range(1, n + 1):
                k = i + j * j
                if k > n:
                    break
                if k == n:
                    return step
                if k not in visited:
                    visited.add(k)
                    queue.append((k, step))
```

再来一个dp方法，来自于stefhan大大：

```python
class Solution:
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
```
注意行尾的逗号。
