# Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

### Note:
1. You may assume the interval's end point is always bigger than its start point.
2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
### Example 1:
```
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
```
### Example 2:
```
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
```
### Example 3:
```Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

```Python
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        end = float('-inf')
        erased = 0
        for i in sorted(intervals, key=lambda i: i.end):
            if i.start >= end:
                end = i.end
            else:
                erased += 1
        return erased
```

```Python
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.end)
        result = 0
        right_most = intervals[0].start
        for x in intervals:
            if x.start >= right_most:
                result += 1
                right_most = max(right_most, x.end)

        return len(intervals) - result
```

需要注意的事情是，示例代码有所更新，现在输入的是一个列表的列表，不再是一个对象的列表：

```Python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals_sort = sorted(intervals, key=lambda x:x[1])
        last = None
        ans = 0
        for it in intervals_sort:
            if not last:
                last = it
            else:
                if it[0] >= last[1]:
                    last = it
                else:
                    ans += 1
        return ans
```
