# Longest Absolute File Path

[[stack]] [[string]] [[simulation]]

## Problem Description

Suppose we have a file system represented by a string in the following manner:

The string `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` represents:

```text
dir
    subdir1
    subdir2
        file.ext
```

The directory `dir` contains an empty sub-directory `subdir1` and a sub-directory `subdir2` containing a file `file.ext`.

The string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` represents:

```text
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```

The directory `dir` contains two sub-directories `subdir1` and `subdir2`. `subdir1` contains a file `file1.ext` and an empty second-level sub-directory `subsubdir1`. `subdir2` contains a second-level sub-directory `subsubdir2` containing a file `file2.ext`.

We are interested in finding the **longest** (number of characters) **absolute path** to a file within our file system. For example, in the second example above, the longest absolute path is `"dir/subdir2/subsubdir2/file2.ext"`, and its length is `32` (not including the double quotes).

Given a string `input` representing the file system in the above format, return _the length of the **longest absolute path** to a file in the abstracted file system_. If there is no file in the system, return `0`.

**Note:**

- The name of a file contains at least a period `'.'` and an extension.
- The name of a directory or sub-directory will not contain a period `'.'`.

## Examples

**Example 1:**

```text
Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Output: 20
Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.
```

**Example 2:**

```text
Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Output: 32
Explanation: We have two files:
"dir/subdir1/file1.ext" of length 21
"dir/subdir2/subsubdir2/file2.ext" of length 32.
We return 32 since it is the longer one.
```

**Example 3:**

```text
Input: input = "a"
Output: 0
Explanation: We do not have any files, just a single directory named "a".
```

## Constraints

- `1 <= input.length <= 10^4`
- `input` may contain lowercase or uppercase English letters, digits, `'.'`, `'/'`, `'\n'`, and `'\t'`.
- All file and directory names have positive length.

## 解法一：栈 + 路径长度记录（推荐）

首先将字符串以'\n'进行分割，得到目录/文件的列表，记为parts

然后统计各目录/文件中'\t'的个数，表示当前目录/文件的深度

遍历parts，若栈顶元素的深度不小于parts的深度，则弹出栈顶元素，重复此过程。

然后将新的深度压入栈中，顺便统计当前目录的总长度。

下面的代码十分简洁明了，来自于链接地址：https://discuss.leetcode.com/topic/55097/simple-python-solution

```python
class Solution:
    def lengthLongestPath(self, s: str) -> int:
        """
        使用栈记录每层目录的累计长度
        时间复杂度：O(n)，空间复杂度：O(d) - d为最大深度
        """
        max_length = 0
        # path_lengths[depth] 表示深度为depth时的路径总长度
        path_lengths = {0: 0}  # 根目录深度为0，长度为0
        
        for line in s.splitlines():
            # 去除制表符，获取实际的文件/目录名
            name = line.lstrip('\t')
            # 计算当前层级的深度（制表符数量）
            depth = len(line) - len(name)
            
            if '.' in name:  # 是文件
                # 计算当前文件的绝对路径长度
                current_length = path_lengths[depth] + len(name)
                max_length = max(max_length, current_length)
            else:  # 是目录
                # 更新下一层的路径长度（加上当前目录名和分隔符'/'）
                path_lengths[depth + 1] = path_lengths[depth] + len(name) + 1
        
        return max_length
```

```python
class Solution:
    def lengthLongestPath(self, s: str) -> int:
        stk = []
        max_len = 0

        for part in s.split("\n"):
            level = part.rfind("\t") + 1

            while level < len(stk):
                stk.pop()
            stk.append(len(part) - level)
            
            if '.' in part:
                total_length = sum(stk) + len(stk) - 1
                max_len = max(max_len, total_length)
        return max_len
```

**复杂度分析**：

- 时间复杂度：O(n) - n为输入字符串长度，每个字符最多访问一次
- 空间复杂度：O(d) - d为目录的最大深度

## 解法二：显式栈实现

```python
class Solution:
    def lengthLongestPath(self, s: str) -> int:
        """
        使用显式栈维护路径
        更直观但空间复杂度稍高
        """
        max_length = 0
        stack = []  # 栈中存储 (深度, 累计长度)
        
        for line in s.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            
            # 弹出深度大于等于当前深度的栈顶元素
            while stack and stack[-1][0] >= depth:
                stack.pop()
            
            # 计算当前路径的累计长度
            current_length = (stack[-1][1] if stack else 0) + len(name)
            
            if '.' in name:  # 是文件
                max_length = max(max_length, current_length)
            else:  # 是目录
                # 将当前目录信息入栈（加上分隔符长度）
                stack.append((depth, current_length + 1))
        
        return max_length
