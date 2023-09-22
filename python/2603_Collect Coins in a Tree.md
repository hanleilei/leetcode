# Collect Coins in a Tree

[[topology sort]]

There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given an integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an array coins of size n where coins[i] can be either 0 or 1, where 1 indicates the presence of a coin in the vertex i.

Initially, you choose to start at any vertex in the tree. Then, you can perform the following operations any number of times: 

Collect all the coins that are at a distance of at most 2 from the current vertex, or
Move to any adjacent vertex in the tree.
Find the minimum number of edges you need to go through to collect all the coins and go back to the initial vertex.

Note that if you pass an edge several times, you need to count it into the answer several times.

## Example 1

![](https://assets.leetcode.com/uploads/2023/03/01/graph-2.png)

```text
Input: coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: Start at vertex 2, collect the coin at vertex 0, move to vertex 3, collect the coin at vertex 5 then move back to vertex 2.
```

## Example 2

![](https://assets.leetcode.com/uploads/2023/03/02/graph-4.png)

```text
Input: coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
Output: 2
Explanation: Start at vertex 0, collect the coins at vertices 4 and 3, move to vertex 2,  collect the coin at vertex 7, then move back to vertex 0.
```

## Constraints

- n == coins.length
- 1 <= n <= 3 * 104
- 0 <= coins[i] <= 1
- edges.length == n - 1
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- edges represents a valid tree.

讲真，这个拓扑排序的，我一直没搞懂。。。

```cpp
class Solution {
public:
    int collectTheCoins(vector<int>& coins, vector<vector<int>>& edges) {
        int n = coins.size(), left_edges = n - 1;
        vector<vector<int>> g(n);
        vector<int> d(n);
        for (auto&& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
            d[e[0]]++, d[e[1]]++;
        }
        vector<int> q;
        // 第一次拓扑排序：去掉没有金币的叶子节点
        for (int i = 0; i < n; i++) {
            if (d[i] == 1 && coins[i] == 0) q.push_back(i);
        }
        while (!q.empty()) {
            left_edges--;
            int x = q.back(); q.pop_back();
            for (const int& y : g[x]) {
                if (--d[y] == 1 && coins[y] == 0) q.push_back(y);
            }
        }
        // 第二次拓扑排序：去掉有金币的叶子节点
        for (int i = 0; i < n; i++) {
            if (d[i] == 1 && coins[i]) q.push_back(i);
        }
        left_edges -= q.size();
        // 要是 有金币的叶子节点的父节点的父节点(向上删两次)
        for (const int& x : q) {
            for (const int& y : g[x]) {
                if (--d[y] == 1) left_edges--;
            }
        }
        // 只要节点移动过，则必出现来回，因此需要剩余的边数 * 2，但若不需要移动，则为0
        // 那么当剩下两个点时，这两个点之间的边我们会删除两次，这会导致剩余边数等于 −1，而此时答案应该是 0。所以最后答案要和 0 取最大值。
        return max(left_edges * 2, 0);
    }
};
```

```python
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        left_edges = n - 1
        g = collections.defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = []
        # 第一次拓扑排序：去掉没有金币的叶子节点
        for i in range(n):
            if degree[i] == 1 and coins[i] == 0:
                q.append(i)
        while q:
            left_edges -= 1
            i = q.pop()
            for j in g[i]:
                degree[j] -= 1
                if degree[j] == 1 and coins[j] == 0:
                    q.append(j)

        # 第二次拓扑排序：去掉有金币的叶子节点
        q = []
        for i in range(n):
            if degree[i] == 1 and coins[i]:
                q.append(i)
        left_edges -= len(q)
        # 要是 有金币的叶子节点的父节点的父节点(向上删两次)
        for i in q:
            for j in g[i]:
                degree[j] -= 1
                if degree[j] == 1:
                    left_edges -= 1

        # 只要节点移动过，则必出现来回，因此需要剩余的边数 * 2，但若不需要移动，则为0
        # 那么当剩下两个点时，这两个点之间的边我们会删除两次，这会导致剩余边数等于 −1，而此时答案应该是 0。所以最后答案要和 0 取最大值。
        return max(left_edges * 2, 0)
```
