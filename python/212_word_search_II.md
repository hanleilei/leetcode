# word search II

[[trie]] [[dfs]]

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

思路：

1. Trie 树：把所有单词插入 Trie 树，DFS 搜索时按 Trie 树的路径走，能快速剪枝
2. DFS 搜索：从棋盘每个位置出发，DFS 搜索 Trie 树，找到单词后把它从 Trie 树里删除（避免重复），同时向上剪枝（如果一个节点没有子节点了，就删除它），这样能大幅减少无效搜索
3. 额外启发式：反转某些“高分支词”（比如前四位全相同的），或者按棋盘上更稀有的端点反转，能进一步减少搜索树的分支（可选）
4. 预处理：棋盘字符频次（用于快速过滤 & 可选启发式反转），棋盘 bigram 过滤（如果单词里有某个 bigram 在棋盘里都没有，直接丢掉）

先来一个最快的，直接7ms的python代码：

```python
from typing import List, Dict, Set, Tuple


class TrieNode:
    __slots__ = ("chara", "word", "children", "parent")

    def __init__(self):
        self.chara = None
        # 这里的 word 我们存 canonical（min(w, rev(w)))，用作“输出ID”
        self.word = None
        self.children: Dict[str, "TrieNode"] = {}
        self.parent: "TrieNode | None" = None

    def remove(self):
        # 删除当前 word，并向上剪枝：把空分支删掉
        pt = self
        pt.word = None
        while not pt.children and pt.parent is not None and pt.word is None:
            chara = pt.chara
            parent = pt.parent
            parent.children.pop(chara, None)
            pt = parent


class Trie:
    def __init__(self, word_pairs: List[Tuple[str, str]]):
        """
        word_pairs: (search_word, canonical_word)
        Trie 的路径按 search_word 插入，但叶子处存 canonical_word
        """
        self.root = TrieNode()
        for search_word, canon in word_pairs:
            pt = self.root
            for i, chara in enumerate(search_word):
                nxt = pt.children.get(chara)
                if nxt is None:
                    nxt = TrieNode()
                    nxt.chara = chara
                    nxt.parent = pt
                    pt.children[chara] = nxt
                pt = nxt
            pt.word = canon


class Solution:
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        h, w = len(board), len(board[0])

        # -----------------------
        # 0) 预处理：棋盘字符频次（用于快速过滤 & 可选启发式反转）
        # -----------------------
        board_cnt: Dict[str, int] = {}
        for r in range(h):
            for c in range(w):
                ch = board[r][c]
                board_cnt[ch] = board_cnt.get(ch, 0) + 1

        # -----------------------
        # 1) bigram 过滤：收集棋盘相邻两字符（只取右&下，匹配时同时看正/逆）
        # -----------------------
        seq_two: Set[str] = set()
        for i in range(h):
            for j in range(w - 1):
                seq_two.add(board[i][j] + board[i][j + 1])
        for j in range(w):
            for i in range(h - 1):
                seq_two.add(board[i][j] + board[i + 1][j])

        # -----------------------
        # 2) canonical 化 + 标注映射 + bigram 过滤
        #    canon_to_originals: canonical -> {原词们}
        # -----------------------
        canon_to_originals: Dict[str, Set[str]] = {}

        def pass_char_count(word: str) -> bool:
            # 比 Counter 更轻：长度<=10 时很快
            tmp: Dict[str, int] = {}
            for ch in word:
                v = tmp.get(ch, 0) + 1
                if v > board_cnt.get(ch, 0):
                    return False
                tmp[ch] = v
            return True

        def pass_bigram(word: str) -> bool:
            if len(word) < 2:
                return True
            for i in range(len(word) - 1):
                a, b = word[i], word[i + 1]
                p = a + b
                if p not in seq_two and (b + a) not in seq_two:
                    return False
            return True

        # 去重一下输入词（可选，但通常有利）
        # 注意：最终输出还是按原词集合输出（canon_to_originals 里会保留）
        for w0 in words:
            if not pass_char_count(w0):
                continue
            if not pass_bigram(w0):
                continue

            rev = w0[::-1]
            canon = w0 if w0 <= rev else rev
            s = canon_to_originals.get(canon)
            if s is None:
                canon_to_originals[canon] = {w0}
            else:
                s.add(w0)

        if not canon_to_originals:
            return []

        # -----------------------
        # 3) 反转某些“高分支词” +（可选）按稀有端点反转
        #    Trie 插入 search_word，但叶子存 canon
        # -----------------------
        word_pairs: List[Tuple[str, str]] = []

        for canon in canon_to_originals.keys():
            search_word = canon

            # (A) repo 启发式：前四位全相同 -> 反转
            if len(search_word) >= 4 and search_word[:4] == search_word[0] * 4:
                search_word = search_word[::-1]
            else:
                # (B) 额外启发式：从棋盘更“稀有”的端点开始（通常更快）
                if len(search_word) >= 2:
                    if board_cnt.get(search_word[0], 0) > board_cnt.get(search_word[-1], 0):
                        search_word = search_word[::-1]

            word_pairs.append((search_word, canon))

        trie = Trie(word_pairs)

        found_words: Set[str] = set()
        root = trie.root
        dirs = self.directions

        for i in range(h):
            if not root.children:  # 全找完了，提前结束
                break
            for j in range(w):
                if not root.children:
                    break
                ch = board[i][j]
                nxt = root.children.get(ch)
                if nxt is not None:
                    self.search(board, nxt, i, j, h, w, found_words, canon_to_originals, dirs)

        return sorted(found_words)

    def search(self, board, pt, x, y, h, w, result, canon_to_originals, dirs):
        tmp = board[x][y]
        board[x][y] = "#"

        if pt.word is not None:
            canon = pt.word
            # 输出原词集合（支持多个原词映射同一个 canonical）
            result.update(canon_to_originals.get(canon, ()))
            pt.remove()

            # 命中并删除后如果已经没分支了，直接回溯（省很多无效扩展）
            if not pt.children:
                board[x][y] = tmp
                return

        children = pt.children
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                c = board[nx][ny]
                if c != "#":
                    nxt = children.get(c)
                    if nxt is not None:
                        self.search(board, nxt, nx, ny, h, w, result, canon_to_originals, dirs)

        board[x][y] = tmp
```

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

