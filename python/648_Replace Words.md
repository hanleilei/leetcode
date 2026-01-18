# Replace Words

[[trie]]

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.

拿到trie的模板后，这题就很好做了：

```python
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def find_root(self, word: str) -> str:
        """在字典树中查找单词的最短词根"""
        node = self.root
        for i, ch in enumerate(word):
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.is_end:  # 找到词根
                return word[:i+1]
        return word  # 没找到词根，返回原单词

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        # 将所有词根插入字典树
        for root_word in dictionary:
            trie.insert(root_word)
        
        # 分割句子，查找并替换每个单词
        words = sentence.split()
        result = []
        
        for word in words:
            # 在字典树中查找最短词根
            root_word = trie.find_root(word)
            result.append(root_word)
        
        return " ".join(result)
```

不折腾那么复杂，来个简单的：

```python
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for root in dictionary:
            p = trie
            for c in root:
                if c not in p: p[c] = {}
                p = p[c]
            p["#"] = {}

        words = sentence.split()
        for i, word in enumerate(words):
            p = trie
            for j, c in enumerate(word):
                if c not in p: break
                if "#" in p[c]:
                    words[i] = word[:j+1]
                    break
                p = p[c]
        
        return " ".join(words)
```
