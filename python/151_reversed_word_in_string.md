# Reverse Words in a String

[[string]] [[two-pointers]]

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Examples

### Example 1
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

### Example 2
```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

### Example 3
```
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

## Constraints
- 1 <= s.length <= 10^4
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

## 解法一：Python 内置方法（最简洁）

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
```

**复杂度分析**：
- 时间复杂度：O(n)
- 空间复杂度：O(n)

## 解法二：正则表达式

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        return " ".join(re.split(r"\s+", s.strip())[::-1])
```

## 解法三：双反转法

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # 预处理：去除多余空格
        s = ' '.join(s.split())
        
        # 1. 反转整个字符串
        chars = list(s[::-1])
        
        # 2. 反转每个单词
        left = 0
        for right in range(len(chars) + 1):
            if right == len(chars) or chars[right] == ' ':
                self.reverse(chars, left, right - 1)
                left = right + 1
        
        return ''.join(chars)
    
    def reverse(self, chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
```

## 解法四：O(1) 额外空间原地解法 ⭐（进阶）

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        O(1) 额外空间的原地解法
        适用于可变字符串的编程语言
        """
        chars = list(s)  # Python中模拟可变字符串
        n = len(chars)
        
        # 步骤1：原地压缩多余空格
        write_idx = 0
        i = 0
        
        while i < n:  # 这段字符串中间处理空格的代码很有趣啊，原理其实很简单。
            # 跳过空格
            while i < n and chars[i] == ' ':
                i += 1
            
            # 添加单词间分隔符
            if write_idx != 0 and i < n:
                chars[write_idx] = ' '
                write_idx += 1
            
            # 复制单词
            while i < n and chars[i] != ' ':
                chars[write_idx] = chars[i]
                write_idx += 1
                i += 1
        
        n = write_idx  # 更新有效长度
        
        # 步骤2：反转整个字符串
        self.reverse(chars, 0, n - 1)
        
        # 步骤3：反转每个单词
        start = 0
        for end in range(n + 1):
            if end == n or chars[end] == ' ':
                self.reverse(chars, start, end - 1)
                start = end + 1
        
        return ''.join(chars[:n])
    
    def reverse(self, chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
```

**复杂度分析**：
- 时间复杂度：O(n) - 每个字符最多被访问常数次
- 空间复杂度：O(1) - 只使用常数额外变量

## 解法五：从右到左扫描

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        从右到左提取单词的解法
        """
        s = list(s)
        res = ''
        left, right = 0, len(s) - 1
        
        # 去除首尾空格
        while s[left] == " ":
            left += 1
        while s[right] == " ":
            right -= 1
        
        while left <= right:
            # 从右边找单词边界
            index = right
            while index >= left and s[index] != " ":
                index -= 1
            
            # 提取单词
            for i in range(index + 1, right + 1):
                res += s[i]
            
            # 添加分隔符
            if index > left:
                res += " "
            
            # 跳过空格，准备下一个单词
            while index >= left and s[index] == " ":
                index -= 1
            right = index
            
        return res
```

## 解法六：

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. 预处理：去除多余空格
        words = s.split()  # 自动处理多个空格
        s = ' '.join(words)  # 重建字符串，单词间只有一个空格, 污点啊
        
        # 2. 使用您的原始逻辑
        res = list(s[::-1])
        left = 0
        
        for right in range(len(res) + 1):
            if right == len(res) or res[right] == ' ':
                res[left:right] = self.reverse(res[left:right])
                left = right + 1
        
        return ''.join(res)
    
    def reverse(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s
```

## 关键要点

1. **进阶解法核心**：三步骤（压缩-反转-再反转）实现 O(1) 空间
2. **空格处理**：多种方法处理连续空格问题
3. **算法选择**：面试推荐解法四（展示算法功底）或解法一（简洁实用）

## 相关题目
- [344. Reverse String](../344_reverse_string.md)
- [557. Reverse Words in a String III](../557_reverse_words_in_string_iii.md)
- [186. Reverse Words in a String II](../186_reverse_words_in_string_ii.md)
