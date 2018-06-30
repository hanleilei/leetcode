# score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

* () has score 1
* AB has score A + B, where A and B are balanced parentheses strings.
* (A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:
```
Input: "()"
Output: 1
```
Example 2:
```
Input: "(())"
Output: 2
```
Example 3:
```
Input: "()()"
Output: 2
```
Example 4:
```
Input: "(()(()))"
Output: 6
```

# 惭愧，这么简单的动态规划就是做不粗来。。

```python
class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        res, i = [0] * 30, 0
        for c in S:
            i += 1 if c == '(' else -1
            res[i] = res[i] + max(res[i + 1] * 2, 1) if c == ')' else 0
        return res[0]
```
