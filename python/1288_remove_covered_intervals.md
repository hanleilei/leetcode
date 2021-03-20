# remove covered interval

Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

###  Example 1:

```
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
```
### Example 2:
```
Input: intervals = [[1,4],[2,3]]
Output: 1
```
### Example 3:
```
Input: intervals = [[0,10],[5,12]]
Output: 2
```
### Example 4:
```
Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2
```
### Example 5:
```
Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1
```

Constraints:
```
1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= intervals[i][0] < intervals[i][1] <= 10^5
All the intervals are unique.
```
先对于子数组的第一个元素进行排序，然后还要更新第二个元素的最大值，可能是更新了测试用例，很多的答案都是错误的，对于 这个例子
```
[[1,4],[1,2],[3,4]]
```
很多都是得到错误的结果。
```Python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = right = 0
        intervals.sort(key=lambda a: (a[0], -a[1]))
        for i, j in intervals:
            res += j > right
            right = max(right, j)
        return res
```


To efficiently encapsulate applications and their dependencies into a set of clean, minimal layers
