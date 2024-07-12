# Maximum Score From Removing Substrings

You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:

- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.

Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.

直接的贪心法，注意删除的时候，一定要用stack，之前用的while循环，会超时。

```python
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        def remove_substr(s, first, second, score, res):
            stack = list()
            for i in s:
                if stack and i == second and stack[-1] == first:
                    stack.pop()
                    res += score
                else:
                    stack.append(i)
            return ''.join(stack), res

        if x > y:
            s, res = remove_substr(s, 'a', 'b', x, res)
            s, res = remove_substr(s, 'b', 'a', y, res)
        else:
            s, res = remove_substr(s, 'b', 'a', y, res)
            s, res = remove_substr(s, 'a', 'b', x, res)
        return res
```
