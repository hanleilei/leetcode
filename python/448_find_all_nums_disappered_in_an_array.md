# find all numbers disappeared in an array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

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
