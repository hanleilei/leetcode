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

不能那么直接的sorted了，上二分法：

```Python
class Solution:
    def findMedianSortedArrays(self, A: 'List[int]', B: 'List[int]') -> 'float':
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
```

再来一个最牛逼的算法，算法复杂度为 1O(log(min(M,N))):

```Python
class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        N1, N2 = len(nums1), len(nums2)
        if N1 < N2:
            nums1, N1, nums2, N2 = nums2, N2, nums1, N1
        l, r = 0, N2*2
        while l <= r:
            j = (l + r) >> 1
            i = N1 + N2 - j
            L1 = float('-inf') if i == 0 else nums1[(i-1)>>1]
            L2 = float('-inf') if j == 0 else nums2[(j-1)>>1]
            R1 = float('inf') if i == 2*N1 else nums1[i>>1]
            R2 = float('inf') if j == 2*N2 else nums2[j>>1]
            if L1 > R2: l = j + 1
            elif L2 > R1: r = j - 1
            else:
                return (max(L1, L2) + min(R1, R2))/2
```
