# Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

## Example 1

```text
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```

## Example 2

```text
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```

## Example 3

```text
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

## Constraints

```text
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
```

两个方法其实是异曲同工，但是第二个写的有点绕，其实就是比较两个字符串合并起来是不是原来的字符串，还是第一个比较简介明了。

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1+str2 != str2 + str1):
            return ""
        return str1[:math.gcd(len(str1),len(str2))]
```

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        size = math.gcd(len(str1), len(str2))
        
        return str2[:size] if str2[:size] * (len(str1) // size) == str1 and str1[:size] * (len(str2) // size) == str2 else ""
```

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s = math.gcd(len(str1), len(str2))
        if str1 == str1[:s] * (len(str1) // s) and str2 == str2[:s] * (len(str2)//s) and str1[:s] == str2[:s]:
            return str1[:s]
        else:
            return ""
```
