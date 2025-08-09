# Find the Original Typed String I

[[stack]]

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

## Example 1

Input: word = "abbcccc"

Output: 5

Explanation:

The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".

## Example 2

Input: word = "abcd"

Output: 1

Explanation:

The only possible string is "abcd".

## Example 3

Input: word = "aaaa"

Output: 4

Constraints:

1 <= word.length <= 100
word consists only of lowercase English letters.

就是compress string的翻版，之前只要计数每个字母出现的频率，现在要做一个总体的可能行计数。

```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        res = 1
        word += "#"
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                if count > 1:
                    res += count - 1
                    count = 1
        return res                
```

```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        possible = 1  # original word

        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                possible += 1

        return possible
```

```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        stack = []
        ans = 1 

        for w in word:
            if not stack or (stack and w==stack[-1]):
                stack.append(w)
            else:
                ans+=len(stack)-1
                stack = [w]
        ans+=len(stack)-1
        return ans 
```
