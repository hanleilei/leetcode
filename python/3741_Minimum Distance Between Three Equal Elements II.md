# Minimum Distance Between Three Equal Elements II

You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

Example 1:

Input: nums = [1,2,1,1,3]

Output: 6

Explanation:

The minimum distance is achieved by the good tuple (0, 2, 3).

(0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

Example 2:

Input: nums = [1,1,2,3,2,1,2]

Output: 8

Explanation:

The minimum distance is achieved by the good tuple (2, 4, 6).

(2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.

Example 3:

Input: nums = [1]

Output: -1

Explanation:

There are no good tuples. Therefore, the answer is -1.

Constraints:

    1 <= n == nums.length <= 100
    1 <= nums[i] <= n

把 i,j,k 画在一维数轴上，∣i−j∣+∣j−k∣+∣k−i∣ 的几何意义是这三个下标中的最左最右下标绝对差的两倍。设最左最右的下标分别为 i 和 k，那么三元组的距离为 2(k−i)。

为了让 2(k−i) 尽量小，按照相同元素分组，枚举同一组中的连续三个下标分别作为 i,j,k。

```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = inf
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)
        
        for pos in d.values():
            for i in range(2, len(pos)):
                res = min(res, (pos[i] - pos[i - 2]) * 2)
        return  -1 if res == inf else res
```

或者：

1. 由于 nums[i] 的范围是 [1,n]，哈希表可以换成更轻量的数组。
2. 由于只关心最近的三个位置，所以只需要知道 x=nums[i] 上一次出现的位置 last[x] 和上上一次出现的位置 last2​[x]。
3. 此外，不需要每次循环都计算一次乘二，乘二可以放在返回答案的时候计算。

```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        last = [-inf] * (n + 1)
        last2 = [-inf] * (n + 1)

        ans = n
        for i, x in enumerate(nums):
            ans = min(ans, i - last2[x])
            last2[x] = last[x]
            last[x] = i

        return -1 if ans == n else ans * 2
```

这个题目和3740 差不多，区别在于3740中 nums[i] 的范围是 [1,n]，所以 last 和 last2 的长度是 n + 1，而不是 101。
