# Diagonal Traverse II

Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

## Example 1

![](https://assets.leetcode.com/uploads/2020/04/08/sample_1_1784.png)

```text
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
```

## Example 2

![](https://assets.leetcode.com/uploads/2020/04/08/sample_2_1784.png)

```text
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

## Constraints

```text
1 <= nums.length <= 105
1 <= nums[i].length <= 105
1 <= sum(nums[i].length) <= 105
1 <= nums[i][j] <= 105
```

这类问题的通行方法，很巧妙。。

```python
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = list()
        for i, r in enumerate(nums):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i+j].append(a)
        return [a for r in res for a in reversed(r)]
```
