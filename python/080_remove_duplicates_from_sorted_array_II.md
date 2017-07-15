# remove duplicates from sorted array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question.

### 下面是我想到的答案，不够优雅，但是在我自己的机器上工作，网页上提交就是不过。。。奇了怪了


```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        existed = list()
        d = dict()
        for i in nums:
            if i in d.keys():
                d[i]+= 1
            else:
                d[i]=1
            if d[i] <= 2:
                existed.append(i)
        return len(existed)
```

这个是网上的票最多的答案，我是想不出来这么优雅的解答：

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
```

再看了这个，顿时感觉自己Low爆了：

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2: return len(nums)

        end = 2
        for n in nums[2:]:
            if n > nums[end-2]:
                nums[end] = n
                end += 1

        return end
```
