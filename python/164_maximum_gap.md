# maximum gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

### Example 1:
```
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
```
### Example 2:
```
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
```

### Note:

1. You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
2. Try to solve it in linear time/space.

下面的方法是使用radix sort，基数排序
```Python
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        radix = 10
        """a为整数列表， radix为基数"""
        K = int(math.ceil(math.log(max(nums)+1, radix))) # 用K位数可表示任意整数
        for i in range(1, K+1): # K次循环
            bucket = [[] for i in range(radix)] # 不能用 [[]]*radix，否则相当于开了radix个完全相同的list对象
            for val in nums:
                bucket[val%(radix**i)//(radix**(i-1))].append(val) # 獲得整數第K位數字 （從低到高）
            del nums[:]
            for each in bucket:
                nums.extend(each) # 桶合并
        gap = 0
        for i in range(1, len(nums)):
            gap = max(gap, nums[i] - nums[i-1])
        return gap
```

其实，可以用很简单的排序：


```Python
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i-1])
        return res
```

性能反而更好, 但是达不到要求的O(N)
