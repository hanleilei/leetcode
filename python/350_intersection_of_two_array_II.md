# Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
Subscribe to see which companies asked this question.

## 用到的算法很简单，就是字典，没有提示里面的二分查找。。


```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 == [] or nums2 == []:
            return []
        from collections import Counter
        n1 = dict(Counter(nums1))
        n2 = dict(Counter(nums2))

        lt = list(set(n1.keys()) & set(n2.keys()))
        arr = list()
        for i in lt:
            m = min(n1[i], n2[i])
            for j in range(m):
                arr.append(i)
        return arr
```
来个直接字典的：

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        result = []
        for element in nums1:
            if element not in dict:
                dict[element] = 1
            else:
                dict[element] += 1
        for element in nums2:
            if element in dict and dict[element] > 0:
                result.append(element)
                dict[element] -= 1
        return result
```

我的算法：

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        s =  Counter(nums1) & Counter(nums2)
        res = list()
        for k, v in s.items():
            for i in range(v):
                res.append(k)
        return res
```

再来一个简单的：

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return list((c1 & c2).elements())
```
