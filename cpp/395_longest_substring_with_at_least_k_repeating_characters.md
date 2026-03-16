# longest substring with at least k repeating characters

[[slidingwindow]] [[DivideConquer]] [[stack]]

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:

1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^5

```cpp
class Solution {
public:
    int longestSubstring(string str, int k) {
        int n = str.length();
        int ans = 0;
        
        // 每次要求子串必须含有require种字符，每种字符都必须>=k次，这样的最长子串是多长
        for (int require = 1; require <= 26; require++) {
            vector<int> cnts(256, 0);  // 用于统计字符出现的次数
            int collect = 0, satisfy = 0;
            
            // l....r 滑动窗口
            for (int l = 0, r = 0; r < n; r++) {
                
                if (++cnts[str[r]] == 1) {
                    collect++;
                }
                if (cnts[str[r]] == k) {
                    satisfy++;
                }
                
                // l....r 种类超了！调整窗口
                while (collect > require) {
                    if (--cnts[str[l]] == 0) {
                        collect--;
                    }
                    if (cnts[str[l++]] == k - 1) {
                        satisfy--;
                    }
                }
                
                // 满足条件的子串更新答案
                if (satisfy == require) {
                    ans = max(ans, r - l + 1);
                }
            }
        }
        return ans;
    }
};
```
