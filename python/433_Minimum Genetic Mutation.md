# Minimum Genetic Mutation

[[bfs]]

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

bfs的方法，分别用labuladong的模板2和模板3来写，思路是一样的，速度也差不多。

```python
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        def checkNeighbor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        
        q = deque([start])
        visited = {start}
        ### use extra variable to store mutations
        mutations = 0
        while q:
            ### use for loop to check all nodes in the q
            ### so that after the for loop, we can increment mutations by 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == end:
                    return mutations
                for nei in bank:
                    if checkNeighbor(cur,nei) and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            ### increment mutations by 1
            mutations += 1
        return -1
```

```python
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        ### check to see if a and b are neighbors
        ### i.e., a and b only differ by one character
        def checkNeighbor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        
        ### initialize the q with start and 0 mutations
        q = deque([[start,0]])
        ### initialize the visited set with start
        visited = {start}
        while q:
            cur, mutations = q.popleft()
            ### if cur == end, we are done
            if cur == end:
                return mutations
            ### go through all gene mutations from the bank
            for nei in bank:
                ### check if nei is a valid neighbor and if we have visited it before
                ### if not, we add it to the visited, add it to the q with mutations+1
                if checkNeighbor(cur,nei) and nei not in visited:
                    visited.add(nei)
                    q.append([nei,mutations+1])
        ### if we don't reach the end, there is no such a mutation, return -1
        return -1
```

再来一个双端bfs：

```python
class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        # 1: 建立字典，顺便去掉重复元素
        mp = {b: 0 for b in bank}

        # 2: 排除极端情况，end 不在基因库中
        if end not in mp:
            return -1

        # 3: 双向 BFS 初始化
        q1, q2 = deque([start]), deque([end])
        table = ('A', 'C', 'G', 'T')

        mp[start] = mp.get(start, 0) | 1
        mp[end] |= 2

        step = 0
        while q1 and q2:
            # 每次选择较小的队列进行扩展
            if len(q1) > len(q2):
                q1, q2 = q2, q1

            flag = mp[q1[0]] & 3  # 当前队列的方向标记（1 或 2）

            for _ in range(len(q1)):
                temp = q1.popleft()

                if mp[temp] == 3:  # 两个队列碰头，返回步长
                    return step

                for i in range(len(temp)):
                    for c in table:
                        if temp[i] == c:
                            continue
                        s = temp[:i] + c + temp[i+1:]
                        if s not in mp or mp[s] & flag:
                            continue
                        mp[s] |= flag
                        q1.append(s)

            step += 1

        return -1
```
