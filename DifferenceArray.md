# 差分数组

```python
class Solution:
    def getModifiedArray(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        diff = [0] * len(nums)

        # 构造差分数组
        diff[0] = nums[0]
        for i in range(1, len(nums)):
            diff[i] = nums[i] - nums[i - 1]

        for i, j, val in operations:
            diff[i] += val
            if j + 1 < len(diff):
                diff[j+1] -= val

        res = [0] * len(diff)
        # 根据差分数组构造结果数组
        res[0] = diff[0]
        for i in range(1, len(diff)):
            res[i] = res[i - 1] + diff[i]
        return res
```
