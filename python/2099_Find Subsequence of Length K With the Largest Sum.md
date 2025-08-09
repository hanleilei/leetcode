# Find Subsequence of Length K With the Largest Sum

[[heap]]

You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation:
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7.
Another possible subsequence is [4, 3].

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length

```python
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # 获取前 k 个最大的元素（可能有重复）
        largest = nlargest(k, nums)
        # 统计这些元素出现的次数
        freq = defaultdict(int)
        for num in largest:
            freq[num] += 1
        # 遍历原数组，按顺序收集这些元素
        res = []
        for num in nums:
            if freq.get(num, 0) > 0:
                res.append(num)
                freq[num] -= 1
                if len(res) == k:
                    break
        return res
```

````python
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Keep track of original indices
        indexed = [(num, i) for i, num in enumerate(nums)]
        
        # Step 2: Sort by value (descending) and take top k
        top_k = sorted(indexed, key=lambda x: x[0], reverse=True)[:k]
        
        # Step 3: Sort selected k elements by original index
        top_k.sort(key=lambda x: x[1])
        
        # Step 4: Extract the numbers only
        return [num for num, _ in top_k]
```
