# monotonic array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

## Example 1

```text
Input: [1,2,2,3]
Output: true
```

## Example 2

```text
Input: [6,5,4,4]
Output: true
```

## Example 3

```text
Input: [1,3,2]
Output: false
```

## Example 4

```text
Input: [1,2,4,5]
Output: true
```

## Example 5

```text
Input: [1,1,1]
Output: true
```

这个太抖机灵了，不太好吧。。

```python
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return sorted(A) == A or sorted(A, reverse=True) == A
```

再来一个简洁的：

这个方法是用了集合的操作：比较巧妙，之前都没有注意到这个：
```Python
s.issubset(t)  
s <= t  
# 测试是否 s 中的每一个元素都在 t 中  

s.issuperset(t)  
s >= t  
# 测试是否 t 中的每一个元素都在 s 中  
```

```Python
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return not {(a>b)-(a<b) for a, b in zip(A[:-1], A[1:])} >= {1, -1}
```

类似的操作还有：

```python
s.union(t)  
s | t  
# 返回一个新的 set 包含 s 和 t 中的每一个元素  

s.intersection(t)  
s & t  
# 返回一个新的 set 包含 s 和 t 中的公共元素  

s.difference(t)  
s - t  
# 返回一个新的 set 包含 s 中有但是 t 中没有的元素  

s.symmetric_difference(t)  
s ^ t  
# 返回一个新的 set 包含 s 和 t 中不重复的元素  

```

或者

```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = True, True
        for i in range(1, len(nums)):
            inc &= nums[i-1] <= nums[i]
            dec &= nums[i-1] >= nums[i]
        return inc or dec
```

再来一个可以遇到False就中断的：

```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        
        isGreat = False
        isLess = False
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                isGreat = True
            if nums[i - 1] < nums[i]:
                isLess = True
            if isGreat and isLess:
                return False
        return True
```
