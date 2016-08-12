# Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

###### 对列表的操作
```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        lst = sorted(nums1)

        if len(lst)%2==1:
            return lst[len(lst)//2]
        else:
            return (lst[len(lst)//2]+lst[len(lst)//2-1])/2.0


```
