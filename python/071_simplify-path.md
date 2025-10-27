# Simplify Path

[[stack]] [[string]]

## Problem Description

Given a string `path`, which is an **absolute path** (starting with a slash `'/'`) to a file or directory in a Unix-style file system, convert it to the simplified **canonical path**.

In a Unix-style file system, a period `'.'` refers to the current directory, a double period `'..'` refers to the directory up a level, and any multiple consecutive slashes (i.e. `'//'`) are treated as a single slash `'/'`. For this problem, any other format of periods such as `'...'` are treated as file/directory names.

The **canonical path** should have the following format:

- The path starts with a single slash `'/'`.
- Any two directories are separated by a single slash `'/'`.
- The path does not end with a trailing `'/'`.
- The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period `'.'` or double period `'..'`)

Return the simplified **canonical path**.

## Examples

**Example 1:**

```text
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
```

**Example 2:**

```text
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
```

**Example 3:**

```text
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
```

**Example 4:**

```text
Input: path = "/a/./b/../../c/"
Output: "/c"
```

## Constraints

- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, `'.'`, `'/'` or `'_'`.
- `path` is a valid absolute Unix path.

## 解法一：栈 + 字符串分割（推荐）

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        使用栈处理路径简化
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        # 按 '/' 分割路径，得到所有目录名
        components = path.split('/')
        stack = []
        
        for component in components:
            if component == '..':
                # 返回上级目录，如果栈不为空则弹出
                if stack:
                    stack.pop()
            elif component and component != '.':
                # 有效的目录名，入栈
                # 忽略空字符串（连续斜杠）和当前目录'.'
                stack.append(component)
        
        # 构建简化后的路径
        return '/' + '/'.join(stack)
```

**复杂度分析**：

- 时间复杂度：O(n) - n为路径长度，需要遍历所有字符
- 空间复杂度：O(n) - 栈的空间和分割后的组件数组

## 解法二：使用标准库（简洁但不推荐面试）

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        使用Python标准库os.path.abspath
        注意：面试中通常不允许使用标准库解决问题
        """
        import os
        return os.path.abspath(path)
```

**复杂度分析**：

- 时间复杂度：O(n) - 内部实现类似解法一
- 空间复杂度：O(n) - 内部需要存储处理过程

## 解法三：手动遍历（详细版本）

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        手动处理每个字符，更详细的实现
        """
        stack = []
        i = 0
        n = len(path)
        
        while i < n:
            # 跳过连续的斜杠
            if path[i] == '/':
                i += 1
                continue
            
            # 收集当前目录名
            start = i
            while i < n and path[i] != '/':
                i += 1
            
            component = path[start:i]
            
            if component == '..':
                # 返回上级目录
                if stack:
                    stack.pop()
            elif component != '.':
                # 有效目录名
                stack.append(component)
        
        return '/' + '/'.join(stack)
```

## 算法详解

### 核心思路

1. **分割处理**：将路径按 `'/'` 分割成组件
2. **栈操作**：
   - 遇到 `'..'`：弹出栈顶（返回上级）
   - 遇到 `'.'` 或空字符串：忽略
   - 遇到有效目录名：入栈
3. **重构路径**：用 `'/'` 连接栈中所有元素

### 处理规则

| 组件类型 | 处理方式 | 说明 |
|----------|----------|------|
| `".."` | `stack.pop()` | 返回上级目录 |
| `"."` | 忽略 | 当前目录 |
| 空字符串 | 忽略 | 连续斜杠产生 |
| 有效名称 | `stack.append()` | 进入子目录 |

### 算法可视化

以 `"/a/./b/../../c/"` 为例：

```text
分割后：["", "a", ".", "b", "..", "..", "c", ""]

处理过程：
1. "" → 忽略，stack: []
2. "a" → 入栈，stack: ["a"]
3. "." → 忽略，stack: ["a"]
4. "b" → 入栈，stack: ["a", "b"]
5. ".." → 弹栈，stack: ["a"]
6. ".." → 弹栈，stack: []
7. "c" → 入栈，stack: ["c"]
8. "" → 忽略，stack: ["c"]

结果："/c"
```

## 边界情况处理

1. **根目录上级**：`"/../"` → `"/"`（栈为空时不能再弹出）
2. **连续斜杠**：`"/home//foo/"` → `"/home/foo"`（忽略空组件）
3. **当前目录**：`"/a/./b"` → `"/a/b"`（忽略"."）
4. **仅根目录**：`"/"` → `"/"`

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 栈+分割 | O(n) | O(n) | 清晰简洁，推荐 |
| 标准库 | O(n) | O(n) | 简单但不适合面试 |
| 手动遍历 | O(n) | O(n) | 更好理解内部逻辑 |

## 关键要点

1. **栈的使用**：天然适合处理目录的进入和返回
2. **字符串分割**：简化处理逻辑，避免手动字符遍历
3. **边界处理**：注意根目录不能再向上，空组件要忽略
4. **路径重构**：最后用 `'/'` 连接所有有效组件

## 相关题目

- [20. Valid Parentheses](020_valid_parentheses.md) - 栈的经典应用
- [150. Evaluate Reverse Polish Notation](150_evaluate_reverse_polish_notation.md) - 栈处理表达式
- [224. Basic Calculator](224_basic_calculator.md) - 栈处理计算

这道题是栈数据结构的典型应用，通过栈来模拟文件系统的目录导航过程，是理解栈特性的好例子。
