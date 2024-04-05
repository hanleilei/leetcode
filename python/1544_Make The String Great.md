# Make The String Great

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

## Example 1

```text
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
```

## Example 2

```text
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
```

## Example 3

```text
Input: s = "s"
Output: "s"
```

## Constraints

```text
1 <= s.length <= 100
s contains only lower and upper case English letters.
```

方法是用 stack：

```python
class Solution:
    def makeGood(self, s: str) -> str:
        stack = list(s[0])
        if len(s) == 1:
            return s

        for i in range(1, len(s)):
            if stack and s[i].lower() == stack[-1].lower() and s[i] != stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)
```

评论区的更好的方法：

```python
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c.swapcase():
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
```

或者现在自己的方法：

```python
class Solution:
    def makeGood(self, s: str) -> str:
        stack = list()
        for i in s:
            if stack and stack[-1] != i and stack[-1].lower() == i.lower():
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
```

看起来自己还是有点长进。。
