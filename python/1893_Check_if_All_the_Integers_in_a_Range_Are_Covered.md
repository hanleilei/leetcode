## Check if All the Integers in a Range Are Covered

You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

Example 1:

```
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.
```

Example 2:

```
Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: false
Explanation: 21 is not covered by any range.
```

Constraints:

```
1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50
```

智障都能想得到的方法：集合。

```python
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = set()
        for start, end  in ranges:
            nums = nums.union(set(range(start, end +1)))
        return set(range(left, right + 1)).issubset(nums)
```

来一个 Lee215 的方法：

```
all values in range(left, right + 1),
should be in any one interval (l, r).


Complexity
Time O((right - left) * n),
where n = ranges.length
Space O(1)
```

```python
class Solution:
    def isCovered(self, ranges, left, right):
        return all(any(l <= i <= r for l, r in ranges) for i in range(left, right + 1))
```

Lee215 有点 stefan 的风格了。。

在来一个先排序，在扫描的方法：

```python
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for lt, rt in ranges:
            if lt > left: return False
            left = max(left, rt+1)
            if left > right: return True
        return False
```