```

## 解法三：递归解析（理解版本）

```python
class Solution:
    def lengthLongestPath(self, s: str) -> int:
        """
        递归解析文件系统结构
        帮助理解问题本质
        """
        def parse_level(lines, index, depth):
            """解析指定深度的目录结构"""
            max_len = 0
            current_path_len = 0
            
            while index < len(lines):
                line = lines[index]
                name = line.lstrip('\t')
                line_depth = len(line) - len(name)
                
                if line_depth < depth:
                    # 返回上一层
                    break
                elif line_depth > depth:
                    # 跳过更深层的内容（会在递归中处理）
                    index += 1
                    continue
                
                if '.' in name:  # 文件
                    max_len = max(max_len, current_path_len + len(name))
                else:  # 目录
                    # 递归处理子目录
                    sub_max, index = parse_level(
                        lines, index + 1, depth + 1
                    )
                    if sub_max > 0:  # 子目录中有文件
                        max_len = max(max_len, current_path_len + len(name) + 1 + sub_max)
                    continue
                
                index += 1
            
            return max_len, index
        
        lines = s.splitlines()
        result, _ = parse_level(lines, 0, 0)
        return result
```

## 算法详解

### 核心思路

1. **层级解析**：通过制表符数量确定文件/目录的深度
2. **路径长度追踪**：维护每个深度级别的累计路径长度
3. **文件识别**：通过是否包含'.'来区分文件和目录
4. **动态更新**：遇到文件时计算路径长度，遇到目录时更新下层路径基础

### 算法可视化

以 `"dir\n\tsubdir1\n\t\tfile1.ext\n\tsubdir2\n\t\tfile2.ext"` 为例：

```text
解析过程：

1. "dir" (depth=0, directory)
   path_lengths = {0: 0, 1: 4}  # "dir" + "/"

2. "\tsubdir1" (depth=1, directory)  
   path_lengths = {0: 0, 1: 4, 2: 12}  # "dir/" + "subdir1" + "/"

3. "\t\tfile1.ext" (depth=2, file)
   current_length = 12 + 9 = 21  # "dir/subdir1/file1.ext"
   max_length = max(0, 21) = 21

4. "\tsubdir2" (depth=1, directory)
   path_lengths = {0: 0, 1: 4, 2: 12}  # 更新为 "dir/" + "subdir2" + "/"

5. "\t\tfile2.ext" (depth=2, file)  
   current_length = 12 + 9 = 21  # "dir/subdir2/file2.ext"
   max_length = max(21, 21) = 21

最终结果：21
```

### 关键技巧

**字典存储路径长度**：

- 键为深度，值为该深度的累计路径长度
- 自动处理目录回退，无需显式维护栈

**制表符计数**：

- `depth = len(line) - len(line.lstrip('\t'))`
- 巧妙计算目录层级

**文件识别**：

- 通过 `'.' in name` 判断是否为文件
- 简单有效的区分方法

## 边界情况

1. **只有目录没有文件**：返回0
2. **根目录直接是文件**：不符合题意（文件系统必须有目录结构）
3. **深层嵌套**：算法能正确处理任意深度
4. **空输入**：虽然约束保证不会出现，但算法也能处理

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 字典记录 | O(n) | O(d) | 最优解，推荐 |
| 显式栈 | O(n) | O(d) | 逻辑清晰，易理解 |
| 递归解析 | O(n) | O(d) | 帮助理解问题本质 |

## 关键要点

1. **层级结构理解**：制表符表示目录深度
2. **路径长度计算**：累计计算而非字符串拼接
3. **文件系统抽象**：理解目录和文件的区别
4. **状态维护**：高效维护当前路径状态

## 相关题目

- [71. Simplify Path](071_simplify-path.md) - 简化路径
- [20. Valid Parentheses](020_valid_parentheses.md) - 有效的括号（栈的应用）
- [394. Decode String](394_decode_string.md) - 字符串解码

这道题巧妙地将文件系统抽象为字符串解析问题，考查了对栈数据结构和字符串处理的综合运用。
