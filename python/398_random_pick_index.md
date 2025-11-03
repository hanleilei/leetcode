# Random Pick Index

[[hash-table]] [[reservoir-sampling]] [[random]]

## Problem Description

Given an array of integers `nums` with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

**Implement the Solution class:**

- `Solution(int[] nums)`: Initializes the object with the array `nums`.
- `int pick(int target)`: Randomly returns an index of `target` in `nums`. Each index should have equal probability of being returned.

### Example

```text
Input:
["Solution", "pick", "pick"]
[[[1,2,3,3,3]], [3], [1]]

Output:
[null, 4, 0]

Explanation:
Solution solution = new Solution([1,2,3,3,3]);
solution.pick(3); // return 4, or 2 or 3, or any index of 3. Each index should have equal probability of returning.
solution.pick(1); // return 0. Since in the array only nums[0] is equal to 1.
```

### Constraints

- `1 <= nums.length <= 2 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `target` is an integer from `nums`
- At most `10^4` calls will be made to `pick`

**Note:**

- The array size can be very large. Solution that uses too much extra space will not pass the judge.

---

## 解法一：哈希表预处理（推荐，空间换时间）

```python
from collections import defaultdict
from random import choice

class Solution:
    def __init__(self, nums: List[int]):
        # 使用哈希表存储每个数值对应的所有索引
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        # 直接从所有目标值的索引中随机选择一个
        return choice(self.indices[target])
```

**核心思想：**

- 预处理阶段将数组扫一遍，将每个数值对应的所有索引存入哈希表
- 每次 pick 时直接从该数值的索引列表中随机选择一个

**时间复杂度：**

- 初始化 O(n)
- pick O(1)

**空间复杂度：** O(n)

---

## 解法二：水塘抽样（空间优化版，follow-up）

```python
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        # 水塘抽样，在一次遍历中找到目标值并随机选择
        count = 0
        result = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # 以 1/count 的概率选择当前索引
                if random.randint(1, count) == 1:
                    result = i
        return result
```

**核心思想：**

- 使用水塘抽样算法，在遍历数组时每次遇到目标值就以特定概率更新结果
- 保证每个匹配的索引都有相等的被选中概率
- 不需要额外空间存储索引列表

**时间复杂度：** O(1) 初始化，O(n) pick（最坏情况）  
**空间复杂度：** O(1) 额外空间

---

## 算法分析

### 两种方案对比

| 方法           | 初始化 | pick   | 空间 | 适用场景       |
|----------------|--------|--------|------|----------------|
| 哈希表预处理   | O(n)   | O(1)   | O(n) | 频繁调用 pick  |
| 水塘抽样       | O(1)   | O(n)   | O(1) | 空间受限       |

### 水塘抽样概率证明

对于数组中第 count 次出现的目标值：

- 该次被选中的概率：1/count
- 之后不再被替换的概率：∏(i=count+1 to m)(1 - 1/i) = count/m
- 最终被保留的概率：1/count × count/m = 1/m

其中 m 是所有匹配目标值的总数，所以每个匹配索引的最终概率都是 1/m。

---

## 相关题目

- [382. Linked List Random Node](382_Linked%20List%20Random%20Node.md) - 链表随机节点
- [384. Shuffle an Array](384_shuffle_an_array.md) - 数组洗牌
- [528. Random Pick with Weight](528_Random%20Pick%20with%20Weight.md) - 带权重的随机选择
