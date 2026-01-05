# shuffle an array

Shuffle a set of numbers without duplicates.

## Example

```java
// Init an array with set 1, 2, and 3.
# Shuffle an Array

[[array]] [[random]] [[fisher-yates]]

## Problem Description

Given an integer array `nums` without duplicates, design an algorithm to shuffle the array randomly. Implement the `Solution` class:

- `Solution(int[] nums)`: Initializes the object with the integer array `nums`.
- `int[] reset()`: Resets the array to its original configuration and returns it.
- `int[] shuffle()`: Returns a random shuffling of the array.

## Example

```text
Input: ["Solution", "shuffle", "reset", "shuffle"]
       [[[1, 2, 3]], [], [], []]
Output: [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation:
Solution solution = new Solution([1, 2, 3]);
solution.shuffle(); // Returns [3, 1, 2] (any permutation with equal probability)
solution.reset();   // Returns [1, 2, 3]
solution.shuffle(); // Returns [1, 3, 2]
```

### Constraints

- 1 <= nums.length <= 200
- -10^6 <= nums[i] <= 10^6
- All elements are unique
- At most 5 * 10^4 calls will be made to `reset` and `shuffle`

---

## 解法一：Fisher-Yates 洗牌算法（最优解）

```python
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.origin = nums[:]
        self.nums = nums[:]

    def reset(self) -> List[int]:
        return self.origin[:]

    def shuffle(self) -> List[int]:
        # Fisher-Yates 洗牌，保证每个排列等概率
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
```

**核心思想：**

- 每次从未处理区间随机选一个数交换到当前位置，保证所有排列等概率。

**时间复杂度：** O(n)
**空间复杂度：** O(n)

---

## 解法二：直接用random.shuffle（简洁但不考察原理）

```python
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.origin = nums[:]
        self.nums = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.origin[:]
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums
```

**说明：**

- `random.shuffle` 内部实现也是 Fisher-Yates 算法。
- 适合面试时快速实现，但建议理解原理。

---

## 算法分析

| 方法                | 时间复杂度 | 空间复杂度 | 备注           |
|---------------------|------------|------------|----------------|
| Fisher-Yates 洗牌   | O(n)       | O(n)       | 推荐，等概率   |
| random.shuffle      | O(n)       | O(n)       | 简洁，等概率   |

---

## 相关题目

- [398. Random Pick Index](398_random_pick_index.md)
- [382. Linked List Random Node](382_Linked List Random Node.md)
