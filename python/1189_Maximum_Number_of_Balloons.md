# Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

```
Input: text = "nlaebolko"
Output: 1
```

Example 2:

```
Input: text = "loonbalxballpoon"
Output: 2
```

Example 3:

```
Input: text = "leetcode"
Output: 0
```

Constraints:

```
1 <= text.length <= 104
text consists of lower case English letters only.
```

直接上counter就行了。

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        c = Counter(text)
        b = Counter("balloon")
        return min([c[i] // b[i] for i in b])
```

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = []
        d = defaultdict(int)
        for t in text:
            if t in "banlo":
                d[t] += 1
        for k, v in d.items():
            if k in "ban":
                ans.append(v)
            elif k in "lo":
                ans.append(v // 2)
        return min(ans) if len(ans)== 5 else 0
```
