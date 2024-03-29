# insert interval

[[interval overlapping]]

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

使用的方法非常简单，先将左边和右边的数组单独区分出来，然后在计算中间的合并的部分。

```Python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s, e = newInterval.start, newInterval.end
        begin = list()
        end = list()

        for i in intervals:
            if s > i.end:
                begin.append(i)
            elif e < i.start:
                end.append(i)
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return begin + [Interval(s, e)] + end
```

python3

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        begin = list()
        end = list()

        for i in intervals:
            if s > i[1]:
                begin.append(i)
            elif e < i[0]:
                end.append(i)
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return begin + [[s, e]] + end
```

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = intervals + [newInterval]
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for i in intervals[1:]:
            if i[0] > res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res
```
