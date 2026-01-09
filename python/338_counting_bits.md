# counting bits

[[dp]] [[bitManipulation]]

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

## Example 1

```text
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

## Example 2

```text
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 ```

Constraints:

```0 <= n <= 105```

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

位运算的操作：

```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        r = [0] * (num+1)
        for i in range(1, len(r)):
            r[i] = r[i & (i-1)] + 1
        return r
```

```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)
        offset = 1

        for index in range(1, num + 1):
            if offset * 2 == index:
                offset *= 2

            result[index] = result[index - offset] + 1

        return result
```

这个最快也就71ms，同样思路的golang和java都是在1ms。。
