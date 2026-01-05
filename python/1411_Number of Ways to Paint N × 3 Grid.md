# 1411. Number of Ways to Paint N × 3 Grid

## 问题描述

You have a `grid` of size `n x 3` and you want to paint each cell of the
grid with exactly one of the three colors: **Red**, **Yellow**, or **Green**
while making sure that no two adjacent cells have the same color (i.e., no
two cells that share vertical or horizontal sides have the same color).

Given `n` the number of rows of the grid, return the number of ways you
can paint this grid. As the answer may grow large, the answer must be
computed modulo $10^9 + 7$.

## 示例

**Example 1:**

![Grid Example](https://assets.leetcode.com/uploads/2020/03/26/e1.png)

```text
Input: n = 1
Output: 12
```

Explanation: There are 12 possible ways to paint the grid as shown.

**Example 2:**

```text
Input: n = 2
Output: 54
```

**Example 3:**

```text
Input: n = 5000
Output: 30228214
```

## 约束条件

- $n == \text{grid.length}$
- $1 \le n \le 5000$

## 解法

### 方法1：动态规划（状态分类）推荐

将一行的涂色方案分为两类：ABA型（121型）和ABC型（123型）。

```python
class Solution:
    def numOfWays(self, n: int) -> int:
        """
        DP - 状态分类
        
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        MOD = 10**9 + 7
        
        # 初始状态：第一行
        # type_121: ABA型（如RYR, GYG等），共6种
        # type_123: ABC型（如RGB, RGY等），共6种
        type_121 = 6
        type_123 = 6
        
        # 从第2行开始递推
        for i in range(n - 1):
            # 新的ABA型可以由：
            # - 上一行ABA型转换而来（3种方式）
            # - 上一行ABC型转换而来（2种方式）
            new_121 = (type_121 * 3 + type_123 * 2) % MOD
            
            # 新的ABC型可以由：
            # - 上一行ABA型转换而来（2种方式）
            # - 上一行ABC型转换而来（2种方式）
            new_123 = (type_121 * 2 + type_123 * 2) % MOD
            
            type_121, type_123 = new_121, new_123
        
        return (type_121 + type_123) % MOD
```

### 方法2：DP优化（滚动变量）

使用临时变量避免同时更新。

```python
class Solution:
    def numOfWays(self, n: int) -> int:
        """
        DP - 滚动变量优化
        
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        MOD = 10**9 + 7
        
        # f0: ABA型，f1: ABC型
        f0 = f1 = 6
        
        for _ in range(n - 1):
            # 使用临时变量
            g0 = (3 * f0 + 2 * f1) % MOD
            g1 = (2 * f0 + 2 * f1) % MOD
            f0, f1 = g0, g1
        
        return (f0 + f1) % MOD
```

### 方法3：矩阵快速幂

使用矩阵快速幂加速递推。

```python
class Solution:
    def numOfWays(self, n: int) -> int:
        """
        矩阵快速幂
        
        时间复杂度：O(log n)
        空间复杂度：O(1)
        """
        MOD = 10**9 + 7
        
        def matrix_multiply(A, B):
            """2x2矩阵乘法"""
            return [
                [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
                 (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
                [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
                 (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
            ]
        
        def matrix_pow(matrix, exp):
            """矩阵快速幂"""
            if exp == 0:
                return [[1, 0], [0, 1]]  # 单位矩阵
            
            result = [[1, 0], [0, 1]]
            base = matrix
            
            while exp > 0:
                if exp % 2 == 1:
                    result = matrix_multiply(result, base)
                base = matrix_multiply(base, base)
                exp //= 2
            
            return result
        
        if n == 1:
            return 12
        
        # 转移矩阵
        # [type_121']   [3 2]   [type_121]
        # [type_123'] = [2 2] × [type_123]
        transition = [[3, 2], [2, 2]]
        
        # 计算转移矩阵的n-1次幂
        result_matrix = matrix_pow(transition, n - 1)
        
        # 初始状态 [6, 6]
        type_121 = (result_matrix[0][0] * 6 + result_matrix[0][1] * 6) % MOD
        type_123 = (result_matrix[1][0] * 6 + result_matrix[1][1] * 6) % MOD
        
        return (type_121 + type_123) % MOD
```

### 方法4：递推数学公式（找规律）

通过递推关系找出通项公式。

```python
class Solution:
    def numOfWays(self, n: int) -> int:
        """
        递推找规律
        
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        MOD = 10**9 + 7
        
        # dp[i][0]: 第i行为ABA型的方案数
        # dp[i][1]: 第i行为ABC型的方案数
        prev_aba, prev_abc = 6, 6
        
        for i in range(2, n + 1):
            curr_aba = (3 * prev_aba + 2 * prev_abc) % MOD
            curr_abc = (2 * prev_aba + 2 * prev_abc) % MOD
            prev_aba, prev_abc = curr_aba, curr_abc
        
        return (prev_aba + prev_abc) % MOD
```

## 算法分析

### 核心思想详解

**状态分类**：

一行的涂色方案可分为两类：

1. **ABA型（121型）**：左右两端颜色相同
   - 示例：RYR, RGR, GYG, GRG, YRY, YGY
   - 总共：6种

2. **ABC型（123型）**：三个颜色都不同
   - 示例：RGB, RBG, GRB, GBR, BRG, BGR
   - 总共：6种

**状态转移**：

当前行与上一行的关系：

```text
上一行: ABA型 (例如 R Y R)
        ↓
当前行可以是:
1. ABA型: G R G, G Y G, B R B (3种)
2. ABC型: G R B, B R G (2种)

上一行: ABC型 (例如 R G B)
        ↓
当前行可以是:
1. ABA型: G Y G, B Y B (2种)
2. ABC型: G R Y, B R Y (2种)
```

**递推公式**：

```python
type_121[i] = 3 × type_121[i-1] + 2 × type_123[i-1]
type_123[i] = 2 × type_121[i-1] + 2 × type_123[i-1]
```

**为什么是这些系数？**

以 ABA → ABA 为例（上一行RYR）：

```text
R Y R
↓ ↓ ↓
G R G ✓ (第一列R→G，第二列Y→R，第三列R→G)
G Y G ✓ (第一列R→G，第二列Y→Y，第三列R→G)
B R B ✓ (第一列R→B，第二列Y→R，第三列R→B)
共3种
```

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| DP状态分类 | O(n) | O(1) | 最直观 |
| 滚动变量 | O(n) | O(1) | 代码简洁 |
| 矩阵快速幂 | O(log n) | O(1) | 大数据最优 |
| 递推公式 | O(n) | O(1) | 易理解 |

### 执行过程示例

以 `n = 3` 为例：

**初始状态（n=1）**：

```text
第1行:
  ABA型: 6种 (RYR, RGR, GYG, GRG, YRY, YGY)
  ABC型: 6种 (RGB, RGY, RBG, RBY, GRB, GRY, ...)
  总计: 12种
```

**第2行（n=2）**：

```text
从ABA型(6种)转移:
  → 新ABA型: 6 × 3 = 18种
  → 新ABC型: 6 × 2 = 12种

从ABC型(6种)转移:
  → 新ABA型: 6 × 2 = 12种
  → 新ABC型: 6 × 2 = 12种

第2行总计:
  ABA型: 18 + 12 = 30种
  ABC型: 12 + 12 = 24种
  总计: 54种
```

**第3行（n=3）**：

```text
从ABA型(30种)转移:
  → 新ABA型: 30 × 3 = 90种
  → 新ABC型: 30 × 2 = 60种

从ABC型(24种)转移:
  → 新ABA型: 24 × 2 = 48种
  → 新ABC型: 24 × 2 = 48种

第3行总计:
  ABA型: 90 + 48 = 138种
  ABC型: 60 + 48 = 108种
  总计: 246种
```

**可视化表格**：

| 行数 | ABA型方案数 | ABC型方案数 | 总方案数 | 计算过程 |
|------|------------|------------|---------|---------|
| 1 | 6 | 6 | 12 | 初始状态 |
| 2 | 30 | 24 | 54 | 3×6+2×6, 2×6+2×6 |
| 3 | 138 | 108 | 246 | 3×30+2×24, 2×30+2×24 |
| 4 | 630 | 492 | 1122 | 3×138+2×108, 2×138+2×108 |

**具体转移示例**：

```text
第1行: R Y R (ABA型)
        ↓
第2行可能的ABA型:
  G R G (R≠G, Y≠R, R≠G) ✓
  G Y G (R≠G, Y=Y, R≠G) ✓
  B R B (R≠B, Y≠R, R≠B) ✓

第2行可能的ABC型:
  G R B (R≠G, Y≠R, R≠B) ✓
  B R G (R≠B, Y≠R, R≠G) ✓
```

## 常见错误

### 错误1：状态分类不清

```python
# 错误：没有区分ABA和ABC类型
dp = 12
for i in range(n - 1):
    dp = dp * 5  # 错误的递推关系

# 正确：分两种状态
type_121 = type_123 = 6
for i in range(n - 1):
    type_121, type_123 = (
        type_121 * 3 + type_123 * 2,
        type_121 * 2 + type_123 * 2
    )
```

### 错误2：同时更新变量

```python
# 错误：同时更新导致使用了新值
for _ in range(n - 1):
    type_121 = type_121 * 3 + type_123 * 2
    type_123 = type_121 * 2 + type_123 * 2  # 使用了新的type_121

# 正确：使用临时变量或元组赋值
for _ in range(n - 1):
    new_121 = type_121 * 3 + type_123 * 2
    new_123 = type_121 * 2 + type_123 * 2
    type_121, type_123 = new_121, new_123
```

### 错误3：忘记取模

```python
# 错误：只在最后取模
type_121, type_123 = 6, 6
for i in range(n - 1):
    type_121 = type_121 * 3 + type_123 * 2
    type_123 = type_121 * 2 + type_123 * 2
return (type_121 + type_123) % MOD  # 可能已经溢出

# 正确：每步都取模
for i in range(n - 1):
    type_121 = (type_121 * 3 + type_123 * 2) % MOD
    type_123 = (type_121 * 2 + type_123 * 2) % MOD
```

### 错误4：初始状态错误

```python
# 错误：初始状态不对
type_121 = 3  # 只有3种颜色
type_123 = 3

# 正确：第一行有6种ABA型和6种ABC型
type_121 = 6  # RYR, RGR, GYG, GRG, YRY, YGY
type_123 = 6  # RGB, RGY, RBG, RBY, GRB, GRY等
```

### 错误5：转移系数错误

```python
# 错误：系数不对
new_121 = type_121 * 2 + type_123 * 3  # 系数反了
new_123 = type_121 * 3 + type_123 * 2

# 正确：
new_121 = type_121 * 3 + type_123 * 2
new_123 = type_121 * 2 + type_123 * 2
```

### 错误6：边界情况未处理

```python
# 错误：n=1时没有特殊处理
def numOfWays(self, n: int) -> int:
    type_121 = type_123 = 6
    for i in range(n - 1):  # n=1时，range(0)不执行
        ...
    return (type_121 + type_123) % MOD

# 其实这个是对的！但如果使用数组可能出错
# 错误示例：
dp = [[0, 0] for _ in range(n + 1)]
# 需要处理dp[1]的初始化
```

## 相关题目

- [0070. Climbing Stairs](./070_climbing_stairs.md) - 基础DP递推
- [0746. Min Cost Climbing Stairs](./746_min_cost_climbing_stairs.md) - DP状态转移
- [0509. Fibonacci Number](./509_Fibonacci_Number.md) - 递推关系
- [1269. Number of Ways to Stay in the Same Place After Some Steps](./1269_number_of_ways_to_stay_in_the_same_place.md) - 计数DP
- [0790. Domino and Tromino Tiling](./790_domino_and_tromino_tiling.md) - 类似状态分类问题
