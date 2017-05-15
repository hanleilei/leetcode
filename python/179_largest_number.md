# largest number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

### 比较的是字符串，然后用的是python2 的cmp方法，比较两个字符串连接后的大小

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
