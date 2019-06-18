# Count and say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

### 一开始理解错了题目意思，不是简单的计算某个数字，而是类似于递归的计算。而且我们现在实用的算法比udemy的简单。

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for __ in range(1, n):
            result = self.count(result)
        return result

    def count(self, s):
        result = []
        start = 0
        while start < len(s):
            curr = start + 1
            while curr < len(s) and s[start] == s[curr]:
                curr += 1
            result.extend((str(curr - start), s[start]))
            start = curr
        return "".join(result)
```
### 下面是udemy上介绍的算法改写，似乎没有上面的简洁，但是更容易理解：

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for __ in range(1, n):
            result = self.count(result)
        return result

    def count(self, s):
        r = ""
        l = len(s)

        # Check for length 1
        if l == 1:
            return s + "1"

        #Intialize Values
        last = s[0]
        cnt = 1
        i = 1

        while i < l:

            # Check to see if it is the same letter
            if s[i] == s[i - 1]:
                # Add a count if same as previous
                cnt += 1
            else:
                # Otherwise store the previous data
                r = r + str(cnt) + s[i - 1]
                cnt = 1

            # Add to index count to terminate while loop
            i += 1

        # Put everything back into run
        r = r + str(cnt) + s[i - 1]

        return r
```

### 用enumernate来实现，似乎更简洁：

```python
class Solution:
    # @return a string
    def countAndSay(self, n):
        s='1'
        for i in range(1,n):
            s=self.cal(s)
        return s

    def cal(self,s):          
        cnt=1
        length=len(s)
        ans=''
        for i ,c in enumerate(s):
            if i+1 < length and s[i]!=s[i+1]:
                ans=ans+str(cnt)+c
                cnt=1
            elif i+1 <length:
                cnt=cnt+1

            ans=ans+str(cnt)+c    
        return ans
```

```python
class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return "1"

        previous = self.countAndSay(n-1)
        digit = previous[0]
        count = 1
        res = ""
        for d in previous[1:]:
            if d == digit:
                count += 1
            else:
                res += str(count) + str(digit)
                digit = d
                count = 1
        res += str(count) + str(digit)
        return res

```
