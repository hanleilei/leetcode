# Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:

- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.

Constraints:

- 1 <= arr.length <= 104
- 1 <= arr[i] <= 105

这段代码利用了从右向左遍历的特性，通过维护一个动态更新的最大值，实现了高效、简洁的数组原地修改。适用于需要对数组进行原地变换的题目场景。

- 时间复杂度： O(n) ，只需遍历一次数组。
- 空间复杂度： O(1) ，原地修改数组，无额外空间开销。

```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        curr = -1
        for i in range(n - 1, -1, -1):
            if arr[i] > curr:
                arr[i], curr = curr, arr[i]
            else:
                arr[i] = curr
        
        return arr
```
