# Longest Repeating Character Replacement

[[slidingwindow]]

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

        n = len(s)
        counter = [0] * 26  # 用数组比字典更快
        left, right = 0, 0
        max_count = 0
        max_len = 0

        for right in range(n):
            # 扩展右边界
            idx = ord(s[right]) - ord('A')
            counter[idx] += 1
            max_count = max(max_count, counter[idx])

            # 如果当前窗口长度 - 最大字符数 > k，需要收缩窗口
            while right - left + 1 - max_count > k:
                left_idx = ord(s[left]) - ord('A')
                counter[left_idx] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
```

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        windowCharCount = [0] * 26
        windowMaxCount = 0
        res = 0

        while right < len(s):
            c = ord(s[right]) - ord('A')
            windowCharCount[c] += 1
            windowMaxCount = max(windowMaxCount, windowCharCount[c])
            right += 1

            while right - left - windowMaxCount > k:
                windowCharCount[ord(s[left]) - ord('A')] -= 1
                left += 1
            # 经过收缩后，此时一定是一个合法的窗口
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
        res = 0
        count = {}
        left = 0
        maxf = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(maxf, count[s[right]])
            while right - left + 1 - maxf > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
```
