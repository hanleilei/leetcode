# Equal Sum Grid Partition II

You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

    Each of the two resulting sections formed by the cut is non-empty.
    The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
    If a cell is discounted, the rest of the section must remain connected.

Return true if such a partition exists; otherwise, return false.

Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

Example 1:

Input: `grid = [[1,4],[2,3]]`

Output: true

Explanation:

![](https://assets.leetcode.com/uploads/2025/03/30/lc.jpeg)

    A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.

Example 2:

Input: `grid = [[1,2],[3,4]]`

Output: true

Explanation:

![](https://assets.leetcode.com/uploads/2025/04/01/chatgpt-image-apr-1-2025-at-05_28_12-pm.png)

    A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
    By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.

Example 3:

Input: `grid = [[1,2,4],[2,3,5]]`

Output: false

Explanation:

![](https://assets.leetcode.com/uploads/2025/04/01/chatgpt-image-apr-2-2025-at-02_50_29-am.png)

    A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
    By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.

Example 4:

Input: `grid = [[4,1,8],[3,2,6]]`

Output: false

Explanation:

No valid cut exists, so the answer is false.

Constraints:

    1 <= m == grid.length <= 10^5
    1 <= n == grid[i].length <= 10^5
    2 <= m * n <= 10^5
    1 <= grid[i][j] <= 10^5

```python
#枚举右,维护左+分类大模拟,参考前排大神写法
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        s=sum(map(sum,grid)) #矩阵总和
        def g(grid):
            n,m=len(grid),len(grid[0])
            pre,p=set(),0
            for i,row in enumerate(grid):
                p+=sum(row)
                for x in row:
                    pre.add(x)
                if p*2==s: #上部等于下部,无需去除
                    return True
                #上部和大于下部和,去除上部元素
                #注意,当列数大于一行且上部为n行下部为0行(或者只有一行)时,不满足if条件
                #因为2*p-s此时等于s,而哈希表pre中只记录单个元素的和,s是一定不存在于pre中的
                if p>s-p and 2*p-s in pre:
                    #上部行数介于1~n-1之间,且列数大于1
                    if m>1:
                        #上部大于1行,随便去除,直接返回True
                        if i:
                            return True
                        #上部只有1行,只能去除开头或者结尾
                        if 2*p-s==row[0] or 2*p-s==row[-1]:
                            return True
                    #只有1列的情况,分两种讨论
                    #1.去除上端点,2.去除分界线上面的点(例如上部是1~3行,下部是4~5行,我们可以去除第3行)
                    if 2*p-s==grid[0][0] or 2*p-s==row[0]:
                        return True
            return False
        #g函数只考虑去除上部元素,将g翻转(第n行变成第1行,n-1行变成第2行,...)
        #由对称性可处理去除下部元素的情况
        def f(grid: List[List[int]]):
            return g(grid) or g(grid[::-1])
        #f函数只处理上下分割的情况,将grid原地转置之后即可处理左右分割的情况
        return f(grid) or f(list(zip(*grid)))
```

```python
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        # 能否水平分割
        def check(a: List[List[int]]) -> bool:
            m, n = len(a), len(a[0])

            # 删除上半部分中的一个数，能否满足要求
            def f(a: List[List[int]]) -> bool:
                st = {0}  # 0 对应不删除数字
                s = 0
                for i, row in enumerate(a[:-1]):
                    for j, x in enumerate(row):
                        s += x
                        # 第一行，不能删除中间元素
                        if i > 0 or j == 0 or j == n - 1:
                            st.add(x)
                    # 特殊处理只有一列的情况，此时只能删除第一个数或者分割线上那个数
                    if n == 1:
                        if s * 2 == total or s * 2 - total == a[0][0] or s * 2 - total == row[0]:
                            return True
                        continue
                    if s * 2 - total in st:
                        return True
                    # 如果分割到更下面，那么可以删第一行的元素
                    if i == 0:
                        st.update(row)
                return False

            # 删除上半部分中的数 or 删除下半部分中的数
            return f(a) or f(a[::-1])

        # 水平分割 or 垂直分割
        return check(grid) or check(list(zip(*grid)))
```
