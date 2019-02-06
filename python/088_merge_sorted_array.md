# merge sorted array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

## 双指针问题，已经开始假定最大容量，然后开始复制数据。有两种思路：从左往右和从右往左。

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p, q = m-1, n-1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[p+q+1] = nums1[p]
                p = p-1
            else:
                nums1[p+q+1] = nums2[q]
                q = q-1
        nums1[:q+1] = nums2[:q+1]

```



```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        first = nums1[:m]
        second = nums2[:]
        l = r = 0
        while l < m and r < n:
            if first[l] <= second[r]:
                nums1[l + r] = first[l]
                l += 1
            else:
                nums1[l + r] = second[r]
                r += 1

        while l < m:
            nums1[l + r] = first[l]
            l += 1

        while r < n:
            nums1[l + r] = second[r]
            r += 1
```
