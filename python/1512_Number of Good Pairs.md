# Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

## Example 1

```text
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
```

## Example 2

```text
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
```

## Example 3

```text
Input: nums = [1,2,3]
Output: 0
```

Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

没什么技巧。。就是如果有N个元素相同符合要求，那么结果就是`0+1+...+N-1` 个满足条件。

```python
class Solution:
    def numIdenticalPairs(self, A: List[int]) -> int:
        res = 0
        count = [0] * 101
        for a in A:
            res += count[a]
            count[a] += 1
        return res
```

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for k, v in counter.items():
            res += (v * (v - 1) // 2)
        return res
```
