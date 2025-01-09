# Largest 3-Same-Digit Number in String

You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

## Note

```text
A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
```

## Example 1

```text
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
```

## Example 2

```text
Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
```

## Example 3

```text
Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
```

## Constraints

```text
3 <= num.length <= 1000
num only consists of digits.
```

什么时候medium和hard也能这么顺滑，那就可以出山了。。

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = list()
        num += "#"
        for i in range(1, len(num)-1):
            if num[i] == num[i - 1] and num[i] == num[i + 1]:
                res.append(num[i])
        return max(res) * 3 if res else ""
```

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = list()
        num += "#"
        count = 1
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                count += 1
                if count == 3:
                    res.append(num[i-1])
            else:
                count = 1
        return max(res) * 3 if res else ""
```

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        res = ""
        for i in range(n - 2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, num[i:i+3])
        return res
```

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        digits = '9876543210'
        for n in digits:
            if n * 3 in num:
                return n*3
        return ""
```
