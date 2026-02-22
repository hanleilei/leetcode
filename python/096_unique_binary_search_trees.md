# unique binary search trees

[[dp]] [[tree]] [[BST]] [[backtracking]]

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example 1:

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

Example 2:

Input: n = 1
Output: 1

Constraints:

1 <= n <= 19

dp:

观察一下，如果只有一个元素，则只有一种构造方式；如果有两个元素，则有两种构造方式：

```
  1         2
   \       /
    2     1
```

如果有三个元素，则有五种构造方式：

```
    1         1         2         3         3
     \         \       / \       /         /
      2         3     1   3     2         1
       \       /               /           \
        3     2               1             2
```

假设 f(n) 表示 n 个节点能构成的不同 BST 的个数，那么得到递推公式：

$$
f(i) = \sum_{k=1}^{i} f(k-1) * f(i-k)
$$

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
        return dp[n]
```

backtracking:

```python
class Solution:
    def numTrees(self, n: int) -> int:
        # 计算闭区间 [1, n] 组成的 BST 个数
        return self.count(1, n)

    # 计算闭区间 [lo, hi] 组成的 BST 个数
    def count(self, lo: int, hi: int) -> int:
        # base case
        if lo > hi: 
            return 1

        res = 0
        for i in range(lo, hi+1):
            # i 的值作为根节点 root
            left = self.count(lo, i - 1)
            right = self.count(i + 1, hi)
            # 左右子树的组合数乘积是 BST 的总数
            res += left * right

        return res
```
