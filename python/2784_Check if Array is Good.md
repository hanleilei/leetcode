# Check if Array is Good

You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].

base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

Return true if the given array is good, otherwise return false.

Note: A permutation of integers represents an arrangement of these numbers.

Example 1:

Input: nums = [2, 1, 3]
Output: false
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.
Example 2:

Input: nums = [1, 3, 3, 2]
Output: true
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.
Example 3:

Input: nums = [1, 1]
Output: true
Explanation: Since the maximum element of the array is 1, the only candidate n for which this array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of base[1] = [1, 1]. Therefore, the answer is true.
Example 4:

Input: nums = [3, 4, 4, 1, 2, 1]
Output: false
Explanation: Since the maximum element of the array is 4, the only candidate n for which this array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer is false.

Constraints:

1 <= nums.length <= 100
1 <= num[i] <= 200

桶排序：

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        bucket = [0] * n  # 下标 0 ~ n-1

        for x in nums:
            if x < 1 or x >= n:
                return False
            bucket[x] += 1

        # 1 ~ n-2 各出现一次，n-1 出现两次
        for i in range(1, n - 1):
            if bucket[i] != 1:
                return False

        return bucket[n - 1] == 2
```

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        cnt = [0] * (n + 1)

        for x in nums:
            if x > n: # 出现大于 n 的数
                return False
            if x == n and cnt[x] > 1: # n 出现超过两次
                return False
            if x < n and cnt[x] > 0: # 1 ~ n-1 出现超过一次
                return False
            cnt[x] += 1

        return True
```

由于 nums 中的数都是正整数，我们可以在首次遇到元素 x 时，把 nums[x] 改成 −nums[x]，这样再次遇到 ∣x∣ 时，就能通过 nums[∣x∣]<0 得知 nums 中至少有两个 ∣x∣。

对于 n，我们需要判断 n 是否出现超过两次，可以单独用一个变量 cntN 统计 n 的出现次数。

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        cnt_n = 0
        for x in nums:
            x = abs(x)
            if (x > n or
                x == n and cnt_n > 1 or
                x < n and nums[x] < 0):  # x 之前遇到过，现在又遇到了，所以 x 的出现次数至少是 2
                return False
            if x == n:
                cnt_n += 1
            else:
                nums[x] = -nums[x]  # 标记 x 遇到过
        return True
```

位运算：

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n == 0:
            return False
        mask = 0
        k = 1
        for x in nums:
            b = 1 << x
            if x == n and k and mask & b:
                k -= 1
            elif x > n or mask & b:
                return False
            mask |= b
        return mask == (1 << (n+1)) - 2
```

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        res = [i for i in range(1, len(nums) + 1)]
        res[-1] = res[-1] - 1

        return res == sorted(nums)
```

继续单行：

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # return sorted(nums)==list(range(1,len(nums)))+[len(nums)-1]
        return Counter(nums)==Counter(list(range(1,(n:=len(nums))))+[n-1])
```
