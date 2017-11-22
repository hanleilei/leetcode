# merge intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

关键点有两个：
1. 计算之前需要对于数组基于start进行排序
2. 求出结果数组最后一个元素的end和当前迭代的end进行比较，求最大值。

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
