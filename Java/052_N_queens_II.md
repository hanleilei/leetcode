# N queens II

[[backtracking]] [[bitManipulation]]

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![](https://leetcode.com/static/images/problemset/8-queens.png)

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

```
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```

```java
class Solution {
    private int size;
    private int count;

    private void solve(int row, int ld, int rd){
        if (row == size){
            count++;
            return;
        }
        int pos = size & (~(row | ld | rd));
        while (pos != 0){
            int p = pos & (-pos);
            pos -= p;
            solve(row | p, (ld | p) << 1, (rd | p) >> 1);
        }
    }

    public int totalNQueens(int n) {
        count = 0;
        size = (1 << n) - 1;
        solve(0, 0, 0);
        return count;
    }
}
```

如果一开始理解有困难，就先用4皇后问题来理解一下，看看每一行的递归是怎么进行的。
