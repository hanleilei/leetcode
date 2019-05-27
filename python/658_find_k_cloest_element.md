# Find K Closest Elements

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

#### Example 1:
```
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
```

#### Example 2:
```
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
```

#### Note:

The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104


UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.


注意这里用了一个非常巧妙的二分法解决了这个问题。分析如下：

### Intuition

The array is sorted.
If we want find the one number closest to x,
we don't have to check one by one.
it's straightforward to use binary research.

Now we want the k closest,
the logic should be similar.


### Explanation:

Assume we are taking A[i] ~ A[i + k -1].
We can binary research i
We compare the distance between x - A[mid] and A[mid - k] - x

If x - A[mid] > A[mid + k] - x,
it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
and we have mid smaller than the right i.
So assign left = mid + 1.

Note that, you shouldn't compare the absolute value abs(x - A[mid]) and abs(A[mid + k] - x).
It's wrong though it get accepetd.
It fails at the case A = [1,1,2,2,2,2,2,3,3], x=3, k=2



### Time Complexity:

O(log(N - K)) to binary research and find reseult
O(K) to create the returned list.


```Python
class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x: # key part
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]

```
