# Jump Game VII

You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3.
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false

Constraints:

2 <= s.length <= 10^5
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length

dp + 前缀和：

从下标 i 跳到下标 j，需要满足 s[j]=0，并且 $i+minJump≤j≤min(i+maxJump,n−1)$ 换句话说，能跳到 j 的 i 必须满足 $max(j−maxJump,0)≤i≤j−minJump$ 想一想，最后一步发生了什么？

- 最后一步跳到 n−1。
- 枚举起跳位置为 i，问题变成能否从 0 跳到 i，这是规模更小的子问题。

定义 f[j] 表示能否从下标 0 跳到下标 j。

枚举上一步的位置 i，如果在区间 [max(j−maxJump,0),j−minJump] 中存在下标 i 满足 f[i]=true，那么 f[j]=true。

初始值：f[0]=true。注意题目保证 s[0]=0。

答案：f[n−1]。

这样做的时间复杂度为 O(n(maxJump−minJump))，最坏情况下是 O(n^2) 的，太慢了。

优化:

把 false 视作 0，true 视作 1，计算 f 的前缀和数组 sum。关于 sum 数组的定义，请看 前缀和。

区间 [max(j−maxJump,0),j−minJump] 中存在下标 i 满足 f[i]=true，等价于 f 的子数组 [max(j−maxJump,0),j−minJump] 的元素和大于 0。用前缀和表示为

$sum[j−minJump+1]−sum[max(j−maxJump,0)]>0$

即

$sum[j−minJump+1]>sum[max(j−maxJump,0)]$

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        f = [False] * n
        sum_ = [0] * (n + 1)  # f 的前缀和
        f[0] = True
        sum_[1] = 1

        for j in range(1, n):
            f[j] = j >= minJump and s[j] == '0' and sum_[j - minJump + 1] > sum_[max(j - maxJump, 0)]
            sum_[j + 1] = sum_[j] + f[j]

        return f[-1]
```

f 数组可以优化掉。

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        sum_ = [0] * (n + 1)  # f 的前缀和
        sum_[1] = 1

        for j in range(1, n):
            sum_[j+1] = sum_[j]
            if j >= minJump and s[j] == '0' and sum_[j - minJump + 1] > sum_[max(j - maxJump, 0)]:
                sum_[j + 1] += 1

        return sum_[n] > sum_[n - 1]
```

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False

        # dp[i] 表示能否到达位置 i
        dp = [False] * n
        dp[0] = True

        # count 记录当前跳跃窗口内可达的位置数
        count = 0
        for i in range(1, n):
            # 进入窗口：i >= minJump 时，加入左边界
            if i >= minJump:
                count += dp[i - minJump]
            # 离开窗口：i > maxJump 时，移除右边界
            if i > maxJump:
                count -= dp[i - maxJump - 1]

            # 只要窗口内有可达位置，且当前不是障碍，就能跳到这里
            dp[i] = count > 0 and s[i] == '0'

        return dp[n - 1]
```

差分数组

当我们跳到下标 i 时，需要标记 [i+minJump,i+maxJump] 中的下标都可以跳到（都可以访问）。
用一个数组 a 记录标记次数。当我们跳到下标 i 时，把区间 [i+minJump,i+maxJump] 中的 a[j] 都加一。如果 a[j]>0 说明 j 可以跳到，如果 a[j]=0 说明 j 无法跳到。

计算差分数组的前缀和，就得到了数组 a。一开始我们在下标 0，要把区间 [0,0] 加一，这样我们可以知道下标 0 是一个可以访问的下标。

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        diff = [0] * (n + 1)

        diff[0] = 1
        diff[1] = -1

        sum_d = 0
        for i, ch in enumerate(s):
            sum_d += diff[i]
            if sum_d > 0 and ch == "0":
                diff[min(i + minJump, n)] += 1
                diff[min(i + maxJump + 1, n)] -= 1
        return sum_d > 0 and s[-1] == "0" 
```

在不断往右跳的过程中，窗口 [i+minJump,i+maxJump] 也在向右滑动。窗口右边的还没有被我们访问到的下标，都在 s 的后缀中。

于是，用一个下标 j 表示：还没有访问到的下标为 [j,n)。初始值 j=1。当我们跳到下标 i 时，暴力标记 [max(j,i+minJump),i+maxJump] 中的下标都被访问到。然后更新 j 为 i+maxJump+1。

由于 j 只会增大，不会减小，所以总体时间复杂度是 O(n)。

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        can_reach = [False] * n
        can_reach[0] = True

        j = 1
        for i, ch in enumerate(s):
            if ch == '0' and can_reach[i]:
                mx = min(i + maxJump, n - 1)
                j = max(j, i + minJump)

                while j <= mx:
                    can_reach[j] = True
                    j += 1
                if j == n:
                    break
        return s[-1] == "0" and can_reach[-1]
```

bfs + 区间剪枝：

使用last_max剪枝，避免重复检查重叠区间。每个索引最多被考虑一次（因为每个索引只会被第一个能跳到它的点覆盖，由于last_max递增）。

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False  

        n = len(s)
        cur_list = [0]
        last_max = 0

        while cur_list:
            next_list = []

            for point in cur_list:
                start = max(point + minJump, last_max+1)
                end = point + maxJump + 1 
                if start < n and end >= n:
                    return True
                elif start >= n:
                    return False

                for test_p in range(start, end):
                    if s[test_p] == '0':
                        next_list.append(test_p)
                last_max = end - 1

            cur_list = next_list

        return False
```

dfs + 局部枚举：

这个方法的性能只能说是不稳定，但是在国际版的leetcode上是可以通过的。每个索引最多被访问一次（因为每个索引只会被第一个能跳到它的点覆盖）。分析得到的问题是：

```
s = "0" * 100000
minJump = 1
maxJump = 50000
```

这样的测试用例，会导致每个索引被访问两次，第一次访问时，枚举 [i+1,i+50000]，第二次访问时，枚举 [i+50001,i+100000]。总的时间复杂度是 O(n^2)。

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1' or '1' * maxJump in s:
            return False
        n = len(s)
        if minJump == maxJump:
            return (n - 1) % minJump == 0 and '1' not in s[::minJump]

        maxJump_1 = maxJump + 1
        n_maxJump_1 = n - maxJump_1
        n_minJump = n - minJump
        
        visited = set([0])
        stack = [0]
        while stack:
            i = stack.pop()
            lower = i + minJump
            for j, c in enumerate(s[lower:min(n_minJump, i + maxJump_1)], start=lower):
                if j not in visited and c == '0':
                    if j >= n_maxJump_1:
                        return True
                    stack.append(j)
                    visited.add(j)
            
        return False
```
