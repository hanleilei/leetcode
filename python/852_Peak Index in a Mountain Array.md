# Peak Index in a Mountain Array

[[binarysearch]]

You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.

非常经典的二分法题目，这道题的关键在于如何判断 mid 是在山峰的左边还是右边。
如果 arr[mid] > arr[mid + 1]，那么 mid 一定在山峰的右边，因为山峰的右边是递减的。
如果 arr[mid] < arr[mid + 1]，那么 mid 一定在山峰的左边，因为山峰的左边是递增的。

来自于mit 6.006 课程的第一个课。

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 2
        while left + 1 < right:
            mid = (right + left) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid
        return right
```

往常我们使用「二分」进行查值，需要确保序列本身满足「二段性」：当选定一个端点（基准值）后，结合「一段满足 & 另一段不满足」的特性来实现“折半”的查找效果。

但本题求的是峰顶索引值，如果我们选定数组头部或者尾部元素，其实无法根据大小关系“直接”将数组分成两段。

但可以利用题目发现如下性质：由于 arr 数值各不相同，因此峰顶元素左侧必然满足严格单调递增，峰顶元素右侧必然不满足。

因此 以峰顶元素为分割点的 arr 数组，根据与 前一元素/后一元素 的大小关系，具有二段性：

峰顶元素左侧满足 `arr[i−1]<arr[i]` 性质，右侧不满足
峰顶元素右侧满足 `arr[i]>arr[i+1]` 性质，左侧不满足
因此我们可以选择任意条件，写出若干「二分」版本。

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #  根据 arr[i-1] < arr[i] 在 [1,n-1] 范围内找值
        #  峰顶元素为符合条件的最靠近中心的元素
        n = len(arr)
        l, r = 1, n - 1
        while l < r:
            mid = (l + r + 1) >> 1  # 等价于 (l + r + 1) // 2
            if arr[mid - 1] < arr[mid]:
                l = mid
            else:
                r = mid - 1
        return r
```

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 根据 arr[i] > arr[i+1] 在 [0,n-2] 范围内找值
        # 峰顶元素为符合条件的最靠近中心的元素值
        n = len(arr)
        l, r = 0, n - 2
        while l < r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return r
```

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 根据 arr[i-1] > arr[i] 在 [1,n-1] 范围内找值
        # 峰顶元素为符合条件的最靠近中心的元素的前一个值
        n = len(arr)
        l, r = 1, n - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid - 1] > arr[mid]:
                r = mid
            else:
                l = mid + 1
        return r - 1
```

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 根据 arr[i] < arr[i+1] 在 [0,n-2] 范围内找值
        # 峰顶元素为符合条件的最靠近中心的元素的下一个值
        n = len(arr)
        l, r = 0, n - 2
        while l < r:
            mid = (l + r + 1) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid
            else:
                r = mid - 1
        return r + 1

```
