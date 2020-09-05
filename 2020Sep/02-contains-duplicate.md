# Contains Duplicate III
[[list]]
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:
```
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```
Example 2:
```
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```
Example 3:
```
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```

整个题目就是滑动窗口+字典

```Python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t==0 and len(nums)== len(set(nums)):
            return False
        for i in range(len(nums)):
            for j in range(1,k+1):
                if i+j >= len(nums):break
                if abs(nums[i+j]-nums[i])<=t:return True
        return False
```

再来一个桶排序的方法：

```Python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets = {}
        for i, v in enumerate(nums):
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            bucketNum, offset = (v // t, 1) if t else (v, 0)
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # Remove the bucket which is too far away. Beware of zero t.
                del buckets[nums[i - k] // t if t else nums[i - k]]

        return False

```

再来一个速度比较快的方法：

```Python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or not nums or k <= 0:
            return False
        buckets = {}
        width = t + 1

        for i, n in enumerate(nums):
            buck = n // width
            if buck in buckets:
                return True
            buckets[buck] = n
            if buck+1 in buckets and (buckets[buck+1] - n) <= t:
                return True
            if buck-1 in buckets and (n - buckets[buck-1]) <= t:
                return True
            if i >= k:
                del buckets[nums[i - k] // width]
        return False
```
用的这个 sortedcontainers 确实不错，详细可以参考这个文档 http://www.grantjenks.com/docs/sortedcontainers/ 和这个： https://stackoverflow.com/questions/17857496/built-in-binary-search-tree-in-python， leetcode也将其作为可以默认导入一部分：

In this problem we need to iterate over window of size k+1 and check if there is numbers with difference <=t in this window. What we need to do efficiently is to add and remove elements from our window, and my choice of data structure is BST, which is implemented in SortedList in python. So on each step we have sorted list of elements in this window. Imagine the case:

[1, 3, 7, 12] and new number we need to insert is 10, and t = 2. Then we need to consider range [8,12] and check if we have numbers in our SList in this range. We can do two binary searches here: bisect_left for left boundary and bisect_right for right boundary. Also we need to check if pos1 != len(SList), if this is the case, it means that new number is bigger than bigges number in list + t, so in this case we just put it directly to our list. If pos1 != pos2, this means, that we found some number i our [nums[i] - t, nums[i] + t] range, so we immediatly return True.

Complexity: time complexity is O(n log k), because we do n steps, each one with O(log k) complexity to do binary search, remove and add elements. Space complexity is O(k) to keep our SortedList updated.

https://leetcode.com/problems/contains-duplicate-iii/discuss/824603/Python-SortedList-O(n-log-k)-solution-explained.

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from sortedcontainers import SortedList

        SList = SortedList()
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])   
            pos1 = SortedList.bisect_left(SList, nums[i] - t)
            pos2 = SortedList.bisect_right(SList, nums[i] + t)

            if pos1 != pos2 and pos1 != len(SList): return True

            SList.add(nums[i])

        return False
```
