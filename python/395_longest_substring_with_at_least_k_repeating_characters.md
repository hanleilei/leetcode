# longest substring with at least k repeating characters

[[sliding window]] [[divide and conquer]] [[stack]]

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

```text
Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
```

Example 2:

```text
Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
```

来一个stefan的神作。。实在是脑壳疼。。

```python
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
```

来一个容易理解的：

```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        stack = [s]
        ans = 0
        while stack:
            s = stack.pop()
            for c in set(s):
                if s.count(c) < k:
                    stack.extend([z for z in s.split(c)])
                    break
            else:
                ans = max(ans, len(s))
        return ans
```

labuladong

```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        length = 0
        for i in range(1, 27):
            # 限制窗口中只能有 i 种不同字符
            length = max(length, self.longestKLetterSubstr(s, k, i))
        return length

    # 寻找 s 中含有 count 种字符，且每种字符出现次数都大于 k 的子串
    def longestKLetterSubstr(self, s: str, k: int, count: int) -> int:
        # 记录答案
        res = 0
        # 快慢指针维护滑动窗口，左闭右开区间
        left, right = 0, 0
        # 题目说 s 中只有小写字母，所以用大小 26 的数组记录窗口中字符出现的次数
        windowCount = [0] * 26
        # 记录窗口中存在几种不同的字符（字符种类）
        windowUniqueCount = 0
        # 记录窗口中有几种字符的出现次数达标（大于等于 k）
        windowValidCount = 0
        # 滑动窗口代码模板
        while right < len(s):
            # 移入字符，扩大窗口
            c = s[right]
            if windowCount[ord(c) - ord('a')] == 0:
                # 窗口中新增了一种字符
                windowUniqueCount += 1
            windowCount[ord(c) - ord('a')] += 1
            if windowCount[ord(c) - ord('a')] == k:
                # 窗口中新增了一种达标的字符
                windowValidCount += 1
            right += 1

            # 当窗口中字符种类大于 count 时，缩小窗口
            while windowUniqueCount > count:
                # 移出字符，缩小窗口
                d = s[left]
                if windowCount[ord(d) - ord('a')] == k:
                    # 窗口中减少了一种达标的字符
                    windowValidCount -= 1
                windowCount[ord(d) - ord('a')] -= 1
                if windowCount[ord(d) - ord('a')] == 0:
                    # 窗口中减少了一种字符
                    windowUniqueCount -= 1
                left += 1

            # 当窗口中字符种类为 count 且每个字符出现次数都满足 k 时，更新答案
            if windowValidCount == count:
                res = max(res, right - left)
        return res
```


```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        n = len(s)

        # 尝试不同的最大不同字符数（1到26）
        for max_unique in range(1, 27):
            # 记录窗口内每个字符的出现次数
            record = [0] * 26
            left = 0
            diff_count = 0  # 窗口中不同字符的数量
            count_at_least_k = 0  # 出现次数 ≥ k 的字符数

            for right in range(n):
                # 将 s[right] 加入窗口
                add_index = ord(s[right]) - ord('a')
                record[add_index] += 1

                if record[add_index] == 1:
                    diff_count += 1
                if record[add_index] == k:
                    count_at_least_k += 1

                # 如果窗口内不同字符数超过限制，收缩窗口
                while left <= right and diff_count > max_unique:
                    del_index = ord(s[left]) - ord('a')

                    if record[del_index] == k:
                        count_at_least_k -= 1
                    if record[del_index] == 1:
                        diff_count -= 1

                    record[del_index] -= 1
                    left += 1

                # 检查当前窗口是否是有效窗口
                if diff_count == max_unique and diff_count == count_at_least_k:
                    res = max(res, right - left + 1)

        return res
```

总感觉这个题目，可能不太适合滑动窗口。。
