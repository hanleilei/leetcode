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
