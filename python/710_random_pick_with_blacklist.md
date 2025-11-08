# Random Pick with Blacklist

[[hash-table]] [[random]] [[mapping]]

## Problem Description

You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.

Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.

**Implement the Solution class:**

- `Solution(int n, int[] blacklist)`: Initializes the object with the integer n and the blacklisted integers blacklist.
- `int pick()`: Returns a random integer in the range [0, n - 1] and not in blacklist.

### Example

```text
Input:
["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]

Output:
[null, 0, 4, 1, 6, 1, 0, 4]

Explanation:
Solution solution = new Solution(7, [2, 3, 5]);
solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. 
                 // Note that for every call of pick, 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
solution.pick(); // return 4
solution.pick(); // return 1
solution.pick(); // return 6
solution.pick(); // return 1
solution.pick(); // return 0
solution.pick(); // return 4
```

### Constraints

- 1 <= n <= 10^9
- 0 <= blacklist.length <= min(10^5, n - 1)
- 0 <= blacklist[i] < n
- All the values of blacklist are unique.
- At most 2 * 10^4 calls will be made to pick.

---

## 解法：哈希表映射（最优解）

```python
import random

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.mapping = {}
        # 白名单的长度（有效范围）
        self.white_len = n - len(blacklist)
        
        # 将黑名单转为集合以加快查询
        black_set = set(blacklist)
        
        # 从高端开始遍历，映射低端的黑名单值
        last = n - 1
        for b in blacklist:
            # 如果黑名单的值已经在高端范围，无需映射
            if b >= self.white_len:
                continue
            
            # 找到第一个不在黑名单中的值
            while last in black_set:
                last -= 1
            
            # 将低端的黑名单值映射到高端的白名单值
            self.mapping[b] = last
            last -= 1

    def pick(self) -> int:
        # 在白名单范围内随机选择
        index = random.randint(0, self.white_len - 1)
        
        # 如果这个位置被映射过，返回映射值；否则直接返回
        return self.mapping.get(index, index)
```

```python
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.dict = {}
        # 白名单长度
        self.white = n - len(blacklist)
        # 将黑名单的值先添加到字典
        for b in blacklist:
            self.dict[b] = 0  # 可以选取为任何值
        
        # 在黑名单区 要映射的指针
        last = n - 1
        for b in blacklist:
            # 黑名单中的值 已经在 黑名单的区间, 那么可以忽略
            if b >= self.white: 
                continue
            # last对应的值已经在黑名单中
            while last in self.dict:
                last -= 1
            self.dict[b] = last
            last -= 1


    def pick(self) -> int:
        index = randint(0, self.white - 1)  # 在白名单部分随机挑选
        if index in self.dict:  # 如果在黑名单中, 那么就映射为白名单的值
            return self.dict[index]
        return index
```

**核心思想：**

- 将问题空间分为两部分：`[0, white_len)` 和 `[white_len, n)`
- 在 `[0, white_len)` 中，黑名单值映射到 `[white_len, n)` 中的白名单值
- 每次 pick 时，仅在 `[0, white_len)` 中随机，然后通过映射得到真实值

**时间复杂度：**

- 初始化 O(m log m)，其中 m 是黑名单长度
- pick O(1)

**空间复杂度：** O(m)

---

## 算法分析

### 为什么这个算法高效？

1. **核心观察**：黑名单中有 m 个数，则白名单有 n - m 个数
2. **映射策略**：
   - 黑名单中 `< (n - m)` 的数映射到 `>= (n - m)` 的白名单数
   - 这样可以将范围缩小到 `[0, n - m)`

3. **随机优化**：
   - 每次只在 `[0, n - m)` 中随机，避免了拒绝采样
   - 大大减少了 random() 的调用次数

### 工作流程示例

假设 `n = 7, blacklist = [2, 3, 5]`：

```text
初始状态：
  [0, 1, 2, 3, 4, 5, 6]
   ↑  ↑  ↓  ↓  ↑  ↓  ↑
           黑名单     白名单(4个)

white_len = 7 - 3 = 4
需要映射的黑名单值: [2, 3]（< 4的）

映射过程：
  黑名单[2, 3]中 < 4 的值：[2, 3]
  白名单中 >= 4 的值：[4, 6]
  
  mapping = {2: 6, 3: 4}

pick() 时：
  随机选择 [0, 1, 2, 3]
  如果选 2 → 返回 mapping[2] = 6
  如果选 3 → 返回 mapping[3] = 4
  否则直接返回
```

### 为什么不用其他方法？

| 方法          | 时间复杂度 | 空间复杂度 | 缺点           |
|---------------|------------|-----------|----------------|
| 拒绝采样      | O(1)~O(∞) | O(m)      | 需多次调用随机 |
| 哈希表映射    | O(1)       | O(m)      | **最优解**     |
| 排序+二分     | O(m log m) | O(m)      | 每次 pick O(log m) |

## 相关题目

- [398. Random Pick Index](398_random_pick_index.md) - 随机数索引
- [528. Random Pick with Weight](528_Random%20Pick%20with%20Weight.md) - 带权重的随机选择
- [380. Insert Delete GetRandom O(1)](380_insert_delete_getrandom.md) - 随机集合
