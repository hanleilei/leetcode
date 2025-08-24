# sort colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

三路快排，荷兰国旗问题

```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l, i, r = 0, 0, len(nums) -1
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                i += 1
                l += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
```

```python
class Solution:
    def sortColors(self, a: List[int]) -> None:
        a[:]=chain(*starmap(repeat,sorted(Counter(a).items())))
```

```python
class Solution:
    def sortColors(self, a: List[int]) -> None:
        a[:]=[0]*(c:=Counter(a))[0]+[1]*c[1]+[2]*c[2]
```

```python
class Solution:
    def sortColors(self, a: List[int]) -> None:
        z = o = t = -1
        for v in a:
            a[t:=t+1] = 2
            if v < 2:
                a[o:=o+1] = 1
                if v < 1:
                    a[z:=z+1] = 0
```

