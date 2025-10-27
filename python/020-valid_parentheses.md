# Valid Parentheses

[[stack]]

## Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

**Example 1:**

```text
Input: s = "()"
Output: true
```

**Example 2:**

```text
Input: s = "()[]{}"
Output: true
```

**Example 3:**

```text
Input: s = "(]"
Output: false
```

**Example 4:**

```text
Input: s = "([])"
Output: true
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## 解法一：栈 + 哈希表（推荐）

```python
class Solution:
    def isValid(self, s: str) -> bool:
        """
        使用栈来匹配括号
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        # 右括号到左括号的映射
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            if char in mapping:  # 遇到右括号
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:  # 遇到左括号
                stack.append(char)
        
        # 栈为空说明所有括号都匹配
        return not stack
```

**复杂度分析**：

- 时间复杂度：O(n) - 需要遍历字符串一次
- 空间复杂度：O(n) - 最坏情况下栈存储所有左括号

## 解法二：优化版栈（简洁写法）

```python
class Solution:
    def isValid(self, s: str) -> bool:
        """
        更简洁的栈实现
        """
        mapping = {'}': '{', ')': '(', ']': '['}
        stack = []
        
        for char in s:
            if stack and char in mapping and stack[-1] == mapping[char]:
                stack.pop()  # 匹配成功，弹出左括号
            else:
                stack.append(char)  # 左括号入栈，或不匹配的右括号入栈
        
        return len(stack) == 0
```

**复杂度分析**：

- 时间复杂度：O(n) - 遍历字符串一次
- 空间复杂度：O(n) - 栈的空间

## 解法三：传统栈写法

```python
class Solution:
    def isValid(self, s: str) -> bool:
        """
        传统的栈实现方法
        """
        if len(s) % 2 == 1:  # 奇数长度必定不匹配
            return False
        
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in '([{':  # 左括号
                stack.append(char)
            elif char in ')]}':  # 右括号
                if not stack or stack.pop() != pairs[char]:
                    return False
        
        return len(stack) == 0
```

## 算法详解

### 核心思路

1. **栈的特性**：后进先出(LIFO)，天然适合处理嵌套结构
2. **匹配规则**：
   - 遇到左括号：入栈等待匹配
   - 遇到右括号：与栈顶元素比较
   - 匹配成功：弹出栈顶
   - 匹配失败：直接返回false
3. **最终检查**：栈为空说明完全匹配

### 处理流程

| 输入字符 | 操作 | 栈状态 |
|----------|------|--------|
| 左括号 | 入栈 | 等待匹配 |
| 右括号 | 检查栈顶并弹出 | 匹配则继续 |
| 栈空时遇右括号 | 返回false | 无法匹配 |
| 遍历结束栈非空 | 返回false | 有未匹配左括号 |

### 算法可视化

以 `"([{}])"` 为例：

```text
处理过程：
1. '(' → 入栈，stack: ['(']
2. '[' → 入栈，stack: ['(', '[']
3. '{' → 入栈，stack: ['(', '[', '{']
4. '}' → 匹配'{' 弹出，stack: ['(', '[']
5. ']' → 匹配'[' 弹出，stack: ['(']
6. ')' → 匹配'(' 弹出，stack: []

结果：栈为空，返回true
```

## 边界情况处理

1. **空字符串**：返回true（没有括号需要匹配）
2. **奇数长度**：直接返回false（无法完全匹配）
3. **只有左括号**：栈非空，返回false
4. **只有右括号**：栈空时遇右括号，返回false
5. **类型不匹配**：如"(]"，返回false

## 常见错误

1. **忘记检查栈是否为空**：在弹出前必须检查
2. **最后不检查栈状态**：遍历结束后栈必须为空
3. **括号类型判断错误**：要准确区分左右括号
4. **边界条件遗漏**：如空字符串的处理

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 栈+哈希表 | O(n) | O(n) | 清晰易懂，推荐 |
| 优化版栈 | O(n) | O(n) | 代码更简洁 |
| 传统栈 | O(n) | O(n) | 分类讨论更明确 |

## 关键要点

1. **栈的应用**：处理嵌套结构的经典数据结构
2. **哈希表优化**：快速查找对应的左括号类型
3. **边界检查**：栈空时不能弹出，遍历后栈必须为空
4. **提前优化**：奇数长度字符串可以直接返回false

## 相关题目

- [32. Longest Valid Parentheses](032_longest_valid_parentheses.md) - 最长有效括号
- [22. Generate Parentheses](022_generate_parentheses.md) - 生成括号
- [1541. Minimum Insertions to Balance a Parentheses String](1541_minimum_insertions_balance_parentheses.md) - 平衡括号字符串的最少插入次数

这道题是栈数据结构的经典入门题目，深刻理解其解法对掌握栈的应用场景非常重要。
