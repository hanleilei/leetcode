# Add and Search Word - Data structure design

[[trie]]

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

## Example:

```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```

## Note:

You may assume that all words are consist of lowercase letters a-z

## 解法1: 字典树

```python
class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.trie = Node()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for w in word:
            curr = curr.children[w]
        curr.isword = True

    def search(self, word: str) -> bool:
        return self.match(word, 0, self.trie)
    
    def match(self, word, index, root):
        if root == None:
            return False
        if index == len(word):
            return root.isword
        if word[index] != ".":
            return root != Node and self.match(word, index + 1, root.children.get(word[index]))
        else:
            for child in root.children.values():
                if self.match(word, index + 1, child):
                    return True
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

方法就是构造一个字典树：

```Python
class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = None

    def search(self, word):
        nodes = [self.root]
        for char in word + '$':
            nodes = [kid for node in nodes for kid in
                     ([node[char]] if char in node else
                      filter(None, node.values()) if char == '.' else [])]
        return bool(nodes)

```

使用集合的字典，速度很快：

```Python
class WordDictionary:

    def __init__(self):
        self.map = collections.defaultdict(set)

    def addWord(self, word):
        k = len(word)
        self.map[k].add(word)

    def search(self, word):
        k = len(word)

        p = self.map[k]
        if not p:
            return False
        if word in p:
            return True

        for i in range(k):
            if word[i] == '.':
                continue
            p = {x for x in p if x[i] == word[i]}
            if not p:
                return False
        return True
```

使用列表的字典，速度很快：

```Python
class WordDictionary:
    def __init__(self):
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False
```
