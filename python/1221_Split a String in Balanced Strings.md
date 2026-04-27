# Split a String in Balanced Strings

[[stack]] [[greedy]]

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

    Each substring is balanced.

Return the maximum number of balanced strings you can obtain.

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Constraints:

    2 <= s.length <= 1000
    s[i] is either 'L' or 'R'.
    s is a balanced string.

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        for i in s:
            if i == "L":
                left += 1
            elif i == "R":
                right += 1
            if left == right:
                res += 1
                left = 0
                right = 0
        return res
```

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        count = 0

        for i in s:
            if i == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                ans += 1

        return ans
```

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = list()
        res = 0
        
        for i in s:
            if len(stack) == 0:
                res += 1
                stack.append(i)
            else:
                if (i == "R"and stack[-1] == "L") or (i == "L" and stack[-1] == "R"):
                    stack.pop()
                else:
                    stack.append(i)
        return res 
```
