# Binary Prefix Divisible By 5

Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

## Example 1

```text
Input: [0,1,1]
Output: [true,false,false]
Explanation:
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
```

## Example 2

```text
Input: [1,1,1]
Output: [false,false,false]
```

## Example 3

```text
Input: [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]
```

## Example 4

```text
Input: [1,1,1,0,1]
Output: [false,false,false,false,false]
```

## Note

* 1 <= A.length <= 30000
* A[i] is 0 or 1

虽然在循环体中的 '% 5' 并不是必须的，但是会极大拖慢系统的速度。

```python
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        # 从左往右，每一个数是之前的数字乘2，再除以 5

        for i in range(1, len(A)):
            A[i] += A[i-1] * 2 % 5
        return [i % 5 == 0 for i in A]
```

大佬的状态机写法：

状态转移表推导
让我们逐个计算 stateSet[state][bit]:

```text
State 0 (余数为0)
添加bit 0: (0*2 + 0) % 5 = 0 % 5 = 0 → 转移到state 0
添加bit 1: (0*2 + 1) % 5 = 1 % 5 = 1 → 转移到state 1
结果: [0, 1]
State 1 (余数为1)
添加bit 0: (1*2 + 0) % 5 = 2 % 5 = 2 → 转移到state 2
添加bit 1: (1*2 + 1) % 5 = 3 % 5 = 3 → 转移到state 3
结果: [2, 3]
State 2 (余数为2)
添加bit 0: (2*2 + 0) % 5 = 4 % 5 = 4 → 转移到state 4
添加bit 1: (2*2 + 1) % 5 = 5 % 5 = 0 → 转移到state 0
结果: [4, 0]
State 3 (余数为3)
添加bit 0: (3*2 + 0) % 5 = 6 % 5 = 1 → 转移到state 1
添加bit 1: (3*2 + 1) % 5 = 7 % 5 = 2 → 转移到state 2
结果: [1, 2]
State 4 (余数为4)
添加bit 0: (4*2 + 0) % 5 = 8 % 5 = 3 → 转移到state 3
添加bit 1: (4*2 + 1) % 5 = 9 % 5 = 4 → 转移到state 4
```

所以完整的状态转移表：

```python
stateSet = [
    [0, 1],  # state 0: bit0→0, bit1→1
    [2, 3],  # state 1: bit0→2, bit1→3
    [4, 0],  # state 2: bit0→4, bit1→0
    [1, 2],  # state 3: bit0→1, bit1→2
    [3, 4]   # state 4: bit0→3, bit1→4
]
```

```python
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        state = 0
        res = list()
        stateSet = [[0, 1], [2, 3], [4, 0], [1, 2], [3, 4]]
        for i in nums:
            state = stateSet[state][i]
            res.append(state == 0)
        return res
```
