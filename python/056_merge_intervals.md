# merge intervals

[[sort]]

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

Constraints:

    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4

关键点有两个：

1. 计算之前需要对于数组基于 start 进行排序
2. 求出结果数组最后一个元素的 end 和当前迭代的 end 进行比较，求最大值。

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = list()

        for interval in intervals:
            if not res or res[-1][-1] < interval[0]:
                res.append(interval)
            else:
                res[-1][-1] = max(res[-1][-1], interval[1])
        return res
```

```Python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        size = len(intervals)
        res = list()
        for i in sorted(intervals, key=lambda i: i.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res
```

再来一个速度快的版本：

```Python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        lsts = sorted(intervals, key=lambda x:x.start)
        res = []
        s, e = lsts[0].start, lsts[0].end
        for i in range(1, len(lsts)):
            if lsts[i].start > e:
                res.append(Interval(s, e))
                s = lsts[i].start
                e = lsts[i].end
            elif lsts[i].start <= e and lsts[i].end > e:
                e = lsts[i].end
            else:
                continue
        res.append(Interval(s, e))
        return res

```
