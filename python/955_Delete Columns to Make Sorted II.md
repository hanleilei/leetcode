# 955. Delete Columns to Make Sorted II

## 问题描述

You are given an array of `n` strings `strs`, all of the same length.

We may choose any deletion indices, and we delete all the characters
in those indices for each string.

For example, if we have `strs = ["abcdef","uvwxyz"]` and deletion
indices `{0, 2, 3}`, then the final array after deletions is
`["bef", "vyz"]`.

Suppose we chose a set of deletion indices `answer` such that after
deletions, the final array has its elements in **lexicographic
order** (i.e., `strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]`).

Return the **minimum** possible value of `answer.length`.

## 示例

**Example 1:**

```text
Input: strs = ["ca","bb","ac"]
Output: 1
```

Explanation: After deleting the first column, `strs = ["a", "b", "c"]`.
Now strs is in lexicographic order. We require at least 1 deletion
since initially strs was not in lexicographic order.

**Example 2:**

```text
Input: strs = ["xc","yb","za"]
Output: 0
```

Explanation: strs is already in lexicographic order, so we do not
need to delete anything. Note that the rows of strs are not
necessarily in lexicographic order.

**Example 3:**

```text
Input: strs = ["zyx","wvu","tsr"]
Output: 3
```

Explanation: We have to delete every column.

## 约束条件

- `n == strs.length`
- $1 \le n \le 100$
- $1 \le \text{strs}[i].\text{length} \le 100$
- `strs[i]` consists of lowercase English letters

## 解法

### 方法1：贪心 + 动态检查列表 推荐

逐列检查，维护一个需要继续检查的行对列表，如果当前列有序，
则更新检查列表。

```python
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        贪心 + 动态检查列表

        时间复杂度：O(n × m)
        空间复杂度：O(n)
        """
        n, m = len(strs), len(strs[0])
        # 需要检查的相邻行对索引列表
        check_list = list(range(n - 1))

        deleted = 0

        for j in range(m):
            # 检查第j列是否有序
            for i in check_list:
                if strs[i][j] > strs[i + 1][j]:
                    # 第j列不是升序，必须删除
                    deleted += 1
                    break
            else:
                # 第j列是升序，保留这一列
                # 更新check_list：只保留当前列相等的行对
                new_size = 0
                for i in check_list:
                    if strs[i][j] == strs[i + 1][j]:
                        # 相邻字符相等，下一列仍需比较
                        check_list[new_size] = i
                        new_size += 1
                # 原地截断列表
                del check_list[new_size:]

        return deleted
```

### 方法2：贪心 + 有序标记数组

使用布尔数组标记哪些行对已经确定有序。

```python
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        贪心 + 有序标记数组

        时间复杂度：O(n × m)
        空间复杂度：O(n)
        """
        n, m = len(strs), len(strs[0])
        # sorted[i] = True 表示 strs[i] < strs[i+1] 已确定
        sorted_pairs = [False] * (n - 1)
        deleted = 0

        for j in range(m):
            # 检查第j列
            delete_col = False

            for i in range(n - 1):
                if sorted_pairs[i]:
                    # 这一对已经确定有序，跳过
                    continue

                if strs[i][j] > strs[i + 1][j]:
                    # 违反顺序，必须删除此列
                    delete_col = True
                    break

            if delete_col:
                deleted += 1
            else:
                # 保留此列，更新有序标记
                for i in range(n - 1):
                    if strs[i][j] < strs[i + 1][j]:
                        sorted_pairs[i] = True

        return deleted
```

### 方法3：贪心 + 字符串比较

保留已处理的列，构建部分字符串进行比较。

```python
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        贪心 + 字符串比较

        时间复杂度：O(n × m²)
        空间复杂度：O(n × m)
        """
        n, m = len(strs), len(strs[0])
        # 保存已保留列构成的字符串
        current_strs = [""] * n
        deleted = 0

        for j in range(m):
            # 尝试添加第j列
            temp_strs = [current_strs[i] + strs[i][j] for i in range(n)]

            # 检查是否有序
            is_sorted = all(
                temp_strs[i] <= temp_strs[i + 1] 
                for i in range(n - 1)
            )

            if is_sorted:
                # 保留此列
                current_strs = temp_strs
            else:
                # 删除此列
                deleted += 1

        return deleted
```

## 算法分析

### 核心思想详解

这道题的关键在于**贪心策略**：逐列判断，能保留就保留。

**字典序比较规则**：

对于字符串 `s1` 和 `s2`：

- 如果 `s1[i] < s2[i]`，则 `s1 < s2`，后续字符无需比较
- 如果 `s1[i] > s2[i]`，则 `s1 > s2`，当前列必须删除
- 如果 `s1[i] == s2[i]`，需要继续比较下一列

**动态检查列表的优化**：

初始时所有相邻行对都需要检查。当某一列确定了部分行对的顺序后，
这些行对后续无需再检查。

