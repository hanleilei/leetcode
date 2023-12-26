# Sum of All Odd Length Subarrays

[[prefix sum]]

Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.

 

## Example 1

```text
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
```

## Example 2

```text
Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
```

##  Example 3

```text
Input: arr = [10,11,12]
Output: 66
```

## Constraints

```text
1 <= arr.length <= 100
1 <= arr[i] <= 1000
```

## Follow up

```text
Could you solve this problem in O(n) time complexity?
```

先来一个lee215的方法：

Consider the subarray that contains A[i],
we can take 0,1,2..,i elements on the left,
from A[0] to A[i],
we have i + 1 choices.

we can take 0,1,2..,n-1-i elements on the right,
from A[i] to A[n-1],
we have n - i choices.

In total, there are k = (i + 1) * (n - i) subarrays, that contains A[i].
And there are (k + 1) / 2 subarrays with odd length, that contains A[i].
And there are k / 2 subarrays with even length, that contains A[i].

A[i] will be counted ((i + 1) * (n - i) + 1) / 2 times for our question.


Example of array [1,2,3,4,5]
1 2 3 4 5 subarray length 1
1 2 X X X subarray length 2
X 2 3 X X subarray length 2
X X 3 4 X subarray length 2
X X X 4 5 subarray length 2
1 2 3 X X subarray length 3
X 2 3 4 X subarray length 3
X X 3 4 5 subarray length 3
1 2 3 4 X subarray length 4
X 2 3 4 5 subarray length 4
1 2 3 4 5 subarray length 5

5 8 9 8 5 total times each index was added, k = (i + 1) * (n - i)
3 4 5 4 3 total times in odd length array with (k + 1) / 2
2 4 4 4 2 total times in even length array with k / 2s


Complexity

Time O(N)
Space O(1)

```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum(((i + 1) * (len(arr) - i) + 1) // 2 * a for i, a in enumerate(arr))
```

```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        s=0
        for i in range(n):
            s+=((i+1)*(n-i)+1)//2*arr[i]
        return s
```

前缀和的方法：

```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        a = arr[:]
        for i in range(1, len(a)):
            a[i] += a[i-1]

        res = 0
        for i in range(n):
            j = i
            while j < n:
                res += a[j] - a[i] + arr[i]
                j += 2
        return res
```

