# # Minimum Number of Moves to Make Palindrome

## Statement

Given a string `s`, return the minimum number of moves required to transform `s` into a palindrome. In each move, you can swap any two adjacent characters in `s`.

> **Note:** The input string is guaranteed to be convertible into a palindrome.

**Constraints:**

- 1≤ `s.length` ≤2000

- `s` consists of only lowercase English letters.

- `s` is guaranteed to be converted into a palindrome in a finite number of moves.

### example:

"eggeekgbbeg" -> 7

"arcacer" -> 4

"ccxx" -> 2

```python
from collections import deque

def min_moves_to_make_palindrome(s: str) -> int:

    n = len(s)
    # 1) 记录每个字符出现的索引队列
    pos = {}
    for i, ch in enumerate(s):
        pos.setdefault(ch, deque()).append(i)

    # 2) 将每个字符的最左和最右配成对，记录所有对；若有单余则记录为 center
    pairs = []
    center = -1
    for q in pos.values():
        while len(q) >= 2:
            l = q.popleft()
            r = q.pop()
            pairs.append((l, r))
        if q:
            center = q.pop()

    # 3) 按左索引升序排列配对，然后分配回文左右位置
    pairs.sort()  # 按 l 升序
    final_pos = [None] * n
    left = 0
    right = n - 1
    for l, r in pairs:
        final_pos[l] = left
        final_pos[r] = right
        left += 1
        right -= 1
    if center != -1:
        final_pos[center] = n // 2

    # 4) 计算 final_pos 数组的逆序对数（Fenwick Tree）
    #    由于 final_pos 值在 [0, n-1]，我们用 1-based 的 BIT
    BIT = [0] * (n + 1)
    def bit_update(i):
        while i <= n:
            BIT[i] += 1
            i += i & -i
    def bit_query(i):
        s = 0
        while i > 0:
            s += BIT[i]
            i -= i & -i
        return s

    inv = 0
    # 遍历 final_pos，统计当前已出现元素中比它大的个数：
    # 等价于：到当前位置 i，为 final_pos[i] 增加元素并计算已有中比它大的数
    # 常见做法：遍历 i 从 0..n-1，inv += i - query(final_pos[i]+1)
    for i, x in enumerate(final_pos):
        xi = x + 1  # 转为 1-based
        inv += i - bit_query(xi)
        bit_update(xi)

    return inv
```

再来一个网站原始的O(NlogN)的解法：

```python
def min_moves_to_make_palindrome(s):
    # Convert string to list for easier manipulation
    s = list(s)

    # Counter to keep track of the total number of swaps
    moves = 0

    # Loop to find a character from the right (s[j]) that
    # matches with a character from the left (s[i])
    i, j = 0, len(s) - 1
    while i < j:
        k = j
        while k > i:
            # If a matching character is found
            if s[i] == s[k]:
                # Move the matching character to the correct position on the right
                for m in range(k, j):
                    s[m], s[m + 1] = s[m + 1], s[m]  # Swap
                    # Increment count of swaps
                    moves += 1
                # Move the right pointer inwards
                j -= 1
                break
            k -= 1
        # If no matching character is found, it must be moved to the center of palindrome
        if k == i:
            moves += len(s) // 2 - i
        i += 1

    return moves

# Driver code
def main():
    strings = ["ccxx", "arcacer", "w", "ooooooo", "eggeekgbbeg"]

    for index, string in enumerate(strings):
        print(f"{index + 1}.\ts: {string}")
        print(f"\tMoves: {min_moves_to_make_palindrome(string)}")
        print('-' * 100)

if __name__ == "__main__":
    main()
```
