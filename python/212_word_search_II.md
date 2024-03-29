# word search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
board = [
['o','a','a','n'],
['e','t','a','e'],
['i','h','k','r'],
['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

先来一个最快的：

```python
class Solution(object):
    def findWords(self, board, words):
        if not board or not board[0]: return False
        R, C = len(board), len(board[0])
        root = {}
        for word in words:
            trie = root
            for c in word:
                if c not in trie:
                    trie[c] = {}
                trie = trie[c]
            trie['#'] = word


        def dfs(i, j, parent):
            c, board[i][j] = board[i][j], '{'
            trie = parent[c]
            if '#' in trie:
                ans.add(trie['#'])
                trie.pop('#')

            if i and board[i - 1][j] in trie:
                dfs(i - 1, j, trie)
            if i < R - 1 and board[i + 1][j] in trie:
                dfs(i + 1, j, trie)
            if j and board[i][j - 1] in trie:
                dfs(i, j - 1, trie)
            if j < C - 1 and board[i][j + 1] in trie:
                dfs(i, j + 1, trie)
            board[i][j] = c
            if not trie:
                parent.pop(c)

        ans = set()
        for i in range(R):
            for j in range(C):
                if board[i][j] in root:
                    dfs(i, j, root)

        return list(ans)
```

在当前最新的测试用例下：2022 Nov 5th，下面的代码都不能通过。用到的测试用例诸如：

1. board 是 ab 的交叉组合，words 也是不同长度的 ab 交叉组合，测试失败
2. board 是 a，words 是不同长度的 a。

再来一个 caikehe 的最简单的：

```python
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp
```

```python
from functools import reduce
from collections import defaultdict
class Solution:
    def findWords(self, board, words):
        Trie = lambda : defaultdict(Trie)
        trie = Trie()
        for w in words:
            end = reduce(dict.__getitem__, w, trie)
            end['#'] = '#'
            end['$'] = w

        self.res = set()
        self.used = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board, i, j, trie)
        return list(self.res)

    def find(self, board, i, j, trie):
        if '#' in trie:
            self.res.add(trie['$'])
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j] = True
            self.find(board, i + 1, j, trie[board[i][j]])
            self.find(board, i, j + 1, trie[board[i][j]])
            self.find(board, i - 1, j, trie[board[i][j]])
            self.find(board, i, j - 1, trie[board[i][j]])
            self.used[i][j] = False
```

最后来 stefan 的：

但是现在超时了，参考一下。

```python
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
from functools import reduce
from collections import defaultdict
class Solution:
    def findWords(self, board, words):
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        board = {i + 1j*j: c
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)}

        found = []
        def search(node, z, word):
            if node.pop(None, None):
                found.append(word)
            c = board.get(z)
            if c in node:
                board[z] = None
                for k in range(4):
                    search(node[c], z + 1j**k, word + c)
                board[z] = c
        for z in board:
            search(root, z, '')

        return found
```
