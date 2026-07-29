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

$10 \leq \text{low} \leq \text{high} \leq 10^9$

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

```java
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

这类题目数据规模极小（最多 45 个合法数字），清晰度优于微优化

```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        # 起始数字 1~9
        for start in range(1, 10):
            num = 0
            # 从该起始数字开始构造连续数字
            for digit in range(start, 10):
                num = num * 10 + digit
                if low <= num <= high:
                    res.append(num)
                elif num > high:  # 提前剪枝
                    break
        return sorted(res)
```

枚举顺次数的最高位 d，然后依次把 d+1,d+2,…,9 加到顺次数的末尾，得到新的顺次数。

例如 d=5，我们会依次得到顺次数 5→56→567→5678→56789。

注意题目要求答案是有序的，最后需要对答案排序。

    注：本题保证顺次数长度至少是 2，也可以初始化顺次数为 10d+(d+1)=11d+1。

```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for d in range(1, 10):
            x = d
            for i in range(d, 10):
                if x > high:
                    break
                if x >= low:
                    res.append(x)
                x = x * 10 + i + 1
        res.sort()
        return res
```
