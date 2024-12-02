# [Prime Subtraction Operation](https://leetcode.com/problems/prime-subtraction-operation/)

You are given a **0-indexed** integer array `nums` of length `n`.

You can perform the following operation as many times as you want:

* Pick an index `i` that you haven’t picked before, and pick a prime `p` **strictly less than** `nums[i]`, then subtract `p` from `nums[i]`.

Return *true if you can make `nums` a strictly increasing array using the above operation and false otherwise.*

A **strictly increasing array** is an array whose each element is strictly greater than its preceding element.

**Example 1:**

<pre><strong>Input:</strong> nums = [4,9,6,10]
<strong>Output:</strong> true
<strong>Explanation:</strong> In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.</pre>

**Example 2:**

<pre><strong>Input:</strong> nums = [6,8,11,12]
<strong>Output:</strong> true
<strong>Explanation: </strong>Initially nums is sorted in strictly increasing order, so we don't need to make any operations.</pre>

**Example 3:**

<pre><strong>Input:</strong> nums = [5,8,3]
<strong>Output:</strong> false
<strong>Explanation:</strong> It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.</pre>

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 1000`
* `<font face="monospace">nums.length == n</font>`

```python
valid = [True] * 1001
valid[0] = valid[1] = False
for i in range(2, len(valid)):
    if valid[i]:
        for j in range(i * i, len(valid), i):
            valid[j] = False
primes = [i for i in range(len(valid)) if valid[i]]


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = 0
        for num in nums:
            if num <= prev:
                return False

            i = bisect_left(primes, num - prev) - 1
            if i != -1:
                num -= primes[i]
            prev = num
        return True
  
```

或者，自建的算法，可以参考一下：

```python
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def find_primes(limit):
            # 创建一个布尔数组表示数是否为质数
            is_prime = [True] * limit
            primes = []
        
            # 0和1不是质数
            is_prime[0] = is_prime[1] = False
        
            # 从2开始遍历，每次找到一个质数就将其倍数标记为非质数
            for number in range(2, limit):
                if is_prime[number]:
                    primes.append(number)
                    for multiple in range(number * number, limit, number):
                        is_prime[multiple] = False
            return primes
    
        ps = find_primes(1000)
        for i in range(len(nums)):
            limit = nums[i] - (nums[i - 1] if i > 0 else 0)
            idx = bisect_left(ps, limit)
            if idx > 0:
                nums[i] -= ps[idx - 1]
            if i > 0 and nums[i] <= nums[i - 1]:
                return False
        return True
```
