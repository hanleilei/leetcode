# Most Stones Removed with Same Row or Column

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

Example 1:

```
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
```

Example 2:

```
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
```

Example 3:

```
Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
```

Constraints:

```
1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.
```

let's read lee215's solution:

## Problem:

we can remove a stone if and only if,
there is another stone in the same column OR row.
We try to remove as many as stones as possible.

One sentence to solve:
Connected stones can be reduced to 1 stone,
the maximum stones can be removed = stones number - islands number.
so just count the number of "islands".

1. Connected stones
   Two stones are connected if they are in the same row or same col.
   Connected stones will build a connected graph.
   It's obvious that in one connected graph,
   we can't remove all stones.

We have to have one stone left.
An intuition is that, in the best strategy, we can remove until 1 stone.

I guess you may reach this step when solving the problem.
But the important question is, how?

2. A failed strategy
   Try to remove the least degree stone
   Like a tree, we try to remove leaves first.
   Some new leaf generated.
   We continue this process until the root node left.

However, there can be no leaf.
When you try to remove the least in-degree stone,
it won't work on this "8" like graph:

```
[[1, 1, 0, 0, 0],
[1, 1, 0, 0, 0],
[0, 1, 1, 0, 0],
[0, 0, 1, 1, 1],
[0, 0, 0, 1, 1]]
```

The stone in the center has least degree = 2.
But if you remove this stone first,
the whole connected stones split into 2 parts,
and you will finish with 2 stones left.

3. A good strategy
   In fact, the proof is really straightforward.
   You probably apply a DFS, from one stone to next connected stone.
   You can remove stones in reversed order.
   In this way, all stones can be removed but the stone that you start your DFS.

One more step of explanation:
In the view of DFS, a graph is explored in the structure of a tree.
As we discussed previously,
a tree can be removed in topological order,
from leaves to root.

4. Count the number of islands
   We call a connected graph as an island.
   One island must have at least one stone left.
   The maximum stones can be removed = stones number - islands number

The whole problem is transferred to:
What is the number of islands?

You can show all your skills on a DFS implementation,
and solve this problem as a normal one.

5. Unify index
   Struggle between rows and cols?
   You may duplicate your codes when you try to the same thing on rows and cols.
   In fact, no logical difference between col index and rows index.

An easy trick is that, add 10000 to col index.
So we use 0 ~ 9999 for row index and 10000 ~ 19999 for col.

6. Search on the index, not the points
   When we search on points,
   we alternately change our view on a row and on a col.

We think:
a row index, connect two stones on this row
a col index, connect two stones on this col.

In another view：
A stone, connect a row index and col.

Have this idea in mind, the solution can be much simpler.
The number of islands of points,
is the same as the number of islands of indexes.

7. Union-Find
   I use union find to solve this problem.
   As I mentioned, the elements are not the points, but the indexes.

for each point, union two indexes.
return points number - union number
Copy a template of union-find,
write 2 lines above,
you can solve this problem in several minutes.

Complexity
union and find functions have worst case O(N), amortize O(1)
The whole union-find solution with path compression,
has O(N) Time, O(N) Space

If you have any doubts on time complexity,
please refer to [wikipedia](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) first.

```cpp
    int removeStones(vector<vector<int>>& stones) {
        for (int i = 0; i < stones.size(); ++i)
            uni(stones[i][0], ~stones[i][1]);
        return stones.size() - islands;
    }

    unordered_map<int, int> f;
    int islands = 0;

    int find(int x) {
        if (!f.count(x)) f[x] = x, islands++;
        if (x != f[x]) f[x] = find(f[x]);
        return f[x];
    }

    void uni(int x, int y) {
        x = find(x), y = find(y);
        if (x != y) f[x] = y, islands--;
    }
```

```java
    Map<Integer, Integer> f = new HashMap<>();
    int islands = 0;

    public int removeStones(int[][] stones) {
        for (int i = 0; i < stones.length; ++i)
            union(stones[i][0], ~stones[i][1]);
        return stones.length - islands;
    }

    public int find(int x) {
        if (f.putIfAbsent(x, x) == null)
            islands++;
        if (x != f.get(x))
            f.put(x, find(f.get(x)));
        return f.get(x);
    }

    public void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) {
            f.put(x, y);
            islands--;
        }
    }
```

```python
    def removeStones(self, points):
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in points:
            union(i, ~j)
        return len(points) - len({find(x) for x in UF})
```

```python
    def removeStones(self, points):
        uf = {}
        def find(x):
            if x != uf.setdefault(x, x):
                uf[x] = find(uf[x])
            return uf[x]
        for i, j in points:
            uf[find(i)] = find(~j)
        return len(points) - len({find(x) for x in uf})
```

## Update About Union Find Complexity

I have 3 main reasons that always insist O(N), on all my union find solutions.

1. The most important, union find is really a common knowledge for algorithm.
   Using both path compression, splitting, or halving and union by rank or size ensures
   that the amortized time per operation is only O(1).
   So it's fair enough to apply this conclusion.

2. It's really not my job to discuss how union find works or the definition of big O.
   I bet everyone can find better resource than my post on this part.
   You can see the core of my solution is to transform the problem as a union find problem.
   The essence is the thinking process behind.
   People can have their own template and solve this problem with 2-3 more lines.
   But not all the people get the point.

3. I personally manually write this version of union find every time.
   It is really not worth a long template.
   The version with path compression can well handle all cases on leetcode.
   What‘s the benefit here to add more lines?

4. In this problem, there is N union operation, at most 2 \* sqrt(N) node.
   When N get bigger, the most operation of union operation is amortize O(1).

5. I knew there were three good resourse of union find:

- [top down analusis of path compression](http://www.cs.tau.ac.il/~michas/ufind.pdf)
- [wiki](https://en.wikipedia.org/wiki/Disjoint-set_data_structure#cite_note-Cormen2009-10)
- [stackexchange](https://cs.stackexchange.com/questions/50294/why-is-the-path-compression-no-rank-for-disjoint-sets-o-log-n-amortized-fo)
  But they most likely give a upper bound time complexity of union find,
  not a supreme.
  If anyone has a clear example of union find operation sequence,
  to make it larger than O(N), I am so glad to know it.

# TODO

又是被碾压的一天
