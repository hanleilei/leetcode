# scramble string

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":
```
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
```
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
```
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
```
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
```
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
```
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:
```
Input: s1 = "great", s2 = "rgeat"
Output: true
```
Example 2:
```
Input: s1 = "abcde", s2 = "caebd"
Output: false
```


```Python
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False
```

```cpp
class Solution {
public:
    bool isScramble(string s1, string s2) {
         int n = s1.size();
         bool dp[30][30][31];
         for (int len = 1; len <= n; len ++){
            for (int i = 0; i + len <= n; i++){
                for (int j = 0; j + len <= n; j++){
                    if (len == 1) dp[i][j][len] = s1[i] == s2[j];
                    else{
                        for (int l = 1; l < len; l++){
                            dp[i][j][len] = (dp[i][j][l] && dp[i+l][j+l][len-l]) || (dp[i][j+len-l][l] && dp[i+l][j][len-l]);
                            if (dp[i][j][len]) break;
                        }
                    }
                }
            }
         }
         return dp[0][0][n];
    }
};
```

```cpp
class Solution {
public:
    bool isScramble(string s1, string s2) {
         int n = s1.size();
         int dp[30][30][31];
         memset(dp, -1, sizeof(dp));
         function<bool(int, int, int)> dfs = [&](int i, int j, int len) -> bool{
            int &res = dp[i][j][len];
            if (res != -1) return res;
            if (len == 1) return res = s1[i] == s2[j];
            for (int l = 1; l < len; l++){
                if ((dfs(i,j,l) && dfs(i + l, j + l, len - l))|| 
                    (dfs(i, j + len - l, l) && dfs(i + l, j, len- l))){
                        return res = true;
                    }
            }
            return res = false;
         };
         return dfs(0, 0, n);
    }
};
```

```cpp
#include <ranges>
class Solution {
public:
    bool isScramble(string s1, string s2) {
         int n = s1.size();
         int dp[30][30][31];
         memset(dp, -1, sizeof(dp));
         function<bool(int, int, int)> dfs = [&](int i, int j, int len) -> bool{
            int &res = dp[i][j][len];
            if (res != -1) return res;
            if (len == 1) return res = s1[i] == s2[j];
            return res = ranges::any_of(views::iota(1, len), [&] (int l) -> bool {
                return ((dfs(i,j,l) && dfs(i + l, j + l, len - l))|| 
                        (dfs(i, j + len - l, l) && dfs(i + l, j, len- l)));
            });
         };
         return dfs(0, 0, n);
    }
};
```
