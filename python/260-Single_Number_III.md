# single number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?


还是别用标准库了。

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                s.remove(i)
        return list(s)
```

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        sum = 0
        for num in nums:
            sum ^= num

        # 2. 找到结果中最低位的 1，将数组中的所有元素根据这个位进行分组。
        k = 0
        while sum & 1 == 0:
            k += 1
            sum >>= 1

        # 3. 在每个组中，找到出现两次的元素。
        ans = [0, 0]
        for num in nums:
            if (num >> k) & 1 == 1:
                ans[1] ^= num
            else:
                ans[0] ^= num

        return ans
```
