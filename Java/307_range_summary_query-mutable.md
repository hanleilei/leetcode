# Range Sum Query - Mutable

[[segment tree]]

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:
```
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
```

Note:

1. The array is only modifiable by the update function.
2. You may assume the number of calls to update and sumRange function is distributed evenly.

先看看stefan大大的算法，删除两行，再加上两行：

```Python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.update = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j+1])

```

直接TLE了，现在。。。

```Python
class IndexTree(object):
    def __init__(self,nums):
        n = len(nums)
        sum = [0] * (n+1)
        for i in range(1,n+1):
            sum[i] = sum[i-1] + nums[i-1]
        self.sum = [0] * (n+1)
        for i in range(1,n+1):
            self.sum[i] = sum[i] - sum[i-(i&-i)]


    def getSum(self,i):
        res = 0
        while i != 0:
            res += self.sum[i]
            i -= (i & -i)
        return res

    def update(self,i,val):
        n = len(self.sum) - 1
        while i <= n:
            self.sum[i] += val
            i += (i & -i)

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tree = IndexTree(nums)
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.tree.update(i+1,diff)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.getSum(j+1) - self.tree.getSum(i)
```

使用的是segment tree。

这是一道很经典的题目，通常还能拓展出一大类问题。

针对不同的题目，我们有不同的方案可以选择（假设我们有一个数组）：

数组不变，求区间和：「前缀和」、「树状数组」、「线段树」
多次修改某个数（单点），求区间和：「树状数组」、「线段树」
多次修改某个区间，输出最终结果：「差分」
多次修改某个区间，求区间和：「线段树」、「树状数组」（看修改区间范围大小）
多次将某个区间变成同一个数，求区间和：「线段树」、「树状数组」（看修改区间范围大小）
这样看来，「线段树」能解决的问题是最多的，那我们是不是无论什么情况都写「线段树」呢？

答案并不是，而且恰好相反，只有在我们遇到第 4 类问题，不得不写「线段树」的时候，我们才考虑线段树。

因为「线段树」代码很长，而且常数很大，实际表现不算很好。我们只有在不得不用的时候才考虑「线段树」。

总结一下，我们应该按这样的优先级进行考虑：

简单求区间和，用「前缀和」
多次将某个区间变成同一个数，用「线段树」
其他情况，用「树状数组」
树状数组

本题显然属于第 2 类问题：多次修改某个数，求区间和。

我们使用「树状数组」进行求解。

「树状数组」本身是一个很简单的数据结构，但是要搞懂其为什么可以这样「查询」&「更新」还是比较困难的（特别是为什么可以这样更新），往往需要从「二进制分解」进行出发理解。

```java
class NumArray {
    int[] tree;
    int lowbit(int x) {
        return x & -x;
    }
    int query(int x) {
        int ans = 0;
        for (int i = x; i > 0; i -= lowbit(i)) ans += tree[i];
        return ans;
    }
    void add(int x, int u) {
        for (int i = x; i <= n; i += lowbit(i)) tree[i] += u;
    }

    int[] nums;
    int n;
    public NumArray(int[] _nums) {
        nums = _nums;
        n = nums.length;
        tree = new int[n + 1];
        for (int i = 0; i < n; i++) add(i + 1, nums[i]);
    }
    
    public void update(int i, int val) {
        add(i + 1, val - nums[i]);
        nums[i] = val;
    }
    
    public int sumRange(int l, int r) {
        return query(r + 1) - query(l);
    }
}
```
