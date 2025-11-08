# Insert Delete GetRandom O(1)

[[hash-table]] [[array]] [[random]] [[design]]

## Problem Description

Design a data structure that supports all following operations in average **O(1)** time.

**Implement the RandomizedSet class:**

- `bool insert(int val)`: Inserts an item `val` to the set if not already present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)`: Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()`: Returns a random element from the current set of elements. Each element must have the **equal probability** of being returned.

### Example

```text
Input:
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]

Output:
[null, true, false, true, 2, true, false, 2]

Explanation:
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1);   // Inserts 1 to the set. Returns true as it was inserted successfully.
randomizedSet.remove(2);   // Returns false as 2 does not exist in the set.
randomizedSet.insert(2);   // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1);   // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2);   // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
```

### Constraints

- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`
- There will be **at least one** element in the data structure when `getRandom` is called

---

## 解法：哈希表 + 动态数组（最优解）

```python
import random

class RandomizedSet:
    def __init__(self):
        self.nums = []        # 存储元素的数组
        self.pos = {}         # 哈希表：元素值 -> 在数组中的索引

    def insert(self, val: int) -> bool:
        # 如果元素已存在，返回 false
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        # 如果元素不存在，返回 false
        if val in self.pos:
            # 获取要删除元素的索引和数组最后一个元素
            idx = self.pos[val]
            last = self.nums[-1]
            
            # 交换删除元素和末尾元素
            self.nums[idx] = last
            self.pos[last] = idx
            
            # 删除末尾元素
            self.nums.pop()
            del self.pos[val]
            return True
        return False

    def getRandom(self) -> int:
        # 从数组中随机返回一个元素
        return self.nums[random.randint(0, len(self.nums) - 1)]
```

**核心思想：**

- 使用**数组**存储元素以支持 O(1) 的随机访问
- 使用**哈希表**存储元素值到数组索引的映射，支持 O(1) 的查找
- **删除时**：用末尾元素替换删除位置的元素，然后删除末尾，避免数组中间删除的 O(n) 开销
- **随机选择**：直接从数组中随机选取，保证等概率

**时间复杂度：**

- `insert` O(1)
- `remove` O(1)
- `getRandom` O(1)

**空间复杂度：** O(n)

---

## 算法分析

### 为什么用数组 + 哈希表？

1. **数组特点**：
   - 支持 O(1) 随机访问（getRandom）
   - 但中间删除是 O(n)

2. **哈希表特点**：
   - 支持 O(1) 查找、插入
   - 无法高效随机访问

3. **结合方案**：
   - 哈希表快速定位元素位置
   - 数组支持随机访问
   - 删除时用末尾元素替换，避免中间删除的 O(n) 操作

### 删除操作详解

假设要删除值为 `val` 的元素，位置为 `idx`：

```
删除前: nums = [1, 2, 3, 4, 5]  (要删除 3，索引 2)
                      ^
                    idx=2

步骤1：交换 nums[idx] 和末尾元素 nums[-1]
       nums = [1, 2, 5, 4, 3]
       pos = {1: 0, 2: 1, 5: 2, 4: 3}
            
步骤2：删除末尾元素
       nums = [1, 2, 5, 4]
       pos = {1: 0, 2: 1, 5: 2, 4: 3, 3: deleted}
```

### 时间复杂度对比

| 操作      | 仅用数组 | 仅用哈希表 | 数组+哈希表 |
|-----------|----------|-----------|------------|
| insert    | O(1)     | O(1)      | O(1)       |
| remove    | O(n)     | O(1)      | O(1)       |
| getRandom | O(1)     | O(n)      | O(1)       |

---

## 相关题目

- [398. Random Pick Index](398_random_pick_index.md) - 随机数索引
- [384. Shuffle an Array](384_shuffle_an_array.md) - 数组洗牌
- [535. Encode and Decode TinyURL](535_encode_and_decode_tinyurl.md) - 哈希表设计

