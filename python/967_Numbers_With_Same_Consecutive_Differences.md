## Numbers With Same Consecutive Differences

Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

Example 1:

```
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
```

Example 2:

```
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
```

Constraints:

```
2 <= n <= 9
0 <= k <= 9
```

第一眼看上去就是用 bfs 最好，直接上 queue，但是写了半个多小时还是调试不出来，还是菜了。。直接上 lee215 大佬的答案和届时吧：

Explanation

```
We initial the current result with all 1-digit numbers,
like cur = [1, 2, 3, 4, 5, 6, 7, 8, 9].

Each turn, for each x in cur,
we get its last digit y = x % 10.
If y + K < 10, we add x * 10 + y + K to the new list.
If y - K >= 0, we add x * 10 + y - K to the new list.

We repeat this step N - 1 times and return the final result.


Complexity
If K >= 5, time and Space O(N)
If K <= 4, time and space O(2^N)
```

```Java

    public int[] numsSameConsecDiff(int N, int K) {
        List<Integer> cur = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);
        for (int i = 2; i <= N; ++i) {
            List<Integer> cur2 = new ArrayList<>();
            for (int x : cur) {
                int y = x % 10;
                if (y + K < 10)
                    cur2.add(x * 10 + y + K);
                if (K > 0 && y - K >= 0)
                    cur2.add(x * 10 + y - K);
            }
            cur = cur2;
        }
        return cur.stream().mapToInt(j->j).toArray();
    }
```

```C++

    vector<int> numsSameConsecDiff(int N, int K) {
        vector<int> cur = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        for (int i = 2; i <= N; ++i) {
            vector<int> cur2;
            for (int x : cur) {
                int y = x % 10;
                if (y + K < 10)
                    cur2.push_back(x * 10 + y + K);
                if (K > 0 && y - K >= 0)
                    cur2.push_back(x * 10 + y - K);
            }
            cur = cur2;
        }
        return cur;
    }
```

```Python

    def numsSameConsecDiff(self, N, K):
        cur = range(1, 10)
        for i in range(N - 1):
            cur = {x * 10 + y for x in cur for y in [x % 10 + K, x % 10 - K] if 0 <= y <= 9}
        return list(cur)
```

再来一个 dfs 的：

```python
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def dfs(n: int, num: int) -> None:
            if n == 1:
                ans.append(num)
            else:
                for num2 in [num * 10 + d for d in {num % 10 - K, num % 10 + K} if 0 <= d < 10]:
                    dfs(n - 1, num2)

        ans = []
        for i in range(1, 10):
            dfs(N, i)
        return ans

```

```java
class Solution {
    public int[] numsSameConsecDiff(int N, int K) {
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i < 10; ++i) {
            dfs(N, K, i, ans);
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
    private void dfs(int n, int K, int num, List<Integer> ans) {
        if (n == 1) {
            ans.add(num);
        }else {
            int digit1 = num % 10 - K, digit2 = num % 10 + K;
            if (digit1 >= 0) {
                dfs(n - 1, K, num * 10 + digit1, ans);
            }
            if (digit2 != digit1 && digit2 < 10) {
                dfs(n - 1, K, num * 10 + digit2, ans);
            }
        }
    }
}
```

再来一个 bfs 的方法，很直接，很好懂，惭愧了。。居然没搞定这个。。

```python
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # 初始化队列：2 <= n <= 9
        q = collections.deque(range(1, 10))
        while n > 1:
            for _ in range(len(q)):
                u = q.popleft()
                for v in {u % 10 - k, u % 10 + k}:  # 不用集合就判断k=0
                    if 0 <= v <= 9:
                        q.append(u * 10 + v)
            n -= 1  # 层数
        return list(q)  # 最后一层队列元素
```
