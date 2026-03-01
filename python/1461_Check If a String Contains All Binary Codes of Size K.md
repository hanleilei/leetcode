# Check If a String Contains All Binary Codes of Size K

[[bitManipulation]]

Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.

Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.

Constraints:

    1 <= s.length <= 5 * 10^5
    s[i] is either '0' or '1'.
    1 <= k <= 20

把子串转成整数，保存到哈希集合或者布尔数组中。

小优化：如果循环过程中发现已经找到 $2^k$ 个不同的二进制数，可以提前返回 true。

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        mask = (1 << k) - 1
        stack = set()
        x = 0
        for i, v in enumerate(s):
            x = (x << 1 & mask) | int(v)
            if i >= k - 1:
                stack.add(x)
        return len(stack) == 1 << k
```

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        MASK = (1 << k) - 1
        has = [False] * (1 << k)
        cnt = x = 0
        for i, ch in enumerate(s):
            # 把 ch 加到 x 的末尾：x 整体左移一位，然后或上 ch
            # &MASK 目的是去掉超出 k 的比特位
            x = (x << 1 & MASK) | int(ch)
            if i < k - 1 or has[x]:
                continue
            has[x] = True
            cnt += 1
            if cnt == 1 << k:
                return True
        return False
```

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False

        need = 1 << k
        if n - k + 1 < need:
            return False

        seen = [False] * need
        mask = 0
        full = need - 1
        cnt = 0

        for i, ch in enumerate(s):
            mask = ((mask << 1) & full) | (ch == '1') # remove the leftmost and append the current bit
            if i < k - 1: continue
            if not seen[mask]:
                seen[mask] = True
                cnt += 1
                if cnt == need:
                    return True
        return False
```

最快的解法是用一个整数来记录当前的 k 位二进制数，使用一个 bytearray 来记录哪些二进制数已经出现过。每次更新整数时，先左移一位（相当于去掉最高位），再加入新位。这样可以在 O(n) 时间内完成检查。

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        need = 1 << k  # 2^k，表示需要的不同子串数量
        
        # 剪枝：子串数量不足时直接返回 False
        if n - k + 1 < need:
            return False
        
        got = bytearray(need)  # 用 bytearray 记录每个二进制模式是否出现，节省内存
        mask = need - 1        # 位掩码，用于保留低 k 位（如 k=3 时，mask=0b111=7）
        
        # 初始化：计算前 k 个字符组成的二进制数
        num = 0
        for i in range(k):
            num = (num << 1) | (s[i] == '1')  # True 视为 1，False 视为 0
        
        got[num] = 1
        count = 1  # 已收集的不同子串数量
        
        # 滑动窗口遍历剩余字符
        for i in range(k, n):
            # 滚动更新整数：去掉最高位、左移、加入新位
            num = ((num << 1) & mask) | (s[i] == '1')
            
            if not got[num]:
                got[num] = 1
                count += 1
                # 提前退出：已找到所有可能的子串
                if count == need:
                    return True
        
        return False

```
