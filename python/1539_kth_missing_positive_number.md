# kth missing positive number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.



## Example 1:
```
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
```
## Example 2:
```
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
```

Constraints:
```
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
```

我想到的方法，比较呆。。
```Python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if len(arr) == arr[-1]:
            return arr[-1] + k
        if arr[-1] - len(arr) < k:
            return k + len(arr)
        diff = list(set(range(1, arr[-1])).difference(set(arr)))
        diff.sort()
        return diff[k-1]
```
看下lee215的方法：
Java:
```java
    public int findKthPositive(int[] A, int k) {
        int l = 0, r = A.length, m;
        while (l < r) {
            m = (l + r) / 2;
            if (A[m] - 1 - m < k)
                l = m + 1;
            else
                r = m;
        }
        return l + k;
    }
```
C++:
```cpp
    int findKthPositive(vector<int>& A, int k) {
        int l = 0, r = A.size(), m;
        while (l < r) {
            m = (l + r) / 2;
            if (A[m] - 1 - m < k)
                l = m + 1;
            else
                r = m;
        }
        return l + k;
    }
```
Python:
```Python
    def findKthPositive(self, A, k):
        l, r = 0, len(A)
        while l < r:
            m = (l + r) // 2
            if A[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k
```
Python, using bisect
Suggested by @r0bertz
```Python
    def findKthPositive(self, A, k):
        class Count(object):
            def __getitem__(self, i):
                return A[i] - i - 1
        return k + bisect.bisect_left(Count(), k, 0, len(A))
```

More Good Binary Search Problems

Kth Missing Positive Number
Minimum Number of Days to Make m Bouquets
Find the Smallest Divisor Given a Threshold
Divide Chocolate
Capacity To Ship Packages In N Days
Koko Eating Bananas
Minimize Max Distance to Gas Station
Split Array Largest Sum
