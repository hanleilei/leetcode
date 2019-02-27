# Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

#### 我只想说，用了collections，解决这类问题，一次性代码写好就ok


```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        d = Counter(nums)
        for k in d.keys():
            if d[k]> len(nums) * 0.5:
                return k
```

再来一些算法：

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###排序后处在中间的一定是众数
        nums.sort()
        return nums[len(nums)//2]


        ###摩尔投票方法
        count=0
        now=None
        max=len(nums)//2
        for i in nums:
            if count==0:
                now=i
                count=1
            elif count>max:
                return now
            elif i==now:
                count+=1
            else:
                count-=1
        return now



        ###这是自己的版本
        rec={}
        max=len(nums)/2
        for i in nums:
            if i in rec:
                rec[i]+=1
            else:
                rec[i]=1
            if rec[i]>max:
                return i
            # print (rec)

```
