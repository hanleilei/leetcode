# largest number

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it. Since the result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109

```python
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(i) for i in nums]
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        largest = ''.join(nums)
        return largest.lstrip('0') or '0'
```

上面的python 2 的方法，可以在python 3 中这样写：

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(num) for num in nums]
        strs.sort(key = functools.cmp_to_key(lambda x,y: 1 if (y+x<x+y) else -1), reverse=True)
        return ''.join(strs).lstrip('0') or '0'
```

或写的直观一点：

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp_func(x, y):
            """Sorted by value of concatenated string increasingly."""
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1
            
        # Build nums contains all numbers in the String format.
        nums = [str(num) for num in nums]
        
        # Sort nums by cmp_func decreasingly.
        nums.sort(key = functools.cmp_to_key(cmp_func), reverse = True)
        
        # Remove leading 0s, if empty return '0'.
        return ''.join(nums).lstrip('0') or '0'
```

或者

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b: return 1
            elif a < b: return -1
            else: return 0
        
        strs = [str(num) for num in nums]
        strs.sort(key = functools.cmp_to_key(sort_rule), reverse=True)
        return ''.join(strs).lstrip("0") or "0
```

quick sort:

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self.quicksort(nums, 0, len(nums) - 1)
        return str(int("".join(map(str, nums))))

    def quicksort(self, nums, l, r):
        if l > r:
            return 
        
        pos = self.partition(nums, l, r)
        self.quicksort(nums, l, pos - 1)
        self.quicksort(nums, pos + 1, r)

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
    
    def compare(self, m, n):
        return str(m) + str(n) > str(n) + str(m)
```

selection sort

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums), 0, -1):
            tmp = 0
            for j in range(i):
                if not self.compare(nums[j], nums[tmp]):
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return str(int("".join(map(str, nums))))
    
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
```

insert sort

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            pos, cur = i, nums[i]
            while pos > 0 and not self.compare(nums[pos-1], cur):
                nums[pos] = nums[pos-1]  # move one-step forward
                pos -= 1
            nums[pos] = cur
        return str(int("".join(map(str, nums))))
    
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
```

merge sort

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = self.mergeSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums))))
        
    def mergeSort(self, nums, l, r):
        if l > r:
            return 
        if l == r:
            return [nums[l]]
        mid = l + (r-l)//2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid+1, r)
        return self.merge(left, right)
        
    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if not self.compare(l1[i], l2[j]):
                res.append(l2[j])
                j += 1
            else:
                res.append(l1[i])
                i += 1
        res.extend(l1[i:] or l2[j:])
        return res
    
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
```
