# Maximum Length of Repeated Subarray

[[dp]]

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

## Example 1

```text
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
```

## Example 2

```text
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
```

Constraints:

```text
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
```

这个是非常典型的dp问题：最长公共子串。

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i-1] == nums2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])
        return res
```

再来一个比较字符串的方法，也能通过：

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = ''.join(map(chr, nums1))
        nums2 = ''.join(map(chr, nums2))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        res = 0
        i = 0
        for j in range(1, n + 1):
            if nums1[i:j] in nums2:
                res = max(res, j - i)
            else:
                i += 1
        return res
```

再来一个二分法，速度似乎最快。。

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def check(length):
            seen = {nums1[i:i+length] for i in range(len(nums1) - length + 1)}
            return any(nums2[j:j+length] in seen for j in range(len(nums2) - length + 1))

        nums1 =  ''.join(map(chr, nums1))
        nums2 =  ''.join(map(chr, nums2))

        lo, hi = 0,min(len(nums1), len(nums2)) + 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo - 1
```
