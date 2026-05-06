# Reverse Pairs

[[tree]]

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

    0 <= i < j < nums.length and
    nums[i] > 2 * nums[j].

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 *1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2* 1

Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 *1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2* 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

Constraints:

    1 <= nums.length <= 5 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1

```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        tb, res = [], 0
        for n in reversed(nums):
            res += bisect.bisect_left(tb, n)
            n2 = 2 * n
            idx = bisect.bisect_left(tb, n2)
            tb.insert(idx, n2)
        return res
```

```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sl = SortedList()
        ans = 0
        for num in nums:
            i = sl.bisect_right(2 * num)
            ans += len(sl) - i
            sl.add(num)
        return ans
```

BIT (Binary Indexed Tree, also called Fenwick Tree):

```python
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def query(self, a):
        res = 0
        while a > 0:
            res += self.tree[a]
            a -= a & -a
        return res

    def update(self, a, add):
        while a <= self.n:
            self.tree[a] += add
            a += a & -a

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        tmp = []
        for u in nums:
            tmp.append(u)
            tmp.append(u * 2)
        rank = {k:i+1 for i,k in enumerate(sorted(set(tmp)))}
        n1 = len(rank)
        b = BIT(n1)
        ans = 0
        for a in reversed(nums):
            J2 = rank[a * 2]
            J = rank[a]
            ans += b.query(J - 1)
            b.update(J2, 1)
        return ans
```

merge sort:

```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arr, start, end):
            if start == end:
                return

            mid = start + ((end - start) >> 1)

            merge_sort(arr, start, mid)
            merge_sort(arr, mid + 1, end)

            i, j = start, mid + 1
            while i <= mid and j <= end:
                if arr[i] > 2 * arr[j]:
                    self.res += mid - i + 1
                    j += 1
                else:
                    i += 1

            i, j, index = start, mid + 1, 0
            temp = [0] * (end - start + 1)
            while i <= mid and j <= end:
                if arr[i] < arr[j]:
                    temp[index] = arr[i]
                    i += 1
                else:
                    temp[index] = arr[j]
                    j += 1
                index += 1

            while i <= mid:
                temp[index] = arr[i]
                i += 1
                index += 1

            while j <= end:
                temp[index] = arr[j]
                j += 1
                index += 1

            index = 0
            for i in range(start, end + 1):
                arr[i] = temp[index]
                index += 1

        self.res = 0
        merge_sort(nums, 0, len(nums) - 1)

        return self.res
```

简洁，但效率不高：

```python
class Solution:
    def reversePairs(self, nums):
        def mergeSort(left, right):
            if left >= right:
                return 0
            mid = left + (right - left) // 2
            res = mergeSort(left, mid) + mergeSort(mid + 1, right)
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] / 2.0 > nums[j]:
                    j += 1
                res += j - (mid + 1)
            # 对当前区间进行排序
            nums[left:right + 1] = sorted(nums[left:right + 1])
            return res
        
        return mergeSort(0, len(nums) - 1)
```
