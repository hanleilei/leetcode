# Longest Square Streak in an Array

You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

```text
Input: nums = [4,3,6,16,8,2]
Output: 3
Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.
```

Example 2:

```text
Input: nums = [2,3,5,6,7]
Output: -1
Explanation: There is no square streak in nums so return -1.
```

Constraints:

```text
2 <= nums.length <= 10**5
2 <= nums[i] <= 10**5
```

直接翻译题目含义，得到一个

```python
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        nums = sorted(nums, reverse=True)
        res = list()
        while nums:
            v = list()
            t = nums.pop()
            if t not in s:
                break
            v.append(t)
            while t * t in s:
                t = t * t
                s.remove(t)
                v.append(t)
            res.append(v)
        res.sort(key=len)

        return len(res[-1]) if len(res[-1]) > 1 else -1
```

这样，可以直接得到最终的数组究竟是什么样的序列，也可以得到长度。问题是只要求得到长度，而不是序列，所以：

```python
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)         # 利用集合快速判断
        max_streak = 0        # 跟踪最长序列的长度

        for num in sorted(nums):  # 小到大遍历，避免 pop 操作
            if num not in s:      # 如果已经处理过该数，跳过
                continue

            streak_len = 0        # 当前序列长度
            while num in s:       # 循环构建平方序列
                streak_len += 1
                s.remove(num)     # 避免重复计算
                num *= num        # 计算平方
            
            max_streak = max(max_streak, streak_len)  # 更新最长序列长度

        return max_streak if max_streak > 1 else -1
```

扎心的事情：这写所谓的去重操作，对速度并没有什么影响。。也许这是测试平台的问题。

再来一个速度最快的优化版本：

```python
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        num_set = set(nums)
        max_length = 0

        for num in nums:
            length = 0
            current = num
            while current in num_set:
                length += 1
                current = current ** 2
            if length > 1:
                max_length = max(max_length, length)
        return max_length if max_length > 1 else -1
```

上面两段代码的差别核心在于这一句：`nums = sorted(set(nums))`，对于去重之后的结合排序。同样，需要把上面的代码`for num in sorted(nums):`变成`for num in sorted(s):`就可以了。
