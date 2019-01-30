# top k frequent elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

###### 看我这抖机灵。。。

```python
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        nums = Counter(nums)
        from heapq import nlargest
        return [i[1] for i in nlargest(k, zip(nums.values(), nums.keys()))]

```
再来一个：

```Python
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter

        d = dict(Counter(nums))
        val = sorted(list(d.values()))[-k:]

        return [i for i, v in d.items() if v in val]
```

用时最少：

```Python
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = dict()  
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        res = sorted(freq, key=lambda x: (-freq[x], x))
        return res[0:k]
```
