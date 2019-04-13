# Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

## Example 1:
```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

### Note:

1. S will have length in range [1, 500].
2. S will consist of lowercase letters ('a' to 'z') only.

```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        from collections import defaultdict
        d = defaultdict(list)

        for i in range(len(S)):
            d[S[i]].append(i)

        ans = []
        l, t = 0, 0
        for m in d.values():
            if m[0] <= t and m[-1] > t :
                t = m[-1]
            if m[0] > t:
                ans.append(t-l+1)
                l, t = m[0], m[-1]
        ans.append(t-l+1)

        return ans
```

```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        from collections import defaultdict
        d = defaultdict(list)

        for i in range(len(S)):
            d[S[i]].append(i)

        res = []
        l , r = 0, 0
        for i, char in enumerate(S):
            r = max(r, d[char][-1])
            if i == r:
                res.append(r-l+1)
                l = r + 1
        return res
```

mark: 2019/04/13 目前还是遇到新题，medium很多还是想不出来最优解，大概思路是有，但是代码还是糊了。
