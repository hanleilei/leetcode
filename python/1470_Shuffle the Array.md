# Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:

```text
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
```

Example 2:

```text
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
```

Example 3:

```text
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
```

Constraints:

- 1 <= n <= 500
- nums.length == 2n
- 1 <= nums[i] <= 10^3

直接上一个循环嵌套的算法：

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = list()
        for j in range(n):
            for i in range(len(nums) // n):            
                res.append(nums[i* n + j])
        return res
```

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = list()
        
        for i in range(len(nums)//2):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
```

似乎是我想复杂了，这里是2 * n个元素，也就是说，len(nums) // 2 == n,这样问题就简化了很多。

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = list()
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
```
