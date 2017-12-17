# single number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?


```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter, defaultdict
        d1 = Counter(nums)
        d2 = defaultdict(list)
        for k,v in d1.most_common((len(nums)+2)/2-2):
            d2[k].append(v)
        return list(set(d1.keys()) - set(d2.keys()))
```
上面的标准库的方法实在是让人看起来不舒服，虽然也可以实现：

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d  = dict()

        for i in nums:
            if i in d:
                d.pop(i)
            else:
                d[i] = 1
        return list(d.keys())
```
