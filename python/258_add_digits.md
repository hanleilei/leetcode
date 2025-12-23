# add digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

A naive implementation of the above process is trivial. Could you come up with other methods?
What are all the possible results?
How do they occur, periodically or randomly?
You may find this Wikipedia article useful.

一开始被递归绕进去了，还是用循环比较好，直到循环退出为止

```python
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while True:
            if num > 9:
                num = sum([int(i) for i in str(num)])
            else:
                return num

```

好吧，遇到一个更简单的方案：

```python
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
          return 0
        return (num -1) % 9 + 1
```

直接求和：

```python
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum([int(i) for i in list(str(num))])
        return num

```

再来一个求余数和求模的结合：

```python
class Solution:
    def addDigits(self, nums: int) -> int:
        while len(str(nums)) > 1:
            res = 0
            while nums // 10 > 0:
                res += nums % 10
                nums //= 10
            nums += res
        return nums
```

```python
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) >= 2:
            num = str(sum([int(i) for i in list(str(num))]))
        return int(num)
```

最后一个方法是数学方法，找规律：

```python
class Solution:
    def addDigits(self, nums: int) -> int:
        return (num - 1) % 9 + 1 if num else 0
```
