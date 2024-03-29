# edit distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

```comment
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

Example 2:

```comment
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

这个其实算得上是一个非常经典的题目了，参考GeekForGeek的解释：https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/

What are the subproblems in this case?
The idea is process all characters one by one staring from either from left or right sides of both strings.
Let us traverse from right corner, there are two possibilities for every pair of character being traversed.
```
m: Length of str1 (first string)
n: Length of str2 (second string)
```
If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings. So we recur for lengths m-1 and n-1.
Else (If last characters are not same), we consider all operations on ‘str1’, consider all three operations on last character of first string, recursively compute minimum cost for all three operations and take minimum of three values.
```
Insert: Recur for m and n-1
Remove: Recur for m-1 and n
Replace: Recur for m-1 and n-1
```

状态转移方程可以得到了，中止条件也很清楚，直接用递归解决问题：

```python
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m==0:
            return n

        # If second string is empty, the only option is to
        # remove all characters of first string
        if n==0:
            return m
        return self.editDistDP(word1, word2, m, n)

    # A Dynamic Programming based Python program for edit
    # distance problem
    def editDistDP(self, str1, str2, m, n):
        # Create a table to store results of subproblems
        dp = [[0 for x in range(n+1)] for x in range(m+1)]

        # Fill d[][] in bottom up manner
        for i in range(m+1):
            for j in range(n+1):

                # If first string is empty, only option is to
                # isnert all characters of second string
                if i == 0:
                    dp[i][j] = j    # Min. operations = j

                # If second string is empty, only option is to
                # remove all characters of second string
                elif j == 0:
                    dp[i][j] = i    # Min. operations = i

                # If last characters are same, ignore last char
                # and recur for remaining string
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                # If last character are different, consider all
                # possibilities and find minimum
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                       dp[i-1][j],        # Remove
                                       dp[i-1][j-1])    # Replace

        return dp[m][n]
```

再来一个速度更快的：

```python
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.dfs(word1,word2,(0,0),{})

    def dfs(self,word1,word2,pos,memo):
        if pos in memo:
            return memo[pos]
        i,j = pos
        if i == len(word1):
            memo[pos] = len(word2) - j
            return memo[pos]
        if j == len(word2):
            memo[pos] = len(word1) - i
            return memo[pos]
        if word1[i] == word2[j]:
            ans = self.dfs(word1,word2,(i + 1,j + 1),memo)
        else:
            ans = min(self.dfs(word1,word2,(i + 1,j + 1),memo),self.dfs(word1,word2,(i + 1,j),memo),self.dfs(word1,word2,(i,j + 1),memo)) + 1
        memo[pos] = ans
        return ans
```

再来一个heap版本的：

```python
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        import heapq
        heap = [(0, word1, word2)]
        seen = set()
        while heap:
            distance, w1, w2 = heapq.heappop(heap)

            if w1 == w2:
                return distance

            if (w1, w2) in seen:
                continue
            else:
                seen.add((w1,w2))

            if w1 and w2 and w1[-1] == w2[-1]:
                heapq.heappush(heap, (distance, w1[:-1], w2[:-1]))
            else:
                if w1:
                    heapq.heappush(heap, (distance+1, w1[:-1], w2))
                if w2:
                    heapq.heappush(heap, (distance+1, w1, w2[:-1]))
                if w1 and w2:
                    heapq.heappush(heap,(distance+1, w1[:-1], w2[:-1]))

```

再来一个deque的版本，也是最快的版本：

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        visit, dq = set(), collections.deque([(word1, word2, 0)])
        while True:
            w1, w2, d = dq.popleft()
            if (w1, w2) not in visit:
                if w1 == w2:
                    return d
                visit.add((w1, w2))
                while w1 and w2 and w1[0] == w2[0]:
                    w1, w2 = w1[1:], w2[1:]
                d += 1
                dq.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d),
                           (w1[1:], w2, d)])
```
