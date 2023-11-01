# Find The Original Array of Prefix Xor

you are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.

## Example 1

```text
Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]
Explanation: From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
```

## Example 2

```text
Input: pref = [13]
Output: [13]
Explanation: We have pref[0] = arr[0] = 13.
```

## Constraints

```text
1 <= pref.length <= 105
0 <= pref[i] <= 106
```

Since pref is the prefix array,
it's calculated from arr one by one,
we can doing this process reverssely to recover the original array.

Since
pref[i] = pref[i-1] ^ A[i]
so we have
pref[i] ^ pref[i-1] = A[i]

So we simply change - to ^ in the intuition solution

The reverse operation of + is -
The reverse operation of ^ is still ^
More general, we can apply this solution to prefix of any operation.

```python
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i] ^ pref[i + 1] for i in range(0, len(pref) - 1)]
```

或者：

```python
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return map(xor, pref, [0] + pref[:-1])
```
