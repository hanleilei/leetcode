# Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

### Example 1:
```
Input: "()())()"
Output: ["()()()", "(())()"]
```
### Example 2:
```
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
```
### Example 3:
```
Input: ")("
Output: [""]
```
直接上dfs：

```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []

        def remove(s, last_i, last_j, pair):
            count = 0
            n = len(s)
            for i in range(last_i, n):
                if s[i] == pair[0]:
                    count += 1
                elif s[i] == pair[1]:
                    count -= 1
                if count >= 0:
                    continue
                for j in range(last_j, i+1):
                    if s[j] == pair[1] and (j == last_j or s[j] != s[j-1]):
                        remove(s[:j] + s[j+1:], i, j, pair)
                return
            reverse = s[::-1]
            if pair[0] == '(':
                remove(reverse, 0, 0, [')', '('])
            else:
                res.append(reverse)

        remove(s, 0, 0, ['(', ')'])
        return res
```

```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return ['']

        self.ans = []
        self.dfs(s, 0, 0, ['(', ')'])
        return self.ans

    def dfs(self, s, start_i, start_j, pa):
        count = 0

        for i in range(start_i, len(s)):
            if s[i] == pa[0]:
                count += 1
            elif s[i] == pa[1]:
                count -= 1
            if count < 0:
                for j in range(start_j, i + 1):
                    if s[j] == pa[1] and (j == 0 or s[j - 1] != pa[1]):
                        self.dfs(s[:j] + s[j + 1:], i, j, pa)
                return

        s = s[::-1]
        if pa[0] == '(':
            self.dfs(s, 0, 0, [')', '('])
        else:
            self.ans.append(s)
```
