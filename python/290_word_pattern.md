# Word Pattern

[[hashtable]] [[string]]

## Problem Description

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`. Specifically:

- Each letter in `pattern` maps to **exactly one** unique word in `s`.
- Each word in `s` maps to **exactly one** unique letter in `pattern`.
- No two letters map to the same word, and no two words map to the same letter.

## Examples

**Example 1:**

```text
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection is: a <-> "dog", b <-> "cat"
```

**Example 2:**

```text
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Explanation:
"a" should map to "dog", but "fish" != "dog"
```

**Example 3:**

```text
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Explanation:
"a" maps to both "dog" and "cat"
```

**Example 4:**

```text
Input: pattern = "abba", s = "dog dog dog dog"
Output: false
Explanation:
Both "a" and "b" try to map to "dog"
```

## Constraints

- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters.
- `1 <= s.length <= 3000`
- `s` contains only lowercase English letters and spaces `' '`.
- `s` **does not contain** any leading or trailing spaces.
- All the words in `s` are separated by a **single space**.

## 解法一：哈希表双向映射

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        使用两个哈希表建立双向映射关系
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        words = s.split()
        
        # 长度不匹配直接返回False
        if len(pattern) != len(words):
            return False
        
        # 建立双向映射
        char_to_word = {}  # 字符到单词的映射
        word_to_char = {}  # 单词到字符的映射
        
        for char, word in zip(pattern, words):
            # 检查字符到单词的映射
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            # 检查单词到字符的映射
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True
```

### 算法思路

1. **长度检查**：首先检查模式和单词数量是否相等
2. **双向映射**：使用两个哈希表确保一一对应关系
3. **冲突检测**：如果发现映射冲突，立即返回False

**复杂度分析**：

- 时间复杂度：O(n) - n为模式长度，需要遍历一次
- 空间复杂度：O(n) - 需要存储映射关系

## 解法二：哈希表+集合

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        使用一个哈希表和一个集合
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        used_words = set()
        
        for char, word in zip(pattern, words):
            if char in char_to_word:
                # 已存在映射，检查是否一致
                if char_to_word[char] != word:
                    return False
            else:
                # 新建映射，检查单词是否已被使用
                if word in used_words:
                    return False
                char_to_word[char] = word
                used_words.add(word)
        
        return True
```

**复杂度分析**：

- 时间复杂度：O(n) - 遍历模式一次
- 空间复杂度：O(n) - 哈希表和集合的空间

## 解法三：巧妙的一行解法

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        利用zip和set的性质实现一行解法
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        words = s.split()
        return (len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words)) 
                and len(pattern) == len(words))
```

### 核心思想

这个解法的巧妙之处在于：

- `zip(pattern, words)` 创建字符-单词对
- `len(set(zip(pattern, words)))` 表示有多少个不同的配对
- `len(set(pattern))` 表示有多少个不同的字符
- `len(set(words))` 表示有多少个不同的单词

如果是完美的一一映射，这三个值应该相等。

**复杂度分析**：

- 时间复杂度：O(n) - 创建集合和zip的时间
- 空间复杂度：O(n) - 集合和zip对象的空间

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 双向映射 | O(n) | O(n) | 最直观，易理解 |
| 哈希表+集合 | O(n) | O(n) | 代码简洁 |
| 一行解法 | O(n) | O(n) | 最简洁，但较难理解 |

## 边界情况处理

1. **长度不匹配**：模式和单词数量不相等
2. **空输入**：空模式或空字符串
3. **重复映射**：一个字符对应多个单词，或一个单词对应多个字符

## 关键要点

1. **双向检查**：必须确保字符到单词和单词到字符都是一一对应
2. **长度验证**：首先检查长度是否匹配
3. **映射一致性**：同一字符必须始终映射到同一单词
4. **唯一性保证**：每个单词只能被一个字符映射

## 常见错误

1. **单向检查**：只检查字符到单词的映射，忽略反向检查
2. **长度忽略**：没有预先检查长度匹配
3. **边界遗漏**：没有处理空输入的情况
4. **理解偏差**：错误理解"一一对应"的含义

## 相关题目

- [205. Isomorphic Strings](205_isomorphic_string.md) - 同构字符串
- [49. Group Anagrams](049_group_anagrams.md) - 字母异位词分组
- [242. Valid Anagram](242_valid_anagram.md) - 有效的字母异位词

这道题是哈希表应用的经典题目，重点在于理解和实现双向映射关系。
