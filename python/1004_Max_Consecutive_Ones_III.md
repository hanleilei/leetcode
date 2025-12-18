# Max Consecutive Ones III

[[sliding_window]] [[2pointers]] [[array]]

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.

## Example 1

```text
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
```

### Example 2

```text
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
```

### Note

```text
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
```

动态规划。。

```python
class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        l = len(A)
        zero = 0
        lo,hi = 0,0
        res = 0
        for hi in range(l):
            if A[hi] == 0:
                zero += 1
            while zero > k:               
                if A[lo] == 0:
                    zero -= 1
                lo += 1
            # print lo, hi
            res = max(res, hi - lo + 1)

        return res
```

```python
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1
```

最快：

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=r=0    
        while r < len(nums):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
            r += 1
        return r-l
```

labuladong：

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        ones = 0
        res = 0

        while right < len(nums):
            if nums[right] == 1:
                ones += 1
            right += 1

            while right - left - ones > k:
                if nums[left] == 1:
                    ones -= 1
                left += 1
            res = max(res, right - left)
        return res
```
