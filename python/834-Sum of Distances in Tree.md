# Sum of Distances in Tree

There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

You are given the integer `n` and the array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

Return an array `answer` of length `n` where `answer[i]` is the sum of the distances between the `ith` node in the tree and all other nodes.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg)

**Input:** n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
**Output:** [8,12,6,10,10,10]
**Explanation:** The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist2.jpg)

**Input:** n = 1, edges = []
**Output:** [0]

**Example 3:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg)

**Input:** n = 2, edges = [[1,0]]
**Output:** [1,1]

**Constraints:**

- `1 <= n <= 3 * 104`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- The given input represents a valid tree.

**下面来看下lee215的方法：**

# **Intuition**

What if given a tree, with a certain root `0`?  
In `O(N)` we can find sum of distances in tree from root and all other nodes.  
Now for all `N` nodes?  
Of course, we can do it `N` times and solve it in `O(N^2)`.  
C++ and Java may get accepted luckily, but it's not what we want.

When we move our root from one node to its connected node,  
one part of nodes get closer, one the other part get further.

If we know exactly how many nodes in both parts, we can solve this problem.

With one single traversal in tree, we should get enough information for it and  
don't need to do it again and again.  

# **Explanation**

0. Let's solve it with node `0` as root.

1. Initial an array of hashset `tree`, `tree[i]` contains all connected nodes to `i`.  
   Initial an array `count`, `count[i]` counts all nodes in the subtree `i`.  
   Initial an array of `res`, `res[i]` counts sum of distance in subtree `i`.

2. Post order dfs traversal, update `count` and `res`:  
   `count[root] = sum(count[i]) + 1`  
   `res[root] = sum(res[i]) + sum(count[i])`

3. Pre order dfs traversal, update `res`:  
   When we move our root from parent to its child `i`, `count[i]` points get 1 closer to root, `n - count[i]` nodes get 1 futhur to root.  
   `res[i] = res[root] - count[i] + N - count[i]`

4. return res, done.

# **Time Complexity**:

dfs: `O(N)` time  
dfs2: `O(N)` time

```java
class Solution {
    int[] res, count;
    ArrayList<HashSet<Integer>> tree;
    public int[] sumOfDistancesInTree(int N, int[][] edges) {
        tree = new ArrayList<HashSet<Integer>>();
        res = new int[N];
        count = new int[N];
        for (int i = 0; i < N ; ++i)
            tree.add(new HashSet<Integer>());
        for (int[] e : edges) {
            tree.get(e[0]).add(e[1]);
            tree.get(e[1]).add(e[0]);
        }
        dfs(0, -1);
        dfs2(0, -1);
        return res;
    }

    public void dfs(int root, int pre) {
        for (int i : tree.get(root)) {
            if (i == pre) continue;
            dfs(i, root);
            count[root] += count[i];
            res[root] += res[i] + count[i];
        }
        count[root]++;
    }

    public void dfs2(int root, int pre) {
        for (int i : tree.get(root)) {
            if (i == pre) continue;
            res[i] = res[root] - count[i] + count.length - count[i];
            dfs2(i, root);
        }
    }
}
```

```cpp
class Solution {
public:
    vector<unordered_set<int>> tree;
    vector<int> res, count;

    vector<int> sumOfDistancesInTree(int N, vector<vector<int>>& edges) {
        tree.resize(N);
        res.assign(N, 0);
        count.assign(N, 1);
        for (auto e : edges) {
            tree[e[0]].insert(e[1]);
            tree[e[1]].insert(e[0]);
        }
        dfs(0, -1);
        dfs2(0, -1);
        return res;
    }
    void dfs(int root, int pre) {
        for (auto i : tree[root]) {
            if (i == pre) continue;
            dfs(i, root);
            count[root] += count[i];
            res[root] += res[i] + count[i];
        }
    }

    void dfs2(int root, int pre) {
        for (auto i : tree[root]) {
            if (i == pre) continue;
            res[i] = res[root] - count[i] + count.size() - count[i];
            dfs2(i, root);
        }
    }
};
```

```python
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        return res
```
