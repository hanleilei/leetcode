# Delete Columns to Make Sorted

You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

```text
abc
bce
cae
```

You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.

Example 1:

```text
Input: strs = ["cba","daf","ghi"]
Output: 1
Explanation: The grid looks as follows:
cba
daf
ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
```

Example 2:

```text
Input: strs = ["a","b"]
Output: 0
Explanation: The grid looks as follows:
a
b
Column 0 is the only column and is sorted, so you will not delete any columns.
```

Example 3:

```text
Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: The grid looks as follows:
zyx
wvu
tsr
All 3 columns are not sorted, so you will delete all 3.
```

**Constraints:**

- n == strs.length
- 1 <= n <= 100
- 1 <= strs[i].length <= 1000
- strs[i] consists of lowercase English letters.

直接用python的内置函数zip和sorted即可：

注意zip(*strs)可以将字符串列表按列进行分组。

```python
class Solution:
    def minDeletionSize(self, strs):
        """
        :type A: List[str]
        :rtype: int
        """
        return sum(list(col) != sorted(col) for col in zip(*strs))
```

模拟每一列进行比较：

```python
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs[0]), len(strs)
        res = 0
        for j in range(m):
            for i in range(1, n):
                if strs[i][j] < strs[i-1][j]:
                    res += 1
                    break
        return res
```
