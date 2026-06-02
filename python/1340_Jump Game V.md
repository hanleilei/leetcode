# Jump Game V

[[dp]] [[dfs]] [[greedy]]

Given an array of integers arr and an integer d. In one step you can jump from index i to index:

    i + x where: i + x < arr.length and  0 < x <= d.
    i - x where: i - x >= 0 and  0 < x <= d.

In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.

Example 2:

Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.

Example 3:

Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies.

Constraints:

    1 <= arr.length <= 1000
    1 <= arr[i] <= 105
    1 <= d <= arr.length

DP - Top Down O(n)

写个暴力搜索，枚举所有情况。

    从 i 往左跳：枚举 j=i−1,i−2,…,max(i−d,0)。根据题目要求，遍历过的元素都必须严格小于 arr[i]，如果 arr[j]≥arr[i] 就停止枚举。然后从 j 开始继续跳。
    从 i 往右跳：枚举 j=i+1,i+2,…,min(i+d,n−1)。根据题目要求，遍历过的元素都必须严格小于 arr[i]，如果 arr[j]≥arr[i] 就停止枚举。然后从 j 开始继续跳。

考虑到整个递归过程中有大量重复递归调用（递归入参相同）。由于递归函数没有副作用，同样的入参无论计算多少次，算出来的结果都是一样的，因此可以用记忆化搜索来优化：

    如果一个状态（递归入参）是第一次遇到，那么可以在返回前，把状态及其结果记到一个 memo 数组中。
    如果一个状态不是第一次遇到（memo 中保存的结果不等于 memo 的初始值），那么可以直接返回 memo 中保存的结果。

```python
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        @cache
        def dp(i):
            res = 1
            # 往左跳
            for j in range(min(n - 1, i + 1), min(n - 1, i + d) + 1):
                if arr[j] >= arr[i]:
                    break
                res = max(res, dp(j) + 1)
            # 往右跳
            for j in range(max(0, i - 1), max(0, i - d) - 1, -1):
                if arr[j] >= arr[i]:
                    break
                res = max(res, dp(j) + 1)
            return res
        return max(map(dp, range(n)))
```

dp - bottom up O(nlogn)

```python
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n
        sorted_arr = sorted([(x, i) for i, x in enumerate(arr)])
        for x, i in sorted_arr[1:]:
            for j in range(min(n - 1, i + 1), min(n - 1, i + d) + 1):
                if arr[j] >= x:
                    break
                dp[i] = max(dp[i], dp[j] + 1)
            
            for j in range(max(0, i - 1), max(0, i - d) - 1, -1):
                if arr[j] >= x:
                    break
                dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```

monotonic stack + dfs O(n)

逆向思维，倒着跳，从下标 i 跳到下标 j，需要满足：

    i 到 j 之间（包含 i 不包含 j）的每个数都严格小于 arr[j]。

上图中的元素 7 往左可以跳到元素 9,13,14，往右可以跳到元素 10,12。由于 7 往左能跳到的元素，9 往左也可以跳到（都满足要求），所以 7→9→13 一定比 7→13 更优。

一般地，跳到左右最近的更大元素是最优的。

所以无需枚举 [i−d,i+d] 中的 j，只需考虑两个下标 j：

    arr[i] 左边最近的更大元素 arr[j]。
    arr[i] 右边最近的更大元素 arr[j]。

```python
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        left = [0] * n
        st = []
        for i, x in enumerate(arr):
            while st and arr[st[-1]] <= x:
                st.pop()
            left[i] = st[-1] if st and i - st[-1] <= d else -1
            st.append(i)
        
        right = [0] * n
        st.clear()
        for i in range(n - 1, -1, -1):
            x = arr[i]
            while st and arr[st[-1]] <= x:
                st.pop()
            right[i] = st[-1] if st and st[-1] - i <= d else -1
            st.append(i)
        
        @cache
        def dfs(i: int)-> int:
            if i < 0: 
                return 0
            return max(dfs(left[i]), dfs(right[i])) + 1
        return max(dfs(i) for i in range(n))
```

或者：

construct a DAG from possible jumps downward, then find the longest path using DFS. This gives time complexity O(nd). To achieve O(n) time complexity, we instead consider possible jumps upward, and note the nearest higher positions are sufficient. These can be found efficiently using monotone stacks.

首先，从可能的向下跳跃构建一个有向无环图（DAG），然后使用深度优先搜索（DFS）找到最长路径。这种方法的时间复杂度为 O(nd)。为了达到 O(n) 的时间复杂度，我们转而考虑可能的向上跳跃，并注意到找到最近的更高位置就足够了。这些位置可以使用单调栈高效地找到。

```python
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        graph = defaultdict(list)

        def jump(iterator):
            stack = []
            for i in iterator:
                while stack and arr[stack[-1]] < arr[i]:
                    j = stack.pop()
                    if abs(i - j) <= d:
                        graph[j].append(i)
                stack.append(i)
        
        jump(range(n))
        jump(reversed(range(n)))

        @lru_cache(maxsize=None)
        def height(i):
            return 1 + max(map(height, graph[i]), default = 0)
    
        return max(map(height, range(n)))
```
