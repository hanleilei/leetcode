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

再来看大佬的，解决了全部的追加问题，尤其是第三个，需要考虑从硬盘里面加载数据：

✔️ Approach 1: HashMap

Using HashMap to store occurrences of elements in the nums1 array.
Iterate x in nums2 array, check if cnt[x] > 0 then append x to our answer and decrease cnt[x] by one.
To optimize the space, we ensure len(nums1) <= len(nums2) by swapping nums1 with nums2 if len(nums1) > len(nums2).

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)

        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans
```

Complexity:

Time: O(M + N), where M <= 1000 is length of nums1 array, N <= 1000 is length of nums2 array.
Space: O(min(M, N))

✔️ Approach 2: Sort then Two Pointers

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans
```

Complexity:

Time: O(MlogM + NlogN), where M <= 1000 is length of nums1 array, N <= 1000 is length of nums2 array.
Extra Space (without counting output as space): O(sorting)

✔️ Follow-up Question 1: What if the given array is already sorted? How would you optimize your algorithm?

```
Approach 2 is the best choice since we skip the cost of sorting.
So time complexity is O(M+N) and the space complexity is O(1).
```

✔️ Follow-up Question 2: What if nums1's size is small compared to nums2's size? Which algorithm is better?

```
Approach 1 is the best choice.
Time complexity is O(M+N) and the space complexity is O(M), where M is length of nums1, N is length of nums2.
```

✔️ Follow-up Question 3: What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

```
If nums1 fits into the memory, we can use Approach 1 which stores all elements of nums1 in the HashMap. Then, we can sequentially load and process nums2.
If neither nums1 nor nums2 fits into the memory, we split the numeric range into numeric sub-ranges that fit into the memory.
We modify Approach 1 to count only elements which belong to the given numeric sub-range.
We process each numeric sub-ranges one by one, util we process all numeric sub-ranges.
For example:
Input constraint:
1 <= nums1.length, nums2.length <= 10^10.
0 <= nums1[i], nums2[i] < 10^5
Our memory can store up to 1000 elements.
Then we split numeric range into numeric sub-ranges [0...999], [1000...1999], ..., [99000...99999], then call Approach 1 to process 100 numeric sub-ranges.
```
