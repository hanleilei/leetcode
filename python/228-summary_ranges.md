# summary ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


#### 坦白的讲，我没有做出来，看明白了下面的算法，https://leetcode.com/discuss/42199/6-lines-in-python 转换为二维数组的方式。后面的几个算法都很简洁。。
```python
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]
```
```python
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        x, size = 0, len(nums)
        ans = []
        while x < size:
            c, r = x, str(nums[x])
            while x + 1 < size and nums[x + 1] - nums[x] == 1:
                x += 1
            if x > c:
                r += "->" + str(nums[x])
            ans.append(r)
            x += 1
        return ans
```

```python
def summaryRanges(self, nums):
    ranges, r = [], []
    for n in nums:
        if n-1 not in r:
            r = []
            ranges += r,
        r[1:] = n,
    return ['->'.join(map(str, r)) for r in ranges]
```

```python
def summaryRanges(self, nums):
    ranges = r = []
    for n in nums:
        if `n-1` not in r:
            r = []
            ranges += r,
        r[1:] = `n`,
    return map('->'.join, ranges)
```
