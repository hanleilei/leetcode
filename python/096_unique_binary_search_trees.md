# unique binary search trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

```python
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        参考下面链接中的公式
        http://blog.csdn.net/sunnyyoona/article/details/42177001
        """
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[-1]
```
