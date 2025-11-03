# Random Pick with Weight

[[binary-search]] [[prefix-sum]] [[random]]

## Problem Description

You are given a 0-indexed array of positive integers `w` where `w[i]` describes the weight of the ith index.

You need to implement the function `pickIndex()`, which randomly picks an index in the range `[0, w.length - 1]` (inclusive) and returns it. The probability of picking an index `i` is `w[i] / sum(w)`.

For example, if `w = [1, 3]`, the probability of picking index 0 is `1 / (1 + 3) = 0.25` (i.e., 25%), and the probability of picking index 1 is `3 / (1 + 3) = 0.75` (i.e., 75%).

**Implement the Solution class:**

- `Solution(int[] w)`: Initializes the object with the given weights `w`.
- `int pickIndex()`: Randomly picks an index in the range `[0, w.length - 1]` (inclusive) and returns it.

## Examples

**Example 1:**

```text
Input: ["Solution","pickIndex"]
       [[[1]],[]]
Output: [null,0]

Explanation:
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
```

**Example 2:**

```text
Input: ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
       [[[1,3]],[],[],[],[],[]]
Output: [null,1,1,1,1,0]

Explanation:
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
```

## Constraints

- `1 <= w.length <= 10^4`
- `1 <= w[i] <= 10^5`
- At most `10^4` calls will be made to `pickIndex`

---

## 解法一：前缀和 + 二分查找（bisect库，推荐）

```python
import random
import bisect
class Solution:
    def __init__(self, w: List[int]):
        # 构建前缀和数组，方便区间查找
        self.pre = [0]
        for x in w:
            self.pre.append(self.pre[-1] + x)

    def pickIndex(self) -> int:
        # 在(0, 总权重]内随机取一个数，找到其对应的区间
        target = random.randint(1, self.pre[-1])
        return bisect.bisect_left(self.pre, target) - 1
```

**核心思想：**

- 将权重数组转换为前缀和数组，例如 `w = [1, 3]` 转换为 `pre = [0, 1, 4]`
- 随机生成 `[1, sum]` 范围内的数，落在哪个区间就选择对应的索引
- 使用二分查找快速定位区间

**时间复杂度：** O(n) 初始化，O(log n) 每次查询  
**空间复杂度：** O(n)

---

## 解法二：前缀和 + 手写二分查找

```python
from random import randint
class Solution:
    def __init__(self, w: List[int]):
        # 构建前缀和数组
        self.pre_sum = [0] * (len(w) + 1)
        for i in range(1, len(w) + 1):
            self.pre_sum[i] = self.pre_sum[i-1] + w[i-1]

    def pickIndex(self) -> int:
        # 随机生成目标值
        target = randint(1, self.pre_sum[-1])
        # 手写二分查找找到第一个 >= target 的位置
        left, right = 1, len(self.pre_sum) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.pre_sum[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left - 1
```

**思路说明：**

- 和解法一原理相同，但手写二分查找
- 查找第一个 `>= target` 的位置，返回其前一个索引

**时间复杂度：** O(n) 初始化，O(log n) 每次查询  
**空间复杂度：** O(n)

---

## 算法分析

**为什么前缀和可以解决按权重随机？**

假设权重数组为 `[w_0, w_1, ..., w_{n-1}]`，总权重为 `S = sum(w)`。

1. 构建前缀和数组 `pre[i] = w_0 + w_1 + ... + w_{i-1}`
2. 将整个权重空间 `[1, S]` 划分为 n 个区间：
   - 区间 1: `(pre[0], pre[1]]` → 长度为 `w[0]`
   - 区间 2: `(pre[1], pre[2]]` → 长度为 `w[1]`
   - ...
   - 区间 n: `(pre[n-1], pre[n]]` → 长度为 `w[n-1]`
3. 在 `[1, S]` 内随机生成一个数，落在第 i 个区间的概率为 `w[i] / S`
4. 使用二分查找快速定位该数所在的区间

**示例：** `w = [1, 3]`

- 前缀和: `pre = [0, 1, 4]`
- 随机数范围: `[1, 4]`
- 如果随机数是 1，落在区间 `(0, 1]`，返回索引 0（概率 1/4）
- 如果随机数是 2、3、4，落在区间 `(1, 4]`，返回索引 1（概率 3/4）

---

## 相关题目

- [382. Linked List Random Node](382_Linked%20List%20Random%20Node.md) - 链表随机节点
- [384. Shuffle an Array](384_shuffle_an_array.md) - 数组洗牌
- [398. Random Pick Index](398_random_pick_index.md) - 随机数索引
