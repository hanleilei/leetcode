# Russian Doll Envelopes

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

### Note:
Rotation is not allowed.

### Example:
```
Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```



```Python
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        import bisect

        # https://leetcode.com/problems/russian-doll-envelopes/discuss/157840/Concise-8-line-Python-O(nlogn)-solution-(easy-to-understand)
        if not envelopes:
            return 0
        dp = []
        for i,j in enumerate(sorted(envelopes, key=lambda x:(x[0], -x[1]))):
            idx = bisect.bisect_left(dp, j[1])
            if idx == len(dp):
                dp += [j[1]]
            else:
                dp[idx] = j[1]
        return len(dp)
```

```Python
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        import bisect

        # https://leetcode.com/problems/russian-doll-envelopes/discuss/157840/Concise-8-line-Python-O(nlogn)-solution-(easy-to-understand)

        res = []
        for _, n in sorted(envelopes, key = lambda env : (env[0], -env[1])):
            index = bisect.bisect_left(res, n)
            if index == len(res):
                res.append(n)
            else:
                res[index] = n
        return len(res)
```
