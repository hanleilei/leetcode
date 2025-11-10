# Count Operations to Obtain Zero

[[math]] [[simulation]] [[gcd]]

## Problem Description

You are given two non-negative integers num1 and num2.

In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

Return the number of operations required to make either num1 = 0 or num2 = 0.

### Examples

**Example 1:**

```text
Input: num1 = 2, num2 = 3
Output: 3

Explanation:
- Operation 1: num1 = 2, num2 = 3
  Since num1 < num2, subtract num1 from num2
  Result: num1 = 2, num2 = 1

- Operation 2: num1 = 2, num2 = 1
  Since num1 > num2, subtract num2 from num1
  Result: num1 = 1, num2 = 1

- Operation 3: num1 = 1, num2 = 1
  Since num1 == num2, subtract num2 from num1
  Result: num1 = 0, num2 = 1

Total operations: 3
```

**Example 2:**

```text
Input: num1 = 10, num2 = 10
Output: 1

Explanation:
- Operation 1: num1 = 10, num2 = 10
  Since num1 == num2, subtract num2 from num1
  Result: num1 = 0, num2 = 10

Total operations: 1
```

### Constraints

- 0 <= num1, num2 <= 10^5

---

## 解法：数学优化（最优✨）

```python
class Solution:
    """
    优化思路：识别欧几里得算法的模式

    反复相减等价于一次模运算：
    num1 // num2 次减法可以用一个操作完成
    """

    def countOperations(self, num1: int, num2: int) -> int:
        """
        通过数学优化计算操作次数

        时间复杂度：O(log(min(num1, num2))) - 与GCD算法相同
        空间复杂度：O(1)
        """
        count = 0

        while num1 != 0 and num2 != 0:
            # 关键优化：如果num1 >= num2
            # 反复减num2直到num1 < num2
            # 等价于num1 // num2次操作
            count += num1 // num2

            # 模运算得到余数（相当于最后一次减法的结果）
            num1 %= num2

            # 交换，继续处理另一对数
            num1, num2 = num2, num1

        return count
```

**算法分析：**

```text
核心思想：识别欧几里得算法

直观方法：
  num1=5, num2=3
  5 >= 3? 减 → 2, 3  (1次)
  2 >= 3? 否，交换 → 3, 2
  3 >= 2? 减 → 1, 2  (1次)
  1 >= 2? 否，交换 → 2, 1
  2 >= 1? 减 → 1, 1  (1次)
  1 >= 1? 减 → 0, 1  (1次)
  总：4次

优化方法：
  num1=5, num2=3
  5 // 3 = 1 次减法 → (2, 3)
  3 // 2 = 1 次减法 → (1, 2)
  2 // 1 = 2 次减法 → (0, 1)
  总：1 + 1 + 2 = 4次 ✓

模式识别：这就是GCD算法！
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(log(min(num1, num2))) |
| 空间复杂度 | O(1) |
| 是否需要额外空间 | 否 |

---

## 算法原理

### 关键观察

```python
# 如果num1 >= num2
# 反复执行: num1 = num1 - num2
# 可以一次性计算为: num1 // num2 次操作

# 剩余的值: num1 % num2
# 对应最后一次不足以再减的值
```

### 与欧几里得算法的联系

```text
欧几里得GCD算法：
  gcd(a, b) = gcd(b, a % b)
  直到b = 0

本题算法：
  count += num1 // num2
  num1 %= num2
  交换两数
  直到num1或num2为0

关键区别：本题计数每次除法运算的商
```

### 执行流程示例

```text
num1 = 2, num2 = 3

迭代1：
  2 < 3，但算法检查 num1 // num2 = 2 // 3 = 0
  count += 0
  num1 %= 3 → 2
  交换 → num1 = 3, num2 = 2

迭代2：
  3 // 2 = 1
  count += 1 (总计: 1)
  num1 %= 2 → 1
  交换 → num1 = 2, num2 = 1

迭代3：
  2 // 1 = 2
  count += 2 (总计: 3)
  num1 %= 1 → 0
  交换 → num1 = 1, num2 = 0
  (num2 = 0，结束)

返回 3 ✓
```

---

## 对比解法

### 解法1：直接模拟（易理解但低效）

```python
def countOperations(self, num1: int, num2: int) -> int:
    """直接模拟每次操作"""
    count = 0
    while num1 > 0 and num2 > 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count
```

**复杂度：** O(max(num1, num2)) - 最坏情况很慢

```text
例：num1 = 100000, num2 = 1
需要100000次操作！
```

### 解法2：数学优化（推荐）

```python
def countOperations(self, num1: int, num2: int) -> int:
    """利用除法优化"""
    count = 0
    while num1 != 0 and num2 != 0:
        count += num1 // num2
        num1, num2 = num2, num1 % num2
    return count
```

**复杂度：** O(log(min(num1, num2))) - 快速

| 数据 | 解法1 | 解法2 |
|------|-------|-------|
| num1 = 2, num2 = 3 | 3次循环 | 3次循环 |
| num1 = 100000, num2 = 1 | 100000次循环 | 1次循环 |
| num1 = 10^5, num2 = 10^5-1 | ~10^5次 | ~20次 |

---

## 常见错误

### 错误1：直接使用减法（超时）

```python
# ❌ TLE（Time Limit Exceeded）
def countOperations(self, num1: int, num2: int) -> int:
    count = 0
    while num1 > 0 and num2 > 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count

# 问题：如果num1 = 100000, num2 = 1
# 需要99999次减法操作才能使num1 = 1
```

### 错误2：错误的初始化条件

```python
# ❌ 错误
while num1 > 0 or num2 > 0:  # 用or不对
    ...

# ✓ 正确
while num1 > 0 and num2 > 0:  # 用and，至少一个为0就停止
    ...
```

### 错误3：交换顺序错误

```python
# ❌ 错误
num1 %= num2
num2 = num1  # 错误交换
num1 = num2

# ✓ 正确
num1, num2 = num2, num1 % num2
# 或
temp = num1 % num2
num1 = num2
num2 = temp
```

### 错误4：忘记计数

```python
# ❌ 错误
while num1 != 0 and num2 != 0:
    num1, num2 = num2, num1 % num2
    # 漏了 count += num1 // num2

# ✓ 正确
while num1 != 0 and num2 != 0:
    count += num1 // num2
    num1, num2 = num2, num1 % num2
```

---

## 测试用例

```python
# 基本测试
assert Solution().countOperations(2, 3) == 3
assert Solution().countOperations(10, 10) == 1

# 边界情况
assert Solution().countOperations(0, 0) == 0
assert Solution().countOperations(1, 0) == 0
assert Solution().countOperations(0, 1) == 0

# 大数差异
assert Solution().countOperations(100000, 1) == 100000
assert Solution().countOperations(100000, 99999) == 100000

# 互质数
assert Solution().countOperations(7, 5) == 5

# 倍数关系
assert Solution().countOperations(12, 3) == 4
```

---

## 相关题目

- [[69. Sqrt(x)]] - 求平方根（二分法）
- [[372. Super Pow]] - 超级幂（数学优化）
- [[233. Number of Digit One]] - 数字1的个数
- [[202. Happy Number]] - 快乐数
- [[1071. Greatest Common Divisor of Strings]] - 字符串的最大公因子
