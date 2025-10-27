# Number of Laser Beams in a Bank

[[array]] [[string]] [[math]]

## Problem Description

Anti-theft security devices are activated inside a bank. You are given a **0-indexed** binary string array `bank` representing the floor plan of the bank, which is an `m x n` 2D matrix. `bank[i]` represents the `ith` row, consisting of `'0'`s and `'1'`s. `'0'` means the cell is empty, while `'1'` means the cell has a security device.

There is **one laser beam** between any two security devices **if both conditions are met**:

- The two devices are located on **two different rows**: `r1` and `r2`, where `r1 < r2`.
- For each row `i` where `r1 < i < r2`, there are **no security devices** in the `ith` row.

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return _the total number of laser beams in the bank_.

## Examples

**Example 1:**

![Laser Beams Example 1](https://assets.leetcode.com/uploads/2021/12/24/laser1.jpg)

```text
Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.
```

**Example 2:**

![Laser Beams Example 2](https://assets.leetcode.com/uploads/2021/12/24/laser2.jpg)

```text
Input: bank = ["000","111","000"]
Output: 0
Explanation: There does not exist two devices located on two different rows.
```

## Constraints

- `m == bank.length`
- `n == bank[i].length`
- `1 <= m, n <= 500`
- `bank[i][j]` is either `'0'` or `'1'`.

## 解法一：一次遍历（推荐）

```python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        一次遍历解法，记录前一行设备数量
        时间复杂度：O(m*n)，空间复杂度：O(1)
        """
        result = 0
        prev_devices = 0  # 记录前一行有设备的行中的设备数量
        
        for row in bank:
            current_devices = row.count('1')  # 当前行设备数量
            
            if current_devices > 0:  # 如果当前行有设备
                result += prev_devices * current_devices  # 与前一行形成的激光束
                prev_devices = current_devices  # 更新前一行设备数量
        
        return result
```

**复杂度分析**：

- 时间复杂度：O(m × n) - 需要遍历所有字符统计设备数量
- 空间复杂度：O(1) - 只使用常数额外空间

## 解法二：预处理 + 计算（清晰版本）

```python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        先预处理出所有有设备的行，再计算激光束数量
        时间复杂度：O(m*n)，空间复杂度：O(m)
        """
        # 统计每行有设备的行的设备数量
        device_counts = [row.count('1') for row in bank if row.count('1') > 0]
        
        # 计算相邻有设备行之间的激光束数量
        total_beams = 0
        for i in range(len(device_counts) - 1):
            total_beams += device_counts[i] * device_counts[i + 1]
        
        return total_beams
```

**复杂度分析**：

- 时间复杂度：O(m × n) - 遍历所有字符统计，再遍历有设备的行
- 空间复杂度：O(m) - 最坏情况存储所有行的设备数量

## 解法三：列表推导式（简洁版本）

```python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        使用列表推导式的简洁写法
        """
        # 获取所有有设备的行的设备数量
        devices = [row.count('1') for row in bank if row.count('1') > 0]
        
        # 计算相邻行之间的激光束总数
        return sum(devices[i] * devices[i + 1] for i in range(len(devices) - 1))
```

## 算法详解

### 核心思路

1. **理解题意**：
   - 激光束只能在不同行的设备之间形成
   - 两行之间不能有其他包含设备的行
   - 实际上就是计算相邻的"有设备行"之间的设备对数

2. **简化问题**：
   - 忽略没有设备的行（它们不影响结果）
   - 只考虑连续的有设备的行
   - 相邻两行设备数量的乘积就是它们之间的激光束数

3. **计算方法**：
   - 如果第i行有a个设备，第j行有b个设备
   - 且i、j行之间没有其他有设备的行
   - 则i、j行之间的激光束数量为 a × b

### 算法可视化

以 `["011001","000000","010100","001000"]` 为例：

```text
原始矩阵：
行0: "011001" → 3个设备 (位置1,2,5)
行1: "000000" → 0个设备 (忽略)
行2: "010100" → 2个设备 (位置1,3)
行3: "001000" → 1个设备 (位置2)

有设备的行: [3, 2, 1]

计算激光束：
- 行0与行2之间: 3 × 2 = 6条激光束
- 行2与行3之间: 2 × 1 = 2条激光束
- 总计: 6 + 2 = 8条激光束
```

### 详细分析

**为什么忽略无设备的行？**

- 无设备的行不会产生激光束
- 无设备的行不会阻断激光束（题目条件）
- 只有有设备的行才需要考虑

**为什么是相邻有设备行的乘积？**

- 每个设备都会与下一个有设备行的每个设备形成一条激光束
- n个设备与m个设备之间共有n×m条激光束

## 边界情况

1. **只有一行有设备**：返回0（无法形成激光束）
2. **所有行都没有设备**：返回0
3. **连续多行都有设备**：每相邻两行都会产生激光束
4. **中间有很多空行**：不影响结果，忽略即可

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 一次遍历 | O(m×n) | O(1) | 最优解，推荐 |
| 预处理+计算 | O(m×n) | O(m) | 逻辑清晰，易理解 |
| 列表推导式 | O(m×n) | O(m) | 代码简洁，Pythonic |

## 关键要点

1. **问题转化**：将2D问题转化为1D问题（只关注行）
2. **状态压缩**：只需要记录前一行的设备数量
3. **乘法原理**：n×m表示n个元素与m个元素的所有配对数
4. **过滤思维**：忽略无关的空行，只处理有效数据

## 相关题目

- [1252. Cells with Odd Values in a Matrix](1252_cells_odd_values_matrix.md) - 矩阵中奇数值单元格的数目
- [1572. Matrix Diagonal Sum](1572_matrix_diagonal_sum.md) - 矩阵对角线元素的和
- [1582. Special Positions in a Binary Matrix](1582_special_positions_binary_matrix.md) - 二进制矩阵中的特殊位置

这道题是一个很好的阅读理解题，关键是要理解题目的本质：计算相邻有设备行之间设备对的数量。
