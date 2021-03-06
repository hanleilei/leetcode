# string to integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
```
Input: "42"
Output: 42
```

Example 2:
```
Input: "   -42"
Output: -42
```

Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:
```
Input: "4193 with words"
Output: 4193
```
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:
```
Input: "words and 987"
Output: 0
```

Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:
```
Input: "-91283472332"
Output: -2147483648
```
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

先来一个简单的：

```python
class Solution:
    def myAtoi(self, s):
        """
        :type str: s
        :rtype: int
        """
        l, sign, op, tmp= list(s), 1, ['-','+'], []
        while l and l[0] == ' ':
            l.pop(0)
        if l and l[0] in op:
            sign = op.index(l[0])*2 - 1
            l.pop(0)
        while l and l[0].isdigit() == True:
            tmp.append(l[0])
            l.pop(0)
        if tmp: return min(max(sign*int(''.join(tmp)),-2**31),2**31-1)
        else: return 0

```

但是这题只需要考虑数字和符号的情况：

1. 若字符串开头是空格，则跳过所有空格，到第一个非空格字符，如果没有，则返回0.

2. 若第一个非空格字符是符号+/-，则标记sign的真假，这道题还有个局限性，那就是在c++里面，+-1和-+1都是认可的，都是-1，而在此题里，则会返回0.

3. 若下一个字符不是数字，则返回0. 完全不考虑小数点和自然数的情况，不过这样也好，起码省事了不少。

4. 如果下一个字符是数字，则转为整形存下来，若接下来再有非数字出现，则返回目前的结果。

5. 还需要考虑边界问题，如果超过了整形数的范围，则用边界值替代当前值。


下面的这个方法，解决不了："0-1" 这个的结果是-1。。。
```python
class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int

        """
        base = "0123456789"
        plus = "+"
        minus = "-"
        sum = 0
        flag = 1
        bit = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if not str:
            return 0

        if len(str) == 0:
            return 0

        for letter in str.strip():
            if letter in plus:
                if bit == 0:
                    bit = 1
                    continue
                else:
                    break
            elif letter in minus:
                if bit == 0:
                    bit = 1
                    flag = -1
                    continue
                else:
                    break
            elif letter not in base:
                break;
            else:
                sum *= 10
                sum += int(letter)

        sum *= flag

        if(sum > INT_MAX):
            return INT_MAX

        if(sum < INT_MIN):
            return INT_MIN

        return sum
```
我的方法，有点乱，但是过了全部的test case：

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        from string import digits
        res = list()
        s = s.strip()

        flag = 1
        if len(s) > 0:
            if s[0] == '-':
                flag = -1
                s = s[1:]
            elif s[0] == '+':
                flag = 1
                s = s[1:]
        if s == '' or s[0] not in digits:
            return 0
        for x in s:
            if x in digits:
                res.append(x)
            else:
                 break   
        res =  int(''.join(res)) * flag
        if flag == 1:
            if res > (1<<31) -1:
                return (1<<31) -1
            else:
                return res
        else:
            if res < -(1<<31):
                return -(1<<31)
            else:
                return res
```
