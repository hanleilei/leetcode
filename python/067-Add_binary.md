# Add binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

#### 简单。。

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(eval('0b'+a) +eval('0b'+b))[2:]
```

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(str(a), 2) + int(str(b), 2))[2:]
```

下面的思路很巧妙，来自于 NotOnlySuccess 的b站视频，主要思想就是：用代码模拟二进制加法的过程，从最低位开始逐位相加，并处理进位。

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        string c;
        int carry = 0;
        for (int i = a.size() - 1, j = b.size() - 1; i>= 0 || j >= 0; i--, j--){
            int A = i >= 0 ? a[i] - '0': 0;
            int B = j >= 0 ? b[j] - '0': 0;
            c += (A^B^carry) + '0';
            carry = ((A^B) &carry) | (A&B);
        }
        if (carry) c += '1';
        ranges::reverse(c);
        return c;
    }
};
```

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            A = int(a[i]) if i >= 0 else 0
            B = int(b[j]) if j >= 0 else 0
            c.append(str(A ^ B ^ carry))  # 当前位的和
            carry = (A & B) | (carry & (A ^ B))  # 进位
            
            i -= 1
            j -= 1
        
        return ''.join(reversed(c))  # 翻转并返回结果
```
