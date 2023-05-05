# Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

## Example 1:
```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
```
## Example 2:
```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
```
## Example 3:
```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
```

## Constraints:
```
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
```
sliding windows。。自己的方法，比较。。重复代码比较多。。


```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        end = k-1
        vowels = {'a','e','i','o','u'}
        t = len([i for i in s[:k] if i in vowels])        
        res = t

        while end < len(s)-1:
            if s[start] in vowels:
                t -= 1
                res = max(res, t)
            start += 1
            if s[end+1] in vowels:
                t += 1
                res = max(res, t)
            end += 1
        return res
```

再来一个简练的：

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = cnt = 0
        for i, c in enumerate(s):
            if c in vowels:
                cnt += 1
            if i >= k and s[i - k] in vowels:
                cnt -= 1
            ans  = max(cnt, ans)
        return ans  
```

