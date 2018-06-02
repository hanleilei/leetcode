# wildcard match

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

```
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
```
The matching should cover the entire input string (not partial).

Note:
```
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
```
Example 1:
```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```
Example 2:
```
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
```
Example 3:
```
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```
Example 4:
```
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
```
Example 5:
```
Input:
s = "acdcb"
p = "a*c?b"
Output: false
```

```c++
class Solution {
public:
    bool isMatch(string s, string p) {
        int  slen = s.size(), plen = p.size(), i, j, iStar=-1, jStar=-1;

        for(i=0,j=0 ; i<slen; ++i, ++j)
        {
            if(p[j]=='*')
            { //meet a new '*', update traceback i/j info
                iStar = i;
                jStar = j;
                --i;
            }
            else
            {
                if(p[j]!=s[i] && p[j]!='?')
                {  // mismatch happens
                    if(iStar >=0)
                    { // met a '*' before, then do traceback
                        i = iStar++;
                        j = jStar;
                    }
                    else return false; // otherwise fail
                }
            }
        }
        while(p[j]=='*') ++j;
        return j==plen;
    }
};
```

再来一个：

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int s_long = s.size(), p_long = p.size();
        int i = 0 ,j = 0;
        int match;
        int risk = -1;
        while (i < s_long) {
            if (j < p_long && p[j] == '*') {
                match = i;
                risk = j++;
            }
            else if (j < p_long && (p[j] == s[i] || p[j] == '?')) {
                ++i;
                ++j;
            }
            else if (risk >= 0) {
                i = ++match;
                j = risk + 1;
            }
            else return false;
        }
        while (j < p_long && p[j] == '*') ++j;
        return j == p_long;
    }
};
```
