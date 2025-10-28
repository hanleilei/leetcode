# find all numbers disappeared in an array

[[hashtable]]

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

理解题目，从 1 到数组长度范围内，然后用集合解决。

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))
```

遍历数组的方式解决：

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]
```

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        for i in nums:
            res[i-1] = 1

        return [i+1 for i in range(len(res)) if res[i] == 0]
```

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [i for i in range(1, len(nums) + 1) if i not in c]
```