```python
# 初始：check_list = [0, 1, 2] (n=4)
# 表示需要比较 (strs[0], strs[1]), (strs[1], strs[2]), 
#             (strs[2], strs[3])

# 第0列：如果 strs[0][0] < strs[1][0]
# 则 strs[0] < strs[1] 已确定，后续无需检查索引0

# 第0列：如果 strs[1][0] == strs[2][0]
# 则需要继续比较下一列，保留索引1
```

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 动态检查列表 | O(n × m) | O(n) | 最优解 |
| 有序标记数组 | O(n × m) | O(n) | 易理解 |
| 字符串比较 | O(n × m²) | O(n × m) | 代码简洁 |

其中 n 是字符串数量，m 是字符串长度。

### 执行过程示例

以 `strs = ["ca", "bb", "ac"]` 为例：

初始状态：

```text
strs = ["ca", "bb", "ac"]
        0↓  1↓  2↓
       [c,  b,  a]  第0列
       [a,  b,  c]  第1列

需要保证：strs[0] <= strs[1] <= strs[2]
check_list = [0, 1]  # 需要检查的行对
```

**Step 1**：检查第 0 列

```text
第0列：['c', 'b', 'a']

检查 i=0: strs[0][0]='c' > strs[1][0]='b'  ✗ 不满足升序
需要删除第0列

deleted = 1
check_list 不变 = [0, 1]
```

**Step 2**：检查第 1 列

```text
第1列：['a', 'b', 'c']

检查 i=0: strs[0][1]='a' < strs[1][1]='b'  ✓ 升序
检查 i=1: strs[1][1]='b' < strs[2][1]='c'  ✓ 升序

保留第1列，更新check_list：
- i=0: 'a' < 'b'，行对(0,1)已确定有序，移除
- i=1: 'b' < 'c'，行对(1,2)已确定有序，移除

check_list = []  (所有行对都已确定)
```

结果：`deleted = 1`

**可视化过程**：

```text
原数组：
  col0  col1
  ----  ----
  c     a      strs[0]
  b     b      strs[1]
  a     c      strs[2]
  ↓
  ✗ 不升序

删除col0后：
  col1
  ----
  a      strs[0]  ← 
  b      strs[1]  ← 有序！
  c      strs[2]  ←
  ↓
  ✓ 升序
```

### 另一个示例

以 `strs = ["xc", "yb", "za"]` 为例：

**Step 1**：检查第 0 列

```text
第0列：['x', 'y', 'z']

i=0: 'x' < 'y'  ✓
i=1: 'y' < 'z'  ✓

保留第0列
所有行对都已确定有序
check_list = []
```

**Step 2**：检查第 1 列

```text
check_list为空，无需检查
```

结果：`deleted = 0`

## 常见错误

### 错误1：每次都检查所有行对

```python
# 错误：即使行对已确定有序仍继续检查
for j in range(m):
    for i in range(n - 1):  # 总是检查所有i
        if strs[i][j] > strs[i + 1][j]:
            deleted += 1
            break

# 正确：维护需要检查的行对列表
check_list = list(range(n - 1))
for j in range(m):
    for i in check_list:  # 只检查需要的
        ...
```

### 错误2：相等时错误地标记为有序

```python
# 错误：相等时就认为有序
if strs[i][j] <= strs[i + 1][j]:
    sorted_pairs[i] = True

# 正确：只有严格小于才确定有序
if strs[i][j] < strs[i + 1][j]:
    sorted_pairs[i] = True
```

### 错误3：删除列后没有正确更新检查列表

```python
# 错误：删除列后仍然更新check_list
for i in check_list:
    if strs[i][j] > strs[i + 1][j]:
        deleted += 1
        break
# 无论如何都更新check_list

# 正确：只有保留列时才更新
else:  # for循环正常结束（未break）
    # 更新check_list
```

### 错误4：列表截断方式错误

```python
# 错误：创建新列表（效率低）
new_list = []
for i in check_list:
    if strs[i][j] == strs[i + 1][j]:
        new_list.append(i)
check_list = new_list

# 正确：原地修改
new_size = 0
for i in check_list:
    if strs[i][j] == strs[i + 1][j]:
        check_list[new_size] = i
        new_size += 1
del check_list[new_size:]
```

### 错误5：没有理解for-else结构

```python
# 错误：不知道何时更新check_list
for i in check_list:
    if strs[i][j] > strs[i + 1][j]:
        deleted += 1
        break
# 这里怎么判断是否保留了列？

# 正确：使用for-else
for i in check_list:
    if strs[i][j] > strs[i + 1][j]:
        deleted += 1
        break
else:  # 循环正常结束，说明保留了列
    # 更新check_list
```

### 错误6：混淆行和列

```python
# 错误：遍历行而非列
for i in range(n):  # 错
    for j in range(m):
        ...

# 正确：外层遍历列
for j in range(m):  # 列
    for i in check_list:  # 行对
        ...
```

## 相关题目

- [0955. Delete Columns to Make Sorted II](./955_Delete Columns to Make Sorted II.md)
- [0944. Delete Columns to Make Sorted](./944_delete_columns_to_make_sorted.md) - 简化版
- [0960. Delete Columns to Make Sorted III](./960_delete_columns_to_make_sorted_iii.md) - 升级版（DP）
- [0014. Longest Common Prefix](./014_longest_common_prefix.md) - 字符串列比较
- [0451. Sort Characters By Frequency](./451_sort_characters_by_frequency.md) - 字符排序
