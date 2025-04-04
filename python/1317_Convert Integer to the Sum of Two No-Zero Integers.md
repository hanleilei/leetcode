# Convert Integer to the Sum of Two No-Zero Integers

No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.

Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.

Constraints:

2 <= n <= 10**4

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if '0' not in f'{i}{n - i}':
                return [i, n - i]
```

什么是 f-string？
f-string 是 Python 3.6 及以上版本引入的一种字符串格式化方法。它允许你在字符串前加上字母 f 或 F，然后在字符串内部用大括号 {} 包含变量或表达式，这些变量或表达式会被自动求值并插入到字符串中相应的位置。

f'{i}{n - i}' 的含义
在你的代码中，f'{i}{n - i}' 的作用是将整数 i 和 n - i 转换为字符串，并将它们连接在一起。例如：

如果 i = 1 且 n = 2，那么 f'{i}{n - i}' 就是 '11'。
如果 i = 10 且 n = 20，那么 f'{i}{n - i}' 就是 '1010'。

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        while i < n:
            if '0' not in str(i) and '0' not in str(n - i):
                return [i, n - i]
            i += 1
```

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        while '0' in f'{a}{n-a}':
            a += 1
        return [a, n-a]
```
