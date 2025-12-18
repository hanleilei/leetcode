# Kth Largest Element in an Array

[[heap]]

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

```text
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

Example 2:

```text
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

Constraints

```text
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
```

下面是caikehe的解法全集。但是其中也就最后一个使用快速排序的解法最有价值，其次使用堆排序的解法。

```python
# O(nlgn) time
def findKthLargest1(self, nums, k):
    return sorted(nums, reverse=True)[k-1]

# O(nk) time, bubble sort idea, TLE
def findKthLargest2(self, nums, k):
    for i in xrange(k):
        for j in xrange(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                # exchange elements, time consuming
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums[len(nums)-k]

# O(nk) time, selection sort idea
def findKthLargest3(self, nums, k):
    for i in xrange(len(nums), len(nums)-k, -1):
        tmp = 0
        for j in xrange(i):
            if nums[j] > nums[tmp]:
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return nums[len(nums)-k]

# O(k+(n-k)lgk) time, min-heap
def findKthLargest4(self, nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for _ in xrange(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)

# O(k+(n-k)lgk) time, min-heap        
def findKthLargest5(self, nums, k):
    return heapq.nlargest(k, nums)[k-1]

# O(n) time, quick selection
def findKthLargest(self, nums, k):
    # convert the kth largest to smallest
    return self.findKthSmallest(nums, len(nums)+1-k)

def findKthSmallest(self, nums, k):
    if nums:
        pos = self.partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return self.findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return self.findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]

# choose the right-most element as pivot   
def partition(self, nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low
```

这个问题，第一反应的答案就是：quick select或者heap：

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums)-1, k)

    def quickSelect(self, nums, start, n, k): # quick select
        pos = self.partition(nums, start, n)
        if pos == k-1:
            return nums[pos]
        elif pos >= k:
            return self.quickSelect(nums, start, pos - 1, k)
        return self.quickSelect(nums, pos + 1, n, k)

    def partition(self, nums, left, right):
        pivot = nums[right] # pick the last one as pivot
        i = left
        for j in range(left, right): # left to right -1
            if nums[j] > pivot: # the larger elements are in left side
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right] # swap the i and the last element
        return i
```

或者：

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
```
