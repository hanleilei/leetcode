# perfect square

[[dp]] [[bfs]]

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

本题目是考察[四平方和定理](https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem)，根据四平方和定理，任意一个正整数均可表示为 4 个整数的平方和，其实是可以表示为 4 个以内的平方数之和，那么就是说返回结果只有 1,2,3 或 4 其中的一个，首先我们将数字化简一下，由于一个数如果含有因子 4，那么我们可以把 4 都去掉，并不影响结果，比如 2 和 8,3 和 12 等等，返回的结果都相同，读者可自行举更多的栗子。还有一个可以化简的地方就是，如果一个数除以 8 余 7 的话，那么肯定是由 4 个完全平方数组成，这里就不证明了，因为我也不会证明，读者可自行举例验证。那么做完两步后，一个很大的数有可能就会变得很小了，大大减少了运算时间，下面我们就来尝试的将其拆为两个平方数之和，如果拆成功了那么就会返回 1 或 2，因为其中一个平方数可能为 0. (注：由于输入的 n 是正整数，所以不存在两个平方数均为 0 的情况)。

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

```python
class Solution:
    def numSquares(self, n: int) -> int:
        if int(math.sqrt(n))**2 == n:
            return 1
        for j in range(int(math.sqrt(n))+1):
            if int(math.sqrt(n-j*j))**2 == n - j * j:
                return 2
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4
        return 3
```

先来一个 bfs 的方法：

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

使用bfs的思路就是类似于这样：

![](https://leetcode.com/uploads/files/1467720855285-xcoqwin.png)

```python
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        res = [i * i for i in range(1, n) if i * i <= n]
        count = 0
        verify = set([n])
        while verify:
            count += 1
            t = set()
            for x in verify:
                for y in res:
                    if x == y:
                        return count
                    if x < y:
                        break
                    t.add(x - y)
            verify = t
        return count
```

再来一个 dp 方法，来自于 stefhan 大大：

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

top down dp(recursion + memorization)

```python
class Solution:
    def numSquares(self, n: int) -> int:
        memo = [0] * (n + 1) 
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n < 4:
            return n
        if memo[n] != 0:
            return memo[n]
        ans = n
        for i in range(1, n + 1):
            square = i * i
            if square > n : break
            ans = min(ans, 1 + self.helper(n - square, memo))

        memo[n] = ans
        return ans
```

DP bottom up(using dp array)

```python
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            for j in range(1, i + 1):
                square = j * j
                if square > i: break
                dp[i] = min(dp[i], 1 + dp[i - square])
        return dp[n]\
```
