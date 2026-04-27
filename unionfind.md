# Union-Find (Disjoint Set Union)

959 Regions Cut By Slashes

```java
public class QuickUnionUF{
    private int[] roots;

    public QuickUnionUF(int N){
        roots = new int[N];
        for(int i = 0; i < N; i++){
            roots[i] = i;
        }
    }

    private int findRoot(int i){
        int root = i;
        while(root != roots[root])
            root = roots[root];

        // path compression
        while (i != roots[i]){
            int tmp = roots[i];
            roots[i] = root;
            i = tmp;
        }
        return root;
    }

    public boolean connected(int p, int q){
        return findRoot(p) == findRoot(q);
    }

    public void union(int p, int q){
        int qroot = findRoot(q);
        int proot = findRoot(p);
        roots[proot] = qroot;
    }
}
```

```java
class UnionFind{
    private int count = 0;
    private int[] parent;
    private UnionFind(int n){
        count = n;
        parent = new int[n];
        for(int i = 0; i < n; i++){
            parent[i] = i;
        }
    }
    public int find(int p){
        while(p != parent[p]){
            parent[p] = parent[parent[p]];
            p = parent[p];
        }
        return p;
    }
    public void union(int p, int q){
        int proot = find(p);
        int qroot = find(q);
        if(proot == qroot) return;
        parent[proot] = qroot;
        count--;
    }
}
```

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, p, i, j):
        proot = self.find(p, i)
        qroot = self.find(p, j)
        if proot == qroot:
            return
        self.parent[proot] = qroot

    def find(self, p, i):
        root = i
        while root != self.parent[root]:
            root = self.parent[root]
        # path compression
        while i != self.parent[i]:
            x = i
            i = self.parent[i]
            self.parent[x] = root
        return root
```

```c++
class UnionFind {
private:
    vector<int> parent;
public:
    UnionFind(int n) {
        parent.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    int find(int p) {
        int root = p;
        while (root != parent[root]) {
            root = parent[root];
        }
        // path compression
        while (p != parent[p]) {
            int x = p;
            p = parent[p];
            parent[x] = root;
        }
        return root;
    }
    void union(int p, int q) {
        int proot = find(p);
        int qroot = find(q);
        if (proot == qroot) return;
        parent[proot] = qroot;
    }
};
```
