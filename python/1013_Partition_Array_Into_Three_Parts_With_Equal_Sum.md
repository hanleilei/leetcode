# Partition Array Into Three Parts With Equal Sum

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])



#### Example 1:
```
Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
```
#### Example 2:
```
Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
```
#### Example 3:
```
Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
```

#### Note:
```
3 <= A.length <= 50000
-10000 <= A[i] <= 10000
```

都是自己想出来的方法，但是，速度太感人了。这类简单的问题要很快搞定，二十分钟最多才行。

```Python
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False

        s = s // 3
        res = 0
        count = 3
        A.insert(0, 0)

        while A:
            if res == s:
                res = A.pop()
                count -= 1
                continue

            res += A.pop()
        return count == 0
```

```Python
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        res = 0
        count = 3
        if total % 3 != 0:
            return False

        for i in range(len(A)):
            if res != total//3:
                res += A[i]
            else:
                res = A[i]
                count -= 1

        return count == 0 or  res == total // 3


```
