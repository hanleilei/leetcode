# Check if Binary String Has at Most One Segment of Ones

[[string]]

Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true

Constraints:

1 <= s.length <= 100
s[i]​​​​ is either '0' or '1'.
s[0] is '1'.

## Solution: String Manipulation

s 不含前导零，那么只含一段连续 1 的 s 只有两种情况：

s 全是 1。
s 是 11⋯100⋯0，一段 1 和一段 0。
如果 s 包含多段连续的 1，比如示例 1 的 s=1001，在 0 的后面还有 1。所以检查 s 是否包含 01 即可。

注：只有一个 1 也算一段连续的 1。

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s
```

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len([i for i in s.split("0") if i != ""]) == 1
```
