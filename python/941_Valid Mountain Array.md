# Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:

- `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
- `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

![1](https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png)

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104

完全按照题目的意思：不能有两个数字相等，并且必须有一个山顶，山顶两边的数字都要比山顶小。

```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        left, right = 0, len(arr) - 1
        while left + 1 < len(arr) - 1 and arr[left] < arr[left + 1]:
            left += 1
        while right -1 > 0 and arr[right] < arr[right - 1]:
            right -= 1
        return left == right
```
