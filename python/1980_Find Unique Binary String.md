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
