# Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:

Input: matrix = [[-5]], k = 1
Output: -5

Constraints:

```text
n == matrix.length == matrix[i].length
1 <= n <= 300
-10**9 <= matrix[i][j] <= 10**9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n**2
```

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

难点就只是如何将数组变得扁平, 然后排序即可。

```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return sorted(sum(matrix,[]))[k-1]
```

但是这个方法，时间复杂度是O(nlogn)，不符合题目要求。再来一个二分法：

```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        count += 1
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
```

再来一个更高效的：

```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        
        def count_less_or_equal(target):
            count = 0
            row, col = n - 1, 0  # 从左下角开始
            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    count += row + 1  # 当前列中<=target的元素数量
                    col += 1  # 向右移动
                else:
                    row -= 1  # 向上移动
            return count
        
        while left < right:
            mid = left + (right - left) // 2
            count = count_less_or_equal(mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
```
