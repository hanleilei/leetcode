# Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

## Example:
```
Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```

先来一个内建的二分法，速度很快，这个方法真的很棒：
```python
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sorted_values_seen, out = [], []
        for n in nums[::-1]:
            idx = bisect.bisect_left(sorted_values_seen,n)
            sorted_values_seen.insert(idx,n)
            out.append(idx)
        return out[::-1]
```

再来一个merge sort的：

```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
```

再来一个segment tree的方法，但是很慢：

```python
class Solution:
    def countSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = SegmentTree(len(hashTable)), []
        for i in range(len(nums) - 1, -1, -1):
            r.append(tree.sum(0, hashTable[nums[i]] - 1))
            tree.update(hashTable[nums[i]], 1)
        return r[::-1]

class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.children = []


class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, start, end):
        if start > end:
            return

        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root

        mid = start + end >> 1
        root.children = filter(None, [
            self.build(start, end)
            for start, end in ((start, mid), (mid + 1, end))])
        return root

    def update(self, i, val, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            return root.val

        if i == root.start == root.end:
            root.val += val
            return root.val

        root.val = sum([self.update(i, val, c) for c in root.children])
        return root.val

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0

        if start <= root.start and end >= root.end:
            return root.val

        return sum([self.sum(start, end, c) for c in root.children])
```

再来一个binary index tree：

```python
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r


class Solution(object):
    def countSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = BinaryIndexedTree(len(hashTable)), []
        for i in range(len(nums) - 1, -1, -1):
            r.append(tree.sum(hashTable[nums[i]]))
            tree.update(hashTable[nums[i]] + 1, 1)
        return r[::-1]
```
加上注释：
```python
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.num = 1

#解法二：树状数组
#树状数组是这样的数据结构，占内存大，可以很快地求出前n项和，讲解在https://www.cnblogs.com/acgoto/p/8583952.html
#这里如何应用树状数组呢，建立长度为n+1的数组，从结尾开始往前遍历，每次便利1.统计自己前面的元素2.更新这个元素进去
#下面这个类不是我自己写的，因为我记住了也看不懂，然后主类是我自己写的，就当是某种应用吧
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r

class Solution:
    def countSmaller(self, nums):
        #这里就是使用了树状数组可以求前n项和的特征，初始化的数组中，每个数的频数都是0
        tree , r = BinaryIndexedTree(len(nums)),[]
        #dic描述了数组中每个元素在原数组中是“第几大”
        dic = {i:v for v,i in enumerate(sorted(set(nums)))}

        for j in reversed(nums):
            #第dic[j]大的数，前面的数组元素之和，也就是前面有多少个数
            r.append(tree.sum(dic[j]))
            #第dic[j]大的数的对应位置+1
            tree.update(dic[j] + 1)

        return r[::-1]
```


再来一个binary search tree：

```python
class BinarySearchTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.leftTreeSize = 0


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val, root):
        if not root:
            self.root = BinarySearchTreeNode(val)
            return 0

        if val == root.val:
            root.count += 1
            return root.leftTreeSize

        if val < root.val:
            root.leftTreeSize += 1

            if not root.left:
                root.left = BinarySearchTreeNode(val)
                return 0
            return self.insert(val, root.left)

        if not root.right:
            root.right = BinarySearchTreeNode(val)
            return root.count + root.leftTreeSize

        return root.count + root.leftTreeSize + self.insert(
            val, root.right)


class Solution(object):
    def countSmaller(self, nums):
        tree = BinarySearchTree()
        return [
            tree.insert(nums[i], tree.root)
            for i in range(len(nums) - 1, -1, -1)
        ][::-1]
```
