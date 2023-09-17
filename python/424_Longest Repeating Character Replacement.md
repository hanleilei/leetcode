# Longest Repeating Character Replacement
cd 
[[sliding window]] [[labuladong]]

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Example 1

```text
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

## Example 2

```text
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
```

## Constraints

- 1 <= s.length <= 105
- s consists of only uppercase English letters.
- 0 <= k <= s.length

直接套用 labuladong 的模板：

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        # 记录每个字符出现的次数
        counter = collections.defaultdict(int)
        left = 0
        right = 0
        maxlen = 0
        res = 0

        while left <= right and right < len(s):
            c = s[right]
            right += 1
            counter[c] += 1
            maxlen = max(maxlen, counter[c])

            # 窗口长度减去最大字符出现次数小于 k，表示需要移动左指针
            while right - left - maxlen > k:
                d = s[left]
                left += 1
                counter[d] -= 1

            # 更新最大长度
            res = max(res, right - left)

        return res
```

参考一下 lee215 的方法:

maxf means the max frequency of the same character in the sliding window.
To better understand the solution,
you can firstly replace maxf with max(count.values()),
Now I improve from O(26n) to O(n) using a just variable maxf.

```python
    def characterReplacement(self, s, k):
        maxf = i = 0
        count = collections.Counter()
        for j in range(len(s)):
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])
            if j - i + 1 > maxf + k:
                count[s[i]] -= 1
                i += 1
        return len(s) - i
```
