# K-th Smallest Prime Fraction

[[binarysearch]] [[2points]]

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]

Constraints:

2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 104
arr[0] == 1
arr[i] is a prime number for i > 0.

All the numbers of arr are unique and sorted in strictly increasing order.

1 <= k <= arr.length * (arr.length - 1) / 2

Follow up: Can you solve the problem with better than O(n^2) complexity?

```python
class Solution: 
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        d = dict()
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                d[arr[i]/arr[j]] = (arr[i], arr[j])
        smallest = heapq.nsmallest(k, [float(key) for key in d.keys()])[-1]
        return list(d[smallest])
```

自制的算法。。很土，只是能够通过。

再来看看lee215的方法：

for each row i, all the numbers (call them A[j]) to the right of A[i]/m, are the ones such that A[i]/A[j] will be smaller than m.
sum them up so that you will know the total number of pairs A[i]/A[j] that are smaller than m. Find a proper m such that the total number equals K, and then you find the maximum A[i]/A[j] among all pairs that are smaller than A[i]/m, which is the Kth smallest number.

```python
class Solution: 
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        l, r, N = 0, 1, len(A)
        while True:
            m = (l + r) / 2
            border = [bisect.bisect(A, A[i] / m) for i in range(N)]
            cur = sum(N - i for i in border)
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                return max([(A[i], A[j]) for i, j in enumerate(border) if j < N], key=lambda x: x[0] / x[1])
```

参考这个：https://leetcode.cn/problems/k-th-smallest-prime-fraction/solutions/1127751/gong-shui-san-xie-yi-ti-shuang-jie-you-x-8ymk/

```python
class Solution: 
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0, 1.0

        # Binary search for finding the kth smallest prime fraction
        while left < right:
            # Calculate the middle value
            mid = (left + right) / 2

            # Initialize variables to keep track of maximum fraction and indices
            max_fraction = 0.0
            total_smaller_fractions = 0
            numerator_idx = 0
            denominator_idx = 0
            j = 1

            # Iterate through the array to find fractions smaller than mid
            for i in range(n - 1):
                while j < n and arr[i] >= mid * arr[j]:
                    j += 1

                # Count smaller fractions
                total_smaller_fractions += (n - j)

                # If we have exhausted the array, break
                if j == n:
                    break

                # Calculate the fraction
                fraction = arr[i] / arr[j]

                # Update max_fraction and indices if necessary
                if fraction > max_fraction:
                    numerator_idx = i
                    denominator_idx = j
                    max_fraction = fraction

            # Check if we have found the kth smallest prime fraction
            if total_smaller_fractions == k:
                return [arr[numerator_idx], arr[denominator_idx]]
            elif total_smaller_fractions > k:
                right = mid  # Adjust the range for binary search
            else:
                left = mid  # Adjust the range for binary search

        return []  # Retu
```
