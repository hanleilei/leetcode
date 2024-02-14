# Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

## Example 1

```text
Input: nums = [3,2,3]
Output: 3
```

## Example 2

```text
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Constraints

```text
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
```

我只想说，用了collections，解决这类问题，一次性代码写好就ok


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

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

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
```

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
            if d[i] > len(nums) // 2:
                return i
        return -1
```

```python
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
