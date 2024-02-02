# Sequential Digits

[[Enumeration]]

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9



```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        t = '123456789'
        res = list()
        for i in range(len(t)):
            for j in range(i + 1, len(t) + 1):
                if low <= int(t[i:j]) <= high:
                    res.append(int(t[i:j]))
        return sorted(res)

```

再来一个很hack的方法：

```python
class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        int[] allNums = {12,23,34,45,56,67,78,89,
                         123,234,345,456,567,678,789,
                         1234,2345,3456,4567,5678,6789,
                         12345,23456,34567,45678,56789,
                         123456,234567,345678,456789,
                         1234567,2345678,3456789,
                         12345678,23456789,
                         123456789};
        List<Integer> res = new ArrayList<>();
        int n = allNums.length;
        for (int i = 0; i < n; i++) {
            if (allNums[i] < low) continue;
            if (allNums[i] > high) break;
            res.add(allNums[i]);
        }
        return res;
    }
}
```