原来stefan的版本剪枝不够，修改后的版本：

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 构建Trie
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        
        rows, cols = len(board), len(board[0])
        result = []
        
        def dfs(node, i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            
            c = board[i][j]
            if c == '#' or c not in node.children:
                return
            
            curr_node = node.children[c]
            
            # 找到单词
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # 避免重复
            
            # 标记为已访问
            board[i][j] = '#'
            
            # 四个方向
            dfs(curr_node, i+1, j)
            dfs(curr_node, i-1, j)
            dfs(curr_node, i, j+1)
            dfs(curr_node, i, j-1)
            
            # 恢复
            board[i][j] = c
            
            # 优化：如果当前节点没有子节点，删除它
            if not curr_node.children and not curr_node.word:
                node.children.pop(c, None)
        
        for i in range(rows):
            for j in range(cols):
                dfs(root, i, j)
        
        return result
```

```java
import java.util.*;

class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        Trie trie = buildTrie(words); // 构建 Trie 树
        Set<String> res = new HashSet<>();
        
        // 遍历每个起点
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                // 如果当前位置的字符不为空，开始DFS搜索
                if (board[i][j] != '#') {
                    dfs(board, trie, res, i, j);
                }
            }
        }
        return new ArrayList<>(res);
    }

    // 深度优先搜索（DFS）
    public void dfs(char[][] board, Trie node, Set<String> res, int i, int j) {
        // 如果越界或者字符已被访问，或者当前字符不是trie的下一个节点，剪枝
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || 
            board[i][j] == '#' || node.next[board[i][j] - 'a'] == null) {
                return;
        }
        
        // 当前节点对应的字符存在单词
        node = node.next[board[i][j] - 'a']; // 移动到下一节点
        if (node.word != null) {
            res.add(node.word);  // 如果找到一个完整的单词，加入结果集
            node.word = null;  // 避免重复添加相同单词
        }
        
        // 记录当前字符
        char c = board[i][j];
        board[i][j] = '#';  // 标记当前字符已被访问
        
        // 递归访问四个方向
        dfs(board, node, res, i - 1, j);  // 上
        dfs(board, node, res, i + 1, j);  // 下
        dfs(board, node, res, i, j - 1);  // 左
        dfs(board, node, res, i, j + 1);  // 右
        
        board[i][j] = c;  // 恢复字符
    }   

    // 构建Trie树
    public Trie buildTrie(String[] words) {
        Trie root = new Trie();
        for (String word : words) {
            Trie p = root;
            for (char c : word.toCharArray()) {
                if (p.next[c - 'a'] == null) {
                    p.next[c - 'a'] = new Trie();
                }
                p = p.next[c - 'a'];  // 移动到当前字符节点
            }
            p.word = word;  // 设置终点的单词
        }
        return root;
    }

    // Trie树节点
    private class Trie {
        Trie[] next = new Trie[26];  // 26个字母
        String word = null;  // 结束的单词
    }
}
```
