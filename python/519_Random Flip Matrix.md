# Random Flip Matrix

There is an m x n binary grid matrix with all the values set 0 initially. Design an algorithm to randomly pick an index (i, j) where matrix[i][j] == 0 and flips it to 1. All the indices (i, j) where matrix[i][j] == 0 should be equally likely to be returned.

Optimize your algorithm to minimize the number of calls made to the built-in random function of your language and optimize the time and space complexity.

Implement the Solution class:

Solution(int m, int n) Initializes the object with the size of the binary matrix m and n.
int[] flip() Returns a random index [i, j] of the matrix where matrix[i][j] == 0 and flips it to 1.
void reset() Resets all the values of the matrix to be 0.
 

Example 1:

Input
["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]
Output
[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

Explanation
Solution solution = new Solution(3, 1);
solution.flip();  // return [1, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.
solution.flip();  // return [2, 0], Since [1,0] was returned, [2,0] and [0,0]
solution.flip();  // return [0, 0], Based on the previously returned indices, only [0,0] can be returned.
solution.reset(); // All the values are reset to 0 and can be returned.
solution.flip();  // return [2, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.
 

Constraints:

1 <= m, n <= 104
There will be at least one free cell for each call to flip.
At most 1000 calls will be made to flip and reset.

```python
import random
from typing import List

class Solution:

    def __init__(self, m: int, n: int):
        self.d = {}
        self.remain = m * n
        self.row_size = m
        self.col_size = n

    def flip(self) -> List[int]:
        # 第1步: 生成一个0..remain-1 之间的随机数
        x = random.randint(0, self.remain - 1)
        self.remain -= 1
        
        # 第2步: 检查这个数字是否被占用过，如果有映射就用映射的值
        idx = self.d.get(x, x)
        
        # 第3步: 建立当前数字到末尾数字的映射关系
        # 如果末尾数字有映射就用映射的值，否则用末尾数字本身
        self.d[x] = self.d.get(self.remain, self.remain)
        
        # 计算行和列
        return [idx // self.col_size, idx % self.col_size]

    def reset(self) -> None:
        self.remain = self.row_size * self.col_size
        self.d.clear()
```
