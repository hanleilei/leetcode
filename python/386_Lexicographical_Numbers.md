# Lexicographical Numbers

Difficulty: Medium

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000

按照字典序对于一个数字生成的数组进行排序。

```python
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [int(j) for j in sorted(str(i) for i in range(1, n+1))]
```

烂透了的算法，只能排序到50000左右的数字。当然可能是因为leetcode的要求苛刻。

当然还有递归算法：

```python
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        def solve(m):
            result.append(m)
            if m * 10 <= n: solve(m * 10)
            if m < n and m % 10 < 9: solve(m + 1)
        solve(1)
        return result
```
居然运行了1.4秒多，让我通过了，下面再看看还有其他什么更好的算法没有。其实也就是把上面的算法改造成正常的形式。

```python
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        stack = [1]
        while stack:
            y = stack.pop()
            result.append(y)
            if y < n and y % 10 < 9:
                stack.append(y + 1)
            if y * 10 <= n:
                stack.append(y * 10)
        return result

```
用时1.3秒，用stack的数据结构，一直在压栈，设定一个判断栈是否为空的条件。

```python
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        stack = []
        x = 1
        while x <= n:
            stack.append(x)
            result.append(x)
            x *= 10
        while stack:
            y = stack.pop()
            if y % 10 == 9: continue
            y += 1
            while y <= n:
                stack.append(y)
                result.append(y)
                y *= 10
        return result

```

这个算法更是没什么好说的还是用迭代的方式更快，如果用copy模块的deepcopy方法反而慢了。
