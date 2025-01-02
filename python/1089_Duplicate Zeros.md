# Duplicate Zeros

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9

Start from the back and adjust items to correct locations. If item is zero then duplicate it.

original arr:
[1, 0, 2, 0, 3, 0]
num of zeros so far:
[0, 1, 1, 2, 2, 3]
arr with duplicate 0s (Θ means a duplicate 0):
[1, Θ, 0, 2, Θ, 0, 3, Θ, 0]
arr after cutoff
[1, Θ, 0, 2, Θ, 0]

```python
# Every number in the original array is shifted to the right by the number of zeros so far.
# Because of the cutoff, we are going to check if the new position of the number is inside the array.
if i + zeroes < n:
```

```text
# This is checking if there is a Θ that should be included.
if arr[i] == 0:
  zeroes -= 1
  if i + zeroes < n:
    arr[i + zeroes] = 0
```

```python
class Solution:
    def duplicateZeros(self, A: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = A.count(0)
        n = len(A)
        for i in range(n - 1, -1, -1):
            print(A)
            if i + zeros < n:
                A[i + zeros]= A[i]
            if A[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    A[i + zeros] = 0
```
