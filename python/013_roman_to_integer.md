# Roman to integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

#### 首先将罗马数字翻转，从小的开始累加，如果遇到CM（M-C=1000-100=900），因为翻转过来是MC，M=1000先被累加，所以使用一个last变量，把M记录下来，如果下一个数小于M，那么减两次C，然后将C累加上，这个实现比较巧妙简洁。



```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = [ 1000, 500, 100, 50, 10, 5, 1 ]
        numerals = [ "M", "D", "C", "L", "X", "V", "I" ]
        d = dict(zip(numerals, values))
        sum = 0
        s = s[::-1]
        last = None
        for i in s:
            if last and d[i]< last:
                sum -= d[i] * 2
            sum += d[i]
            last = d[i]
        return sum


```
