# Longest Palindromic Subsequence

[[dp]]

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

 

Constraints:

    1 <= s.length <= 1000
    s consists only of lowercase English letters.

```cpp
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        // dp[i][j] 表示 s[i..j] 范围内的最长回文子序列长度
        vector<vector<int>> dp(n, vector<int>(n, 0));

        // 单个字符的最长回文子序列长度为 1
        for (int i = 0; i < n; ++i) {
            dp[i][i] = 1;
        }
         // 枚举子串长度
        for (int len = 2; len <= n; ++len) {
            // 枚举子串起点
            for (int i = 0; i <= n - len; ++i) {
                int j = i + len - 1; // 子串终点
                if (s[i] == s[j]) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][n - 1];
    }
};
```

```cpp
class Solution {
public:
    int longestPalindromeSubseq(string str) {
        int len=str.length();
        vector<int> dp(len,0);
        dp[len-1]=1;
        for(int i=len-2,leftdown,backup;i>=0;i--){
            dp[i]=1;
            if(i+1<len){
                leftdown=dp[i+1];
                dp[i+1]=(str[i]==str[i+1]?2:1);
            }
            for(int j=i+2;j<len;j++){
                backup=dp[j];
                if(str[i]==str[j]){
                    dp[j]=2+leftdown;
                }else{
                    dp[j]=max(dp[j-1],dp[j]);
                }
                leftdown=backup;
            }
        }
        return dp[len-1];
    }
};
```
