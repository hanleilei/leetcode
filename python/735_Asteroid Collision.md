# Asteroid Collision

[[stack]]

## Problem Description

We are given an array `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids
meet, the smaller one will explode. If both are the same size, both will
explode. Two asteroids moving in the same direction will never meet.

### Examples

**Example 1:**

```text
Input: asteroids = [5,10,-5]
Output: [5,10]

Explanation:
The 10 and -5 collide resulting in 10.
The 5 and 10 never collide (both moving right).
```

**Example 2:**

```text
Input: asteroids = [8,-8]
Output: []

Explanation:
The 8 and -8 collide exploding each other (same size).
```

**Example 3:**

```text
Input: asteroids = [10,2,-5]
Output: [10]

Explanation:
- The 2 and -5 collide → -5 survives
- The 10 and -5 collide → 10 survives
```

### Constraints

- 2 <= asteroids.length <= 10^4
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0

---

## 解法：单调栈模拟碰撞（最优✨）

```python
from typing import List

class Solution:
    """
    核心思想：
    1. 只有"右移→"遇到"←左移"才会碰撞
    2. 用栈维护当前存活的小行星
    3. 遇到左移小行星时，与栈顶右移小行星比较
    """
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        时间复杂度：O(n) - 每个元素最多入栈出栈一次
        空间复杂度：O(n) - 栈的空间
        """
        stack = []
        
        for ast in asteroids:
            # 情况1：右移小行星，直接入栈
            if ast > 0:
                stack.append(ast)
            else:
                # 情况2：左移小行星，需要检查碰撞
                # 当栈不为空 且 栈顶是右移 且 当前左移更大
                while stack and stack[-1] > 0 and abs(ast) > stack[-1]:
                    stack.pop()  # 栈顶右移小行星爆炸
                
                # 处理碰撞后的三种情况
                if not stack or stack[-1] < 0:
                    # 栈空 或 栈顶也是左移 → 不会碰撞，入栈
                    stack.append(ast)
                elif stack[-1] == abs(ast):
                    # 相同大小 → 都爆炸
                    stack.pop()
                # 否则：栈顶更大，当前小行星爆炸，不入栈
        
        return stack
```

这类stack的问题，就是各种的corner case要考虑。有点烦

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = list()
        for a in asteroids:
            while s and s[-1] > 0 and a < 0:
                if s[-1] + a < 0: s.pop()
                elif s[-1] + a > 0: break    
                else: s.pop(); break
            else: s.append(a)        
        return s
```

### 算法分析

```text
碰撞规则：
1. →→ 或 ←← ：同向不碰撞
2. ←→ ：背向不碰撞
3. →← ：相向碰撞！

关键观察：
- 只有栈顶是→，当前是←时才碰撞
- 栈顶是←时，新的←不会碰撞（同向）
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(n) |
| 数据结构 | 栈 |

---

## 执行流程示例

```text
Example: asteroids = [10, 2, -5]

步骤1：处理10
  10 > 0，入栈
  stack = [10]

步骤2：处理2
  2 > 0，入栈
  stack = [10, 2]

步骤3：处理-5
  -5 < 0，检查碰撞
  
  循环检查：
    - stack[-1]=2 > 0 且 |-5|=5 > 2
      → 弹出2
      stack = [10]
    
    - stack[-1]=10 > 0 且 |-5|=5 < 10
      → 退出循环
  
  stack[-1]=10 > 0 且 10 > |-5|
  → -5爆炸，不入栈

最终：stack = [10]
```

---

## 四种典型场景

### 场景1：全向右（无碰撞）

```python
asteroids = [5, 10, 15]
# 输出：[5, 10, 15]
# 分析：全部右移，依次入栈
```

### 场景2：全向左（无碰撞）

```python
asteroids = [-15, -10, -5]
# 输出：[-15, -10, -5]
# 分析：全部左移，依次入栈
```

### 场景3：右→左碰撞

```python
asteroids = [8, -8]
# 输出：[]
# 分析：8和-8碰撞，同时爆炸

asteroids = [10, -5]
# 输出：[10]
# 分析：10和-5碰撞，10胜出

asteroids = [5, -10]
# 输出：[-10]
# 分析：5和-10碰撞，-10胜出
```

### 场景4：左→右（背向，无碰撞）

```python
asteroids = [-5, 10]
# 输出：[-5, 10]
# 分析：-5向左，10向右，越走越远
```

---

## 常见错误

### 错误1：变量名错误（原代码bug）

```python
# ❌ 错误（原代码中的bug）
elif res[-1] == -i:  # res未定义
    stack.pop()

# ✓ 正确
elif stack[-1] == abs(ast):
    stack.pop()
```

### 错误2：没有处理相同大小

```python
# ❌ 错误
while stack and stack[-1] > 0 and abs(ast) >= stack[-1]:
    stack.pop()
# 问题：相同大小时，只弹出栈顶，但当前也应该不入栈

# ✓ 正确
while stack and stack[-1] > 0 and abs(ast) > stack[-1]:
    stack.pop()
if stack and stack[-1] == abs(ast):
    stack.pop()  # 相同大小都爆炸
```

### 错误3：忘记检查栈顶方向

```python
# ❌ 错误
while stack and abs(ast) > abs(stack[-1]):
    stack.pop()
# 问题：栈顶是左移时也会误判碰撞

# ✓ 正确
while stack and stack[-1] > 0 and abs(ast) > stack[-1]:
    stack.pop()
```

### 错误4：没有判断栈空

```python
# ❌ 错误
while stack[-1] > 0 and abs(ast) > stack[-1]:
    stack.pop()
# 问题：栈为空时访问stack[-1]会报错

# ✓ 正确
while stack and stack[-1] > 0 and abs(ast) > stack[-1]:
    stack.pop()
```

---

## 关键洞察

```text
为什么用栈？

1. 碰撞只会影响最近的小行星（栈顶）
2. 后进先出的特性完美匹配碰撞规则
3. 已处理的左移小行星不会再碰撞

时间复杂度为什么是O(n)？

虽然有while循环，但每个元素最多：
- 入栈一次
- 出栈一次
总操作次数 = 2n = O(n)
```

---

## 相关题目

- [[20. Valid Parentheses]] - 括号匹配（栈的基础应用）
- [[155. Min Stack]] - 最小栈
- [[394. Decode String]] - 字符串解码（栈处理嵌套）
- [[739. Daily Temperatures]] - 每日温度（单调栈）
- [[503. Next Greater Element II]] - 下一个更大元素II

