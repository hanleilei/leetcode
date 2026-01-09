# longest increasing subsequence

[[dp]] [[binarysearch]]

Given an integer array nums, return the length of the longest strictly increasing subsequence.

## Example 1

```text
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

## Example 2

```text
Input: nums = [0,1,0,3,2,3]
Output: 4
```

## Example 3

```text
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

## Constraints

```text
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
```

标准的dp问题：

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0){
            return 0;
        }
        int res = 1;
        int[] dp = new int[nums.length + 1];
        for (int i = 0; i < nums.length; ++i) dp[i] = 1;
        for (int i = 1; i < nums.length; ++i){
            for (int j = 0; j < i; ++j){
                if (nums[j] < nums[i]){
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```

先来一个自己实现的二分查找：

```python
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) // 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)
```

```python
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        def insert(target):
            left, right = 0, len(LIS) - 1
            # Find the first index "left" which satisfies LIS[left] >= target
            while left <= right:
                mid = left + (right - left) // 2
                if LIS[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target);
            else:
                LIS[left] = target

        for num in nums:
            insert(num)

        return len(LIS)
```

上标准库：

Greedy with Binary Search

Let's construct the idea from following example.
Consider the example nums = [2, 6, 8, 3, 4, 5, 1], let's try to build the increasing subsequences starting with an empty one: sub1 = [].

1. Let pick the first element, sub1 = [2].
2. 6 is greater than previous number, sub1 = [2, 6]
3. 8 is greater than previous number, sub1 = [2, 6, 8]
4. 3 is less than previous number, we can't extend the subsequence sub1, but we must keep 3 because in the future there may have the longest subsequence start with [2, 3], sub1 = [2, 6, 8], sub2 = [2, 3].
5. With 4, we can't extend sub1, but we can extend sub2, so sub1 = [2, 6, 8], sub2 = [2, 3, 4].
6. With 5, we can't extend sub1, but we can extend sub2, so sub1 = [2, 6, 8], sub2 = [2, 3, 4, 5].
7. With 1, we can't extend neighter sub1 nor sub2, but we need to keep 1, so sub1 = [2, 6, 8], sub2 = [2, 3, 4, 5], sub3 = [1].
8. Finally, length of longest increase subsequence = len(sub2) = 4.

In the above steps, we need to keep different sub arrays (sub1, sub2..., subk) which causes poor performance. But we notice that we can just keep one sub array, when new number x is not greater than the last element of the subsequence sub, we do binary search to find the smallest element >= x in sub, and replace with number x.

Let's run that example nums = [2, 6, 8, 3, 4, 5, 1] again:

1. Let pick the first element, sub = [2].
2. 6 is greater than previous number, sub = [2, 6]
3. 8 is greater than previous number, sub = [2, 6, 8]
4. 3 is less than previous number, so we can't extend the subsequence sub. We need to find the smallest number >= 3 in sub, it's 6. Then we overwrite it, now sub = [2, 3, 8].
5. 4 is less than previous number, so we can't extend the subsequence sub. We overwrite 8 by 4, so sub = [2, 3, 4].
6. 5 is greater than previous number, sub = [2, 3, 4, 5].
7. 1 is less than previous number, so we can't extend the subsequence sub. We overwrite 2 by 1, so sub = [1, 3, 4, 5].
8. Finally, length of longest increase subsequence = len(sub) = 4.

```python
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        stack = []
        for n in nums:
            if not stack or n > stack[-1]:
                stack.append(n)
            else:
                idx = bisect.bisect_left(stack, n)
                stack[idx] = n
        return len(stack)
```

或者：

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [sys.maxsize] * len(nums)   # 相当于 INT_MAX
        for x in nums:
            # lower_bound 返回第一个 >= x 的位置的索引
            idx = bisect.bisect_left(lis, x)
            lis[idx] = x
        # 找到第一个仍是 sys.maxsize 的位置，即有效长度
        idx = bisect.bisect_left(lis, sys.maxsize)
        return idx
```

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> lis(nums.size(), INT_MAX);
        for (auto x: nums){
            lis[ranges::lower_bound(lis, x) - lis.begin()] = x;
        }
        return ranges::lower_bound(lis, INT_MAX) - lis.begin();
    }
};
```
