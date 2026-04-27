# Number of Provinces

[[unionfind]] [[dfs]] [[bfs]]

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where `isConnected[i][j] = 1` if the ith city and the jth city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return the total number of provinces.

## Example 1

![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

```text
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

## Example 2

![](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)

```text
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

## Constraints

- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j] is 1 or 0.`
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`

直接上DFS的方案：

```java
class Solution {
    public void dfs(int[][] m, int[] visited, int i){
        for (int j = 0;j < m.length; j++){
            if (m[i][j] == 1 && visited[j] == 0){
                visited[j] = 1;
                dfs(m, visited, j);
            }
        }
    }
    public int findCircleNum(int[][] isConnected) {
        int[] visited = new int[isConnected.length];
        int count = 0;
        for (int i = 0; i < isConnected.length; i++){
            if (visited[i] == 0){
                dfs(isConnected, visited, i);
                count++;            
            }
        }
        return count;
    }
}
```

BFS的方案：

```java
class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];

        int cnt = 0;
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++){
            if (!visited[i]){
                cnt++;
                queue.offer(i);
                visited[i] = true;
                while (!queue.isEmpty()){
                    int v = queue.poll();
                    for (int w = 0; w < n; w++){
                        if (isConnected[v][w] == 1 && !visited[w]){
                            visited[w] = true;
                            queue.offer(w);
                        }
                    }

                }
            }
        }
        return cnt;
    }
}
```

并查集：

```java
class Solution {
    public int findCircleNum(int[][] isConnected) {
        int cities = isConnected.length;
        int[] parent = new int[cities];
        for (int i = 0; i < cities; i++){
            parent[i] = i;
        }

        for (int i = 0; i < cities; i++){
            for (int j = i + 1; j < cities; j++){
                if (isConnected[i][j] == 1){
                    union(parent, i, j);
                }
            }
        }

        int provinces = 0;
        for (int i = 0; i < cities; i++){
            if (parent[i] == i){
                provinces++;
            }
        }
        return provinces;
    }

    public void union(int[] parent, int index1, int index2){
        parent[find(parent, index1)] = find(parent, index2);
    }

    public int find(int[] parent, int index){
        if(parent[index] != index){
            parent[index] = find(parent, parent[index]);
        }
        return parent[index];
    }
}
```
