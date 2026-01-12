# 72. Edit Distance

## 问题描述

Given two words word1 and word2, find the minimum number of
operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

## 示例

**Example 1:**

```text
Input: word1 = "horse", word2 = "ros"
Output: 3
```

Explanation:

- horse -> rorse (replace 'h' with 'r')
- rorse -> rose (remove 'r')
- rose -> ros (remove 'e')

**Example 2:**

```text
Input: word1 = "intention", word2 = "execution"
Output: 5
```

Explanation:

- intention -> inention (remove 't')
- inention -> enention (replace 'i' with 'e')
- enention -> exention (replace 'n' with 'x')
- exention -> exection (replace 'n' with 'c')
- exection -> execution (insert 'u')

## 约束条件

- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.

## 解法分析

这是一个经典的动态规划问题，也被称为编辑距离（Levenshtein
Distance）。

### 核心思路

定义 $dp[i][j]$ 表示将 word1 的前 i 个字符转换为 word2 的前 j
个字符所需的最少操作数。

状态转移方程：

1. 如果 $word1[i-1] = word2[j-1]$，字符相同：
   - $dp[i][j] = dp[i-1][j-1]$

2. 如果字符不同，取三种操作的最小值：
   - 插入：$dp[i][j] = dp[i][j-1] + 1$
   - 删除：$dp[i][j] = dp[i-1][j] + 1$
   - 替换：$dp[i][j] = dp[i-1][j-1] + 1$

边界条件：

- $dp[0][j] = j$（word1为空，需要插入j个字符）
- $dp[i][0] = i$（word2为空，需要删除i个字符）

参考资料：[GeeksforGeeks - Edit Distance](https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/)

## 解法

列出状态转移方程：

$$
[
cnt_{i,j} =
\begin{cases}
    0, & \text{if } i = 0 \text{ and } j = 0 \\
    j, & \text{if } i = 0 \\
    i, & \text{if } j = 0 \\
    cnt_{i-1,j-1}, & \text{if } word1[i-1] = word2[j-1] \\
    \min(cnt_{i-1,j}, cnt_{i,j-1}, cnt_{i-1,j-1}) + 1  & \text{if } word1[i-1] \neq word2[j-1]
\end{cases}
]
$$

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();

        vector<vector<int>> dp(n + 1, vector<int>(m + 1));
        
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = 0;
                } else if (i == 0) {
                    dp[i][j] = j;  // 插入j个字符
                } else if (j == 0) {
                    dp[i][j] = i;  // 删除i个字符
                } else if (word1[i-1] == word2[j-1]) {  // 注意：字符串索引是i-1和j-1
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    // 注意：这里应该取三种操作的最小值
                    // 1. 删除字符：dp[i-1][j] + 1
                    // 2. 插入字符：dp[i][j-1] + 1
                    // 3. 替换字符：dp[i-1][j-1] + 1
                    dp[i][j] = 1 + min({dp[i-1][j],  // 删除
                                        dp[i][j-1],  // 插入
                                        dp[i-1][j-1]});  // 替换
                }
            }
        }
        
        return dp[n][m];
    }
};
```
