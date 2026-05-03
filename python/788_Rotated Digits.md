# Rotated Digits

[[dp]]

An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

    0, 1, and 8 rotate to themselves,
    2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
    6 and 9 rotate to each other, and
    the rest of the numbers do not rotate to any other number and become invalid.

Given an integer n, return the number of good integers in the range [1, n].

Example 1:

Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Example 2:

Input: n = 1
Output: 0

Example 3:

Input: n = 2
Output: 1

Constraints:

    1 <= n <= 10^4

根据题意，好数中不能有 3,4,7，且至少包含 2,5,6,9 中的一个。

将 n 转换成字符串 s，定义 f(i,hasDiff,isLimit,isNum) 表示构造从左往右第 i 位及其之后数位的合法方案数，其余参数的含义为：

    hasDiff 表示前面填的数字是否包含 2,5,6,9（至少一个）。
    isLimit 表示当前是否受到了 n 的约束。若为真，则第 i 位填入的数字至多为 s[i]，否则可以是 9。如果在受到约束的情况下填了 s[i]，那么后续填入的数字仍会受到 n 的约束。
    isNum 表示 i 前面的数位是否填了数字。若为假，则当前位可以跳过（不填数字），或者要填入的数字至少为 1；若为真，则要填入的数字可以从 0 开始。

后面两个参数可适用于其它数位 DP 题目。

枚举要填入的数字，具体实现逻辑见代码。对于本题来说，由于前导零对答案无影响，isNum 可以省略。

下面代码中 Java/C++/Go 只需要记忆化 (i,hasDiff) 这个状态，因为：

    对于一个固定的 (i,hasDiff)，这个状态受到 isLimit 的约束在整个递归过程中至多会出现一次，没必要记忆化。比如 n=1234，当 i=2 的时候，前面可以填 10,11,12 等等，如果受到 isLimit 的约束，就说明前面填的是 12。「当 i=2 的时候，前面填的是 12」这件事情，在整个递归中只会发生一次。
    另外，如果只记忆化 (i,hasDiff)，dp 数组的含义就变成在不受到约束时的合法方案数，所以要在 !isLimit 成立时才去记忆化。接着上面的例子，在前面填 12 的时候，下一位填的数字不能超过 3，因此算出来的结果是不能套用到前面填的是 10,11 这些数字上面的。

通用数位dp：

```python
diffs = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)

        @cache
        def f(i: int, has_diff: bool, is_limit: bool) -> int:
            if i == len(s):
                return has_diff # 只有包含 2/5/6/9才算一个好数
            
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(up + 1): # 枚举需要填入的数字 d
                if diffs[d] != -1: # d不是3/4/7
                    res += f(i + 1, has_diff or diffs[d], is_limit and d == up)
            return res
        
        return f(0, False, True)
```

```python
mapping = {
    "0": "0",
    "1": "1",
    "2": "5",
    "5": "2",
    "6": "9",
    "8": "8",
    "9": "6"
}

class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            if self.check(i):
                res += 1
        return res
    
    def check(self, n: int) -> bool:
        s = str(n)
        rotated_chars = []
        for ch in s:
            if ch not in mapping:
                return False
            rotated_chars.append(mapping[ch])
        
        return int(''.join(rotated_chars)) != n
```
