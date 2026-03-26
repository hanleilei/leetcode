# multiply strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:

    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            n1 = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                n2 = ord(num2[j]) - ord('0')
                total = res[i + j + 1] + n1 * n2
                res[i + j + 1] = total % 10
                res[i + j] += total // 10
        
        result = []
        for i in range(len(res)):
            if i == 0 and res[i] == 0:
                continue
            result.append(str(res[i]))
        
        return ''.join(result)
```
