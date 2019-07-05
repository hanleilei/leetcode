# partition labels

string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:
```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

## Note:
```
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
```

Build a hashmap to record the last index for each ch.
Then use one pointer l to record the start index of current string, and update r by comparing current ch with that last index in hashmap.

```Python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {}
        res = []
        l, r = 0, 0
        for i,v in enumerate(S):
            d[v] = i
        for i in range(len(S)):
            r = max(r, d[S[i]])
            if i == r:
                res.append(i-l+1)
                l = i+1
        return res
```
