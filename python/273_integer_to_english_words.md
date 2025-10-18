# integer to english words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

```text
Input: 123
Output: "One Hundred Twenty Three"
```

Example 2:

```text
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```

Example 3:

```text
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

Example 4:

```text
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```

先看看stefan大大的解法：

```python
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n//10-2]] + words(n%10)
            if n < 1000:
                return [to19[n//100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n//1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'

```


```python
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        n2w = {1e9: "Billion", 1e6: "Million", 1e3: "Thousand", 1e2: "Hundred",
               90:  "Ninety", 80:  "Eighty", 70:  "Seventy",
               60:  "Sixty", 50:  "Fifty", 40:  "Forty",
               30:  "Thirty", 20:  "Twenty", 19: "Nineteen",
               18:  "Eighteen", 17: "Seventeen", 16: "Sixteen",
               15:  "Fifteen", 14: "Fourteen", 13: "Thirteen",
               12:  "Twelve", 11:  "Eleven", 10:  "Ten",
               9:   "Nine", 8:   "Eight", 7:   "Seven",
               6:   "Six", 5:   "Five", 4: "Four", 3: "Three",
               2: "Two", 1: "One", 0: "Zero"}

        keys = [1000000000, 1000000, 1000, 100, 90, 80, 70,
               60, 50, 40, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12,
               11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        def dp(n):
            if n <= 20: return n2w[n]
            for div in keys:
                d, r = divmod(n, div)
                if not d: continue
                s1 = dp(d) + " " if div >= 100 else ""
                s2 = " " + dp(r) if r else ""
                return s1 + n2w[div] + s2

        return dp(num)
```

最后来一个速度最快的：

```python
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        v1 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        v2 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        v3 = ['Thousand', 'Million', 'Billion']

        res = []
        index = -1

        while num:
            temp = num % 1000
            num //= 1000
            tempRes = []

            if temp > 99:
                tempRes += v1[temp // 100],
                tempRes += 'Hundred',
                temp %= 100

            if temp > 19:
                tempRes += v2[temp // 10],
                temp %= 10

            if temp > 0:
                tempRes += v1[temp],

            if index >= 0 and tempRes:
                tempRes += v3[index],

            res = tempRes + res
            index += 1

        return ' '.join(res) if res else 'Zero'
        
```
