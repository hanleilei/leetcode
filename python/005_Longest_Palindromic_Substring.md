# Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

#### manacher 算法

Given a string S, we are to find the longest sub-string s of S such that the reverse of s is exactly the same as s.

First insert a special character ‘#’ between each pair of adjacent characters of S, in front of S and at the back of S. After that, we only need to check palindrome sub-strings of odd length.

Let P[i] be the largest integer d such that S[i-d,…,i+d] is a palindrome.  We calculate all P[i]s from left to right. When calculating P[i], we have to compare S[i+1] with S[i-1], S[i+2] with S[i-2] and so on. A comparison is successful if two characters are the same, otherwise it is unsuccessful. In fact, we can possibly skip some unnecessary comparisons utilizing the previously calculated P[i]s.
Assume P[a]+a=max{ P[j]+j :  j<i }. If P[a]+a >= i, then we have P[i] >= min{ P[2*a-i],  2*a-i-(a- P[a])}.

Is it the algorithm linear time? The answer is yes.

First the overall number of unsuccessful comparisons is obviously at most N.

A more careful analysis show that S[i] would never be compared successfully with any S[j](j<i) after its first time successful comparison with some S[k] (k<i).

So the number of overall comparisons is a most 2N.

还有一些中文的blog：http://blog.csdn.net/ggggiqnypgjg/article/details/6645824
还有这个：https://www.felix021.com/blog/read.php?2040 （写的非常清楚）

```Python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
```

直接在leetcode的blog上也有：https://articles.leetcode.com/longest-palindromic-substring-part-ii/

还有这个算法，需要仔细考虑以下：

```Python
class Solution:
    def longestPalindrome(self, s):
        l = len(s)
        if l <= 2:
            return s
        if s == s[::-1]:
            return s

        maxLen, start = 1, 0

        for i in range(l):
            odd = s[i - maxLen - 1:i + 1]
            even = s[i - maxLen:i + 1]
            if i - maxLen >= 1 and odd == odd[::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and even == even[::-1]:
                start = i - maxLen
                maxLen += 1

        return s[start:start + maxLen]
```

上面的算法由于添加了新的test case，现在不能通过了，例如："ac"

这类回文的问题，我们可以从中间往两边扩展，注意有一个条件要求就是i的位置，和i可以是单数或者双数，即回文的长度可以是单数或者单数。

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isvalid(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ""

        for i in range(len(s)):
            s1 = isvalid(s, i, i)
            s2 = isvalid(s, i, i+1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res
```

rolling hash + binary search + prefix_sum

很好的思考过程，但是。。要特么面试写这样写要死翘翘。。

参考这个[视频](https://www.bilibili.com/video/BV1MzBpBzEMk/?spm_id_from=333.1387.list.card_archive.click&vd_source=87d6dd47dbb44dd80e0f5eb84dd30767)

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    typedef unsigned long long ULL;
    static const ULL P = 131;
    
    vector<ULL> h1, h2, p;
    
    ULL get_hash(const vector<ULL>& h, int l, int r) {
        if (l < 1) l = 1;
        if (r >= h.size()) r = h.size() - 1;
        return h[r] - h[l - 1] * p[r - l + 1];
    }
    
    string longestPalindrome(string s) {
        int n = s.length();
        if (n == 0) return "";
        if (n == 1) return s;
        
        // 动态调整数组大小
        h1.resize(n + 1, 0);
        h2.resize(n + 1, 0);
        p.resize(n + 1, 1);
        
        // 初始化幂数组
        for (int i = 1; i <= n; i++) {
            p[i] = p[i - 1] * P;
        }
        
        // 预处理正序哈希数组
        for (int i = 1; i <= n; i++) {
            h1[i] = h1[i - 1] * P + (s[i - 1] - 'a' + 1);
        }
        
        // 预处理倒序哈希数组
        string reversed_s = s;
        reverse(reversed_s.begin(), reversed_s.end());
        for (int i = 1; i <= n; i++) {
            h2[i] = h2[i - 1] * P + (reversed_s[i - 1] - 'a' + 1);
        }
        
        int max_len = 1;
        int start = 0;
        
        for (int i = 0; i < n; i++) {
            // 奇数长度回文
            int left = 0, right = min(i, n - 1 - i);
            while (left <= right) {
                int mid = (left + right) / 2;
                int l_bound = i - mid;
                int r_bound = i + mid;
                
                // 正序子串哈希
                ULL hash_forward = get_hash(h1, l_bound + 1, r_bound + 1);
                // 对应的倒序子串哈希（注意索引转换）
                ULL hash_backward = get_hash(h2, n - r_bound, n - l_bound);
                
                if (hash_forward == hash_backward) {
                    int curr_len = 2 * mid + 1;
                    if (curr_len > max_len) {
                        max_len = curr_len;
                        start = l_bound;
                    }
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            
            // 偶数长度回文
            if (i < n - 1 && s[i] == s[i + 1]) {
                left = 0;
                right = min(i, n - 2 - i);
                while (left <= right) {
                    int mid = (left + right) / 2;
                    int l_bound = i - mid;
                    int r_bound = i + 1 + mid;
                    
                    if (l_bound < 0 || r_bound >= n) break;
                    
                    ULL hash_forward = get_hash(h1, l_bound + 1, r_bound + 1);
                    ULL hash_backward = get_hash(h2, n - r_bound, n - l_bound);
                    
                    if (hash_forward == hash_backward) {
                        int curr_len = 2 * mid + 2;
                        if (curr_len > max_len) {
                            max_len = curr_len;
                            start = l_bound;
                        }
                        left = mid + 1;
                    } else {
                        right = mid - 1;
                    }
                }
                
                // 检查最小偶数回文
                if (max_len < 2) {
                    max_len = 2;
                    start = i;
                }
            }
        }
        
        return s.substr(start, max_len);
    }
};
```
