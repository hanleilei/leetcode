# Find Unique Binary String

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.

自己写的：

```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        size = len(nums[0])
        diff = set(range(2 ** size)) - set([int(i, 2) for i in nums])
        res =  bin(diff.pop())[2:] 
        return '0' * (size - len(res)) + res
```

算是把所有的场景都列出，然后pop一个值，对返回值处理一下。

速度太慢，看别人的快速算法，很巧妙：

```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        for i in range(int('1'+'0'*(n-1), 2), int('1'*n, 2)+1):
            if bin(i)[2:] not in nums:
                return bin(i)[2:]
        return '0'*n
```

这个方法确实很巧妙，因为题目限制条件，数组元素个数必须要有每个元素相同数量。所以循环就是从二进制数字1开头，到全部都是1结束。如果没有，则返回n个零。

----

再来一个康德儿对角线法：

The trick to do this question is somewhat similar to Cantor's Diagonalization. You can read about it in detail [here](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument).

Since we are given that number of bits in the number is equal to number of elements.
What we can do is we create a binary string which differs from first binary at 1st position, second binary at 2nd position, third binary at 3rd position,...and so on.

This will make sure that the binary we have made is unique (as it differs from all others at at least one position).

We create an empty string first.
And simply iterate through the binary strings while putting the flipped bit of ith bit of "binary at ith position".

```cpp
    for(int i=0; i<nums.size(); i++) 
        ans+= nums[i][i]=='0' ? '1' : '0';
```

I have created this image explaining the process for test case ["111", "001", "010"] :

![](https://assets.leetcode.com/users/images/14609e9b-672d-45de-b38a-5f86c1da5e6b_1629609053.2843444.jpeg)

```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join(['1' if num[i]=='0' else '0' for i,num in enumerate(nums)])
```

```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ''
        for i, n in enumerate(nums):
            res += '1' if (n[i]=='0') else '0'
        return res
```

这个算法，适合扩展思路。
