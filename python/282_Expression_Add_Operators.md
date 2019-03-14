# Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

## Example 1:
```
Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
```

## Example 2:
```
Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
```

## Example 3:
```
Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
```

## Example 4:
```
Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
```

## Example 5:
```
Input: num = "3456237490", target = 9191
Output: []
```

```Python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)
```
在来一个详细注释而且速度快的。
```Python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # 声明解说数组
        res = []
        # 表达式，n个数字最多增加n-1个符号，所以表达式长度最长为2*n-1
        expression = [0] * (2 * len(num) - 1)
        # 使用深度优先搜索进行遍历搜索
        self.__dfs(num, target, 0, expression, 0, 0, 0, res)
        return res

    def __dfs(self, num, target, start, exp, vaild, prev, curr, res):
        # 递归结束条件，如果已经没有剩余的数字
        if start == len(num):
            # 如果当前已求得的和和目标相等，我们把有效的字符添加到结果中
            if curr == target:
                res.append("".join(exp[0:vaild]))
            return
        # n表示当前拆分的数字
        n = 0
        # l表示当前的有效位数
        l = vaild
        # index记录起始位置
        index = start
        if index: vaild += 1
        while start < len(num):
            # 获取数字
            n = n * 10 + (ord(num[start]) - ord('0'))
            # 如果当前起始数字为'0'(注意单独一个 0 是合法的) 则后面的所有数字都不会合法
            # 直接退出循环
            if num[index] == "0" and start != index : break
            # 将当前数字添加到表达式字符串中
            exp[vaild] = num[start]
            # 有效位数自增一次
            vaild += 1
            # 起始位置自增一次
            start += 1
            # 如果是给定字符串的第一个位置，不需要进行计算
            if index == 0:
                self.__dfs(num, target, start, exp, vaild, n, n, res)
                continue
            # 当前符号置为 「+」
            exp[l] = "+"
            self.__dfs(num, target, start, exp, vaild, n, curr + n, res)
            # 当前符号置为 「-」
            exp[l] = "-"
            self.__dfs(num, target, start, exp, vaild, -n, curr - n, res)
            # 当前符号置为 「*」
            exp[l] = "*"
            self.__dfs(num, target, start, exp, vaild, prev * n,curr - prev + prev * n, res)
```
