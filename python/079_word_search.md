# word search

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

上面的方法略慢，要268ms。下面的只要80ms，超过98.6%的人：

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
