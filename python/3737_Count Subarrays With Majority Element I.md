# Count Subarrays With Majority Element I

You are given an integer array nums and an integer target.

Return the number of of nums in which target is the majority element.

The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.

Example 1:

Input: nums = [1,2,2,3], target = 2

Output: 5

Explanation:

Valid subarrays with target = 2 as the majority element:

    nums[1..1] = [2]
    nums[2..2] = [2]
    nums[1..2] = [2,2]
    nums[0..2] = [1,2,2]
    nums[1..3] = [2,2,3]

So there are 5 such subarrays.

Example 2:

Input: nums = [1,1,1,1], target = 1

Output: 10

Explanation:

​​​​​​​All 10 subarrays have 1 as the majority element.

Example 3:

Input: nums = [1,2,3], target = 4

Output: 0

Explanation:

target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 10​​​​​​^9
    1 <= target <= 10^9

类似 525. 连续数组，把 nums 中的 target 视作 1，其余元素视作 −1，得到一个新数组 a，问题变成：

    计算 a 中元素和严格大于 0 的子数组个数。

设 a 的前缀和数组为 s。关于 s 的定义，请看 前缀和。

问题变成：

    计算有多少对 (i,j) 满足 0≤i<j≤n 且 s[j]−s[i]>0。

枚举 j，问题变成：

    计算 s 的下标区间 [0,j−1] 中有多少个 s[i]<s[j]。

方法一：枚举右，有序集合维护左

枚举 j 的同时，用有序集合维护左边的 s[i]。

在有序集合中查找第一个 ≥s[j] 的数的位置，即为 $s[i]<s[j]$ 的个数。

```python
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        sl = SortedList([0])
        res = s = 0
        for n in nums:
            s += 1 if n == target else -1
            res += sl.bisect_left(s)
            sl.add(s)
        return res
```

每次循环，s 的变化量只有 1。

定义 f[j] 表示满足 i<j 且 s[i]<s[j] 的 i 的个数（即方法一每次循环加到 ans 中的值）。

如果知道 f[j−1]，能不能 O(1) 地把 f[j] 算出来？

如果 s[j]=s[j−1]+1，我们可以在 f[j−1] 的基础上，加上恰好等于 s[j]−1 的 s[i] 的个数，就得到了 f[j]。

这启发我们统计 s[j] 的出现次数 cnt[s[j]]。

    如果 s[j]=s[j−1]+1，我们可以在 f[j−1] 的基础上，加上恰好等于 s[j]−1 的 s[i] 的个数 cnt[s[j]−1]，得到 f[j]=f[j−1]+cnt[s[j]−1]=f[j−1]+cnt[s[j−1]]。
    如果 s[j]=s[j−1]−1，我们可以在 f[j−1] 的基础上，减去恰好等于 s[j] 的 s[i] 的个数 cnt[s[j]]，得到 f[j]=f[j−1]−cnt[s[j]]。

答案为 f 的元素和。

```python
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        s = n = len(nums)
        cnt = [0] * (n * 2 + 1)
        cnt[s] = 1
        ans = f = 0
        for x in nums:
            if x == target:
                f += cnt[s]
                s += 1
            else:
                s -= 1
                f -= cnt[s]
            ans += f
            cnt[s] += 1
        return ans
```
