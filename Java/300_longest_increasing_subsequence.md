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
