# Sort Array By Parity

[[2points]]

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

## Example 1

```text
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

## Example 2

```text
Input: nums = [0]
Output: [0]
```

## Constraints

- 1 <= nums.length <= 5000
- 0 <= nums[i] <= 5000

双指针问题

```python
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return list(filter(lambda x: x % 2==0, A)) + list(filter(lambda y: y % 2 , A))

```
再来一个快速的版本
```python
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evens = [A for A in A if A%2 == 0]
        odds = [A for A in A if A%2 == 1]
        return evens + odds

```
自己想出来的：

```python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd, even = list(), list()
        for i in A:
            if i % 2 == 1:
                odd.append(i)
            else:
                even.append(i)
        return even + odd
```
再来一个单行的：

```Python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x% 2)
```

在原来的数组上修改，这样的空间复杂度就是O(1), 空间复杂度就是O(n)。

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
        return nums
```
