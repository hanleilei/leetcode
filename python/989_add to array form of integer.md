# Add to Array-Form of Integer

The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:
```
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
```
Example 2:
```
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
```
Example 3:
```
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
``` 

Constraints:

- 1 <= num.length <= 104
- 0 <= num[i] <= 9
- num does not contain any leading zeros except for the zero itself.
- 1 <= k <= 104

```python
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = list()
        for i in range(len(num)-1, -1, -1):
            res.append((num[i] + k) % 10)
            k = (num[i] + k) // 10

        while k > 0:
            res.append(k % 10)
            k //= 10
        return res[::-1]
```

```python
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = list()
        size = len(num)
        carry = 0
        while size > 0 or k > 0 or carry > 0:
            if size > 0:
                carry += num[size -1]
                size -= 1
            
            carry += k % 10
            k //= 10

            res.append(carry % 10)
            carry  //= 10

        return res[::-1]
```