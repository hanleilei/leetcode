# Check If N and Its Double Exist

Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

## Example 1

```text
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
```

## Example 2

```text
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
```

## Constraints

2 <= arr.length <= 500
-103 <= arr[i] <= 103

```python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = Counter(arr)
        # 判断是否有多个0
        if s[0] > 1:return True
        for n in arr:
            if s[n*2] and n != 0:
                return True
        return False
```
