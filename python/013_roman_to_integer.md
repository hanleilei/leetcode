# Roman to integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

#### 首先将罗马数字翻转，从小的开始累加，如果遇到CM（M-C=1000-100=900），因为翻转过来是MC，M=1000先被累加，所以使用一个last变量，把M记录下来，如果下一个数小于M，那么减两次C，然后将C累加上，这个实现比较巧妙简洁。



```python
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        res = 0
        cache = None

        for i in s[::-1]:
            if cache and cache > d[i]:
                res -= d[i] * 2
            res += d[i]
            cache = d[i]
        return res
```
