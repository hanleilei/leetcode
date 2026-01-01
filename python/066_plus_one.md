# plus one

[[simulation]]

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

## Example 1

```text
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

## Example 2

```text
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

就是考察python的列表推导式

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

思路：

1. 配置flag 为1，从最后一位开始遍历，如果小于9，直接加flag， 然后flag配置为0。
2. 这样，如果是最后一位是0，则其他位置什么都不变。
3. 如果遇到9，看flag是多少，如果当前位置不是最右边（这个通过flag来判断），则跳过
4. 最后再判断flag，这个是针对999这种情况的，如果是999，则最后一位是0，其他位置都是0，所以需要在最前面加1。

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = list()
        flag = 1
        for i in range(len(digits) - 1, -1 ,-1):
            if digits[i] < 9:
                digits[i] += flag
                flag = 0
            else:
                if flag:
                    digits[i] = 0
                    flag = 1
        return [1] + digits if flag else digits
```

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        digits.back() += 1;
        for (int i = digits.size() - 1; i >= 0 && digits[i] == 10; i--){
            digits[i] = 0;
            if (i == 0) digits.insert(digits.begin(), 1);
            else digits[i-1] += 1;
        }
        return digits;
    }
};
```

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 在最后一位加1
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            # 如果当前位为10，需要进位
            if digits[i] == 10:
                digits[i] = 0
                # 如果是最左边一位，插入 1
                if i == 0:
                    digits.insert(0, 1)
                else:
                    digits[i - 1] += 1
        return digits
```

手搓一个：

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 0
        for i in range(len(digits)):
            if i == 0:
                digits[i] += 1
            else:
                digits[i] += carry
            carry, digits[i] = divmod(digits[i], 10)
        if carry == 1:
            digits.append(1)
        return digits[::-1]
```
