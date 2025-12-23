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
            return (lst[len(lst)//2]+lst[len(lst)//2-1]) / 2.0
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

再来一个stefan大大的算法，自制的二分查找：

```Python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) // 2
            if after-i-1 < 0 or a[i] >= b[after-i-1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0
```

再来一个自制的算法：

1. 先对两个数组求逆；
2. 每次pop出最后一个元素比较，小的元素放到目标列表中。
3. 再来判断哪个列表为空，把不为空的别表求逆序，然后放入目标队列末尾
4. 求中位数。

完全就是 merge 2 sorted array 的方法，加上最后的求中位数的方法。和第21题有点类似。

```Python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        d = list()

        s1 = nums1[::-1]
        s2 = nums2[::-1]

        while s2 and s1:
            if s1[-1] >= s2[-1]:
                d.append(s2.pop())
            elif s1[-1] < s2[-1]:
                d.append(s1.pop())
        d.extend(s1[::-1]) if not len(s2) else d.extend(s2[::-1])
        if len(d) % 2:
            return d[len(d)//2]
        else:
            return (d[len(d)//2] + d[len(d)//2 - 1]) /2
```

总结：

这道题让我们求两个有序数组的中位数，而且限制了时间复杂度为O(log (m+n))，看到这个时间复杂度，自然而然的想到了应该使用二分查找法来求解。但是这道题被定义为Hard也是有其原因的，难就难在要在两个未合并的有序数组之间使用二分法，如果这道题只有一个有序数组，让我们求中位数的话，估计就是个Easy题。那么我们可以将两个有序数组混合起来成为一个有序数组再做吗，图样图森破，这个时间复杂度限制的就是告诉你金坷垃别想啦。那么我们还是要用二分法，而且是在两个数组之间使用，感觉很高端啊。那么回顾一下中位数的定义，如果某个有序数组长度是奇数，那么其中位数就是最中间那个，如果是偶数，那么就是最中间两个数字的平均值。这里对于两个有序数组也是一样的，假设两个有序数组的长度分别为m和n，由于两个数组长度之和 m+n 的奇偶不确定，因此需要分情况来讨论，对于奇数的情况，直接找到最中间的数即可，偶数的话需要求最中间两个数的平均值。为了简化代码，不分情况讨论，我们使用一个小trick，我们分别找第 (m+n+1) / 2 个，和 (m+n+2) / 2 个，然后求其平均值即可，这对奇偶数均适用。加入 m+n 为奇数的话，那么其实 (m+n+1) / 2 和 (m+n+2) / 2 的值相等，相当于两个相同的数字相加再除以2，还是其本身。

好，这里我们需要定义一个函数来在两个有序数组中找到第K个元素，下面重点来看如何实现找到第K个元素。首先，为了避免产生新的数组从而增加时间复杂度，我们使用两个变量i和j分别来标记数组nums1和nums2的起始位置。然后来处理一些corner cases，比如当某一个数组的起始位置大于等于其数组长度时，说明其所有数字均已经被淘汰了，相当于一个空数组了，那么实际上就变成了在另一个数组中找数字，直接就可以找出来了。还有就是如果K=1的话，那么我们只要比较nums1和nums2的起始位置i和j上的数字就可以了。难点就在于一般的情况怎么处理？因为我们需要在两个有序数组中找到第K个元素，为了加快搜索的速度，我们要使用二分法，那么对谁二分呢，数组么？其实要对K二分，意思是我们需要分别在nums1和nums2中查找第K/2个元素，注意这里由于两个数组的长度不定，所以有可能某个数组没有第K/2个数字，所以我们需要先check一下，数组中到底存不存在第K/2个数字，如果存在就取出来，否则就赋值上一个整型最大值。如果某个数组没有第K/2个数字，那么我们就淘汰另一个数组的前K/2个数字即可。举个例子来说吧，比如 nums1 = {3}，nums2 = {2, 4, 5, 6, 7}，K=4，我们要找两个数组混合中第4个数字，那么我们分别在 nums1 和 nums2 中找第2个数字，我们发现 nums1 中只有一个数字，不存在第二个数字，那么 nums2 中的前2个数字可以直接跳过，为啥呢，因为我们要求整个混合数组的第4个数字，不管 nums1 中的那个数字是大是小，第4个数字绝不会出现在 nums2 的前两个数字中，所以可以直接跳过。

有没有可能两个数组都不存在第K/2个数字呢，这道题里是不可能的，因为我们的K不是任意给的，而是给的m+n的中间值，所以必定至少会有一个数组是存在第K/2个数字的。最后就是二分法的核心啦，比较这两个数组的第K/2小的数字midVal1和midVal2的大小，如果第一个数组的第K/2个数字小的话，那么说明我们要找的数字肯定不在nums1中的前K/2个数字，所以我们可以将其淘汰，将nums1的起始位置向后移动K/2个，并且此时的K也自减去K/2，调用递归。反之，我们淘汰nums2中的前K/2个数字，并将nums2的起始位置向后移动K/2个，并且此时的K也自减去K/2，调用递归即可.
