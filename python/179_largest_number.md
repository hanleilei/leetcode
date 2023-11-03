# largest number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

比较的是字符串，然后用的是python2 的cmp方法，比较两个字符串连接后的大小

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
        return ''.join(strs)
```
