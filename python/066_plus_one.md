# plus one

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example 1:
```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```
Example 2:
```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```
#### 就是考察python的列表推导式

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(j) for j in str(int(''.join(str(i) for i in digits))+1)]

```

来个更简洁的:

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i]< 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        newNumber = [0] * (n + 1) # 处理999999这样的情况
        newNumber[0] = 1
        return newNumber
```
