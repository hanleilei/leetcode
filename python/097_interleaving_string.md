# interleaving string

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
```

Example 2:
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```

还是看一个是用set的方法.

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False
        if not s1 or not s2:
            return (s1 or s2) == s3
        options = {(0, 0)}
        for char in s3:
            new_options = set()
            for i1, i2 in options:
                if i1 < len(s1) and char == s1[i1]:
                    new_options.add((i1 + 1, i2))
                if i2 < len(s2) and char == s2[i2]:
                    new_options.add((i1, i2 + 1))
            options = new_options
            if not options:
                return False
        return True
```

还有一个递归的方法，用的是字典：

```python
class Solution:
    def isInterleave(self, s1, s2, s3, memo=dict()):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3): return False
        if not s1 and not s2 and not s3: return True
        if (s1, s2, s3) in memo:         return memo[s1, s2, s3]
        memo[s1,s2,s3] =\
               (len(s1) > 0 and len(s3) > 0 and s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:], memo)) or\
               (len(s2) > 0 and len(s3) > 0 and s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:], memo))
        return memo[s1,s2,s3]

```

完全看看caikehe的所有bfs和dfs的方法。

```python
# O(m*n) space
def isInterleave1(self, s1, s2, s3):
    r, c, l= len(s1), len(s2), len(s3)
    if r+c != l:
        return False
    dp = [[True for _ in xrange(c+1)] for _ in xrange(r+1)]
    for i in xrange(1, r+1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    for j in xrange(1, c+1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    for i in xrange(1, r+1):
        for j in xrange(1, c+1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
               (dp[i][j-1] and s2[j-1] == s3[i-1+j])
    return dp[-1][-1]

# O(2*n) space
def isInterleave2(self, s1, s2, s3):
    l1, l2, l3 = len(s1)+1, len(s2)+1, len(s3)+1
    if l1+l2 != l3+1:
        return False
    pre = [True for _ in xrange(l2)]
    for j in xrange(1, l2):
        pre[j] = pre[j-1] and s2[j-1] == s3[j-1]
    for i in xrange(1, l1):
        cur = [pre[0] and s1[i-1] == s3[i-1]] * l2
        for j in xrange(1, l2):
            cur[j] = (cur[j-1] and s2[j-1] == s3[i+j-1]) or \
                     (pre[j] and s1[i-1] == s3[i+j-1])
        pre = cur[:]
    return pre[-1]

# O(n) space
def isInterleave3(self, s1, s2, s3):
    r, c, l= len(s1), len(s2), len(s3)
    if r+c != l:
        return False
    dp = [True for _ in xrange(c+1)] 
    for j in xrange(1, c+1):
        dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
    for i in xrange(1, r+1):
        dp[0] = (dp[0] and s1[i-1] == s3[i-1])
        for j in xrange(1, c+1):
            dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
    return dp[-1]
    
# DFS 
def isInterleave4(self, s1, s2, s3):
    r, c, l= len(s1), len(s2), len(s3)
    if r+c != l:
        return False
    stack, visited = [(0, 0)], set((0, 0))
    while stack:
        x, y = stack.pop()
        if x+y == l:
            return True
        if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
            stack.append((x+1, y)); visited.add((x+1, y))
        if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
            stack.append((x, y+1)); visited.add((x, y+1))
    return False
            
# BFS 
def isInterleave(self, s1, s2, s3):
    r, c, l= len(s1), len(s2), len(s3)
    if r+c != l:
        return False
    queue, visited = [(0, 0)], set((0, 0))
    while queue:
        x, y = queue.pop(0)
        if x+y == l:
            return True
        if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
            queue.append((x+1, y)); visited.add((x+1, y))
        if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
            queue.append((x, y+1)); visited.add((x, y+1))
    return False
```
