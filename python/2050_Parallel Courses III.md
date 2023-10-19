# Parallel Courses III

[[bfs]] [[topology sort]]  [[dfs]]

You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship). Furthermore, you are given a 0-indexed integer array time where time[i] denotes how many months it takes to complete the (i+1)th course.

You must find the minimum number of months needed to complete all the courses following these rules:

You may start taking a course at any time if the prerequisites are met.
Any number of courses can be taken at the same time.
Return the minimum number of months needed to complete all the courses.

Note: The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).

## Example 1

![1](https://assets.leetcode.com/uploads/2021/10/07/ex1.png)

```text
Input: n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
Output: 8
Explanation: The figure above represents the given graph and the time required to complete each course. 
We start course 1 and course 2 simultaneously at month 0.
Course 1 takes 3 months and course 2 takes 2 months to complete respectively.
Thus, the earliest time we can start course 3 is at month 3, and the total time required is 3 + 5 = 8 months.
```

## Example 2

![1](https://assets.leetcode.com/uploads/2021/10/07/ex2.png)

```text
Input: n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]
Output: 12
Explanation: The figure above represents the given graph and the time required to complete each course.
You can start courses 1, 2, and 3 at month 0.
You can complete them after 1, 2, and 3 months respectively.
Course 4 can be taken only after course 3 is completed, i.e., after 3 months. It is completed after 3 + 4 = 7 months.
Course 5 can be taken only after courses 1, 2, 3, and 4 have been completed, i.e., after max(1,2,3,7) = 7 months.
Thus, the minimum time needed to complete all the courses is 7 + 5 = 12 months.
```

## Constraints

```text
1 <= n <= 5 * 104
0 <= relations.length <= min(n * (n - 1) / 2, 5 * 104)
relations[j].length == 2
1 <= prevCoursej, nextCoursej <= n
prevCoursej != nextCoursej
All the pairs [prevCoursej, nextCoursej] are unique.
time.length == n
1 <= time[i] <= 104
The given graph is a directed acyclic graph.
```

This problem is an advanced version of 1494. Parallel Courses II, which has prerequisite relationship between courses.
To solve prerequisite relationship, we can obviously use Topology Sort idea to complete prev courses before next courses.
Let dist[u] is the number of months required to finish u course, dist[u] is calculated as maximum dist of the predecessor nodes + times[u].

```python
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        inDegree = [0] * n
        for l, r in relations:
            l, r = l - 1, r - 1
            graph[l].append(r)
            inDegree[r] += 1
        
        q = deque([])
        dist = [0] * n
        for u in range(n):
            if inDegree[u] == 0:
                q.append(u)
                dist[u] = time[u]
        
        while q:
            u= q.popleft()
            for v in graph[u]:
                dist[v] = max(dist[u] + time[v], dist[v])
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
        return max(dist)
```

再来一个topology sort：

```python
class Solution:
    def minimumTime(self, numCourses: int, prerequisites: List[List[int]], time: List[int]) -> int:
        # Initilize data
        output = 0
        dp = [0] * numCourses
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        
        # Build graph and inDegree
        for parent, child in prerequisites:
            graph[parent - 1].append(child - 1)
            inDegree[child - 1] += 1
        
        # BFS
        queue = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append([course, 0])
        
        while queue:
            curCourse, curTime = queue.popleft()
            curTime += time[curCourse]
            
            for child in graph[curCourse]:
                dp[child] = max(dp[child], curTime)
                if inDegree[child] == 1:
                    queue.append([child, dp[child]])
                else:
                    inDegree[child] -= 1
                    
            output = max(output, curTime)
    
        return output
```

再来个dfs：

```python
class Solution:
    def minimumTime(self, n: int, prerequisites: List[List[int]], time: List[int]) -> int:
        # Create an adjacency list such that the edge points from the next node to the previous node.
        adj = [[] for _ in range(n + 1)]
        for course in prerequisites:
            next_course, prev_course = course[0], course[1]
            adj[next_course].append(prev_course)

        # dp[i] stores the earliest time to complete the ith course.
        dp = [-1] * (n + 1)

        def dfs(node: int) -> int:
            if dp[node] != -1:
                return dp[node]

            # We can only start a particular course when all its prerequisites are finished.
            time_to_start = 0
            for child in adj[node]:
                time_to_start = max(time_to_start, dfs(child))

            # Time to complete the course = timeToStart + timeToComplete
            dp[node] = time_to_start + time[node - 1]
            return dp[node]

        for i in range(1, n + 1):
            if dp[i] == -1:
                dp[i] = dfs(i)

        return max(dp)
```

TODO