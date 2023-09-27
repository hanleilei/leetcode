# Remove Duplicate Letters

[[stack]]

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order among all possible results.

## Example 1

```text
Input: s = "bcabc"
Output: "abc"
```

## Example 2

```text
Input: s = "cbacdcbc"
Output: "acdb"
```

## Constraints

- 1 <= s.length <= 104
- s consists of lowercase English letters.

Note: This question is the same as 1081: `https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/`

这就是一个很好的stack的问题：

- We traverse sequentially on the string
- For each s[i], we check whether it's already in stack or not
- if its not in the stack, we need to push it to the stack. But we need to check another condition before pushing.
- If s[i] is not in the stack (we can check using this in O(1) using a set), and it is smaller than previous elements in stack (lexicographically), and those elements are repeating in future (can check with last_occ), we need to pop these elements
- Now we can push s[i] in stack
- Finally just join the characters in stack to form the result

Example:

```text
s = 'bcabc'
last_occ = { a : 2, b : 3, c : 4 }
stack trace:
[]
[ 'b' ]
[ 'b', 'c' ]
[ 'a' ] (b & c got popped because a < c, a < b and b and c both were gonna repeat in future)
[ 'a' , 'b' ]
[ 'a' , 'b', 'c' ]
```

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = dict()
        stack = list()
        visited = set()
        for i in range(len(s)):
            last_occ[s[i]] = i
        
        for i in range(len(s)):
            if s[i] not in visited:
                while stack and stack[-1] > s[i] and last_occ[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return ''.join(stack)
```
