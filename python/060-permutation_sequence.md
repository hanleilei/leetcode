# permutation sequence

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive

###### 方法

首先是要生成所需要的字符串，然后用itertools模块中的方法生成所要的序列。
最后要注意的是，可能所生成的字符串，一定要用迭代的方式，这样很节省时间，否则总是超时。

```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from itertools import permutations
        s = ''
        k = k-1
        count = 0
        for i in range(1,n+1):
            s+= str(i)
        for i in permutations(s,n):
            if count == k:
                return ''.join(i)
            else:
                count += 1

```
