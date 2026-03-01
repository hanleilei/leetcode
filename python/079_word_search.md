# word search

[[dfs]]

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

```python
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit again
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
```

上面的方法略慢，要 268ms。下面的只要 80ms，超过 98.6%的人：

```python
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word)==0:
            return True

        if len(word)>len(board)*len(board[0]):
            return False

        wCount={}
        for w in word:
            wCount[w]=wCount.get(w,0)+1

        #print (wCount)

        chrCount={}
        headList=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                chrCount[board[i][j]]=chrCount.get(board[i][j],0)+1
                if board[i][j]==word[0]:
                    headList.append((i,j))
        # print (chrCount)
        for w in word:
            print (w)
            if wCount[w]>chrCount.get(w,0):
                return False

        wIndex=0

        def findWord(i,j,wIndex):
            if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or board[i][j]!=word[wIndex]:
                return False

            if wIndex==len(word)-1:
                return True

            wIndex+=1
            board[i][j]=''
            neigbor=[(1,0),(-1,0),(0,1),(0,-1)]
            for a,b in neigbor:
                if findWord(i+a,j+b,wIndex):
                    return True
            wIndex-=1
            board[i][j]=word[wIndex]
            return False

        for i,j in headList:
            if findWord(i,j,wIndex):
                return True

        return False
```

上面的方法略慢，看下这个：

```python
from collections import Counter


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        bcnts = Counter(c for r in board for c in r)

        for w, w_cnt in Counter(word).items():
            if w not in bcnts or w_cnt > bcnts[w]:
                return False

        def backtrack(i, j, index):
            if index == len(word) - 1:
                return True

            # 标记为已访问
            board[i][j] = '*'
            for dx, dy in dirs:
                next_i, next_j = i + dx, j + dy
                # 先判断再进入，减少递归次数
                if 0 <= next_i < m and 0 <= next_j < n and word[index + 1] == board[next_i][next_j] and backtrack(
                        next_i, next_j, index + 1):
                    return True

            board[i][j] = word[index]
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False
```

最后来一个快的，42ms：

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        R = len(board)
        C = len(board[0])
        
        if len(word) > R*C:
            return False
        
        count = Counter(sum(board, []))
        
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
                        
        seen = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= R or c >= C or word[i] != board[r][c] or (r,c) in seen:
                return False
            
            seen.add((r,c))
            res = (
                dfs(r+1,c,i+1) or 
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1) 
            )
            seen.remove((r,c))  #backtracking

            return res
        
        for i in range(R):
            for j in range(C):
                if dfs(i,j,0):
                    return True
        return False
```

再来一个0ms的：

启发：如果 word=abcd 但 board 中的 a 很多，d 很少（比如只有一个），那么从 d 开始搜索，能更快地找到答案。（即使我们肉眼去找，这种方法也是更快的）

设 word 的第一个字母在 board 中出现了 x 次，word 的最后一个字母在 board 中出现了 y 次。

如果 `y<x`，我们可以把 word 反转，相当于从 word 的最后一个字母开始搜索，这样更容易在一开始就满足 `board[i][j] != word[k]`，不会往下递归，递归的总次数更少。

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word):  # 优化一
            return False
        if cnt[word[-1]] < cnt[word[0]]:  # 优化二
            word = word[::-1]

        m, n = len(board), len(board[0])
        def dfs(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:  # 匹配失败
                return False
            if k == len(word) - 1:  # 匹配成功！
                return True
            board[i][j] = ''  # 标记访问过
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):  # 相邻格子
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                    return True  # 搜到了！
            board[i][j] = word[k]  # 恢复现场
            return False  # 没搜到
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
```
