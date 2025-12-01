# H-index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

```text
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
     received 3, 0, 6, 1, 5 citations respectively.
     Since the researcher has 3 papers with at least 3 citations each and the remaining
     two with no more than 3 citations each, her h-index is 3.
```

Note: If there are several possible values for h, the maximum one is taken as the h-index

不排序：

```Python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0] * (n + 1)  # papers[i] is the number of papers with i citations.
        for c in citations:
            papers[min(n, c)] += 1  # All papers with citations larger than n is count as n.
        i = n
        s = papers[n]  # sum of papers with citations >= i
        while i > s:
            i -= 1
            s += papers[i]
        return i
```

单行，但是排序：

```Python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))
```

再来一个 counting sort 的方法：

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        nums = [0] * (max(citations) + 1)
        size = len(citations)
        total = 0
        for i in citations:
            nums[min(i, size)] += 1

        for i in range(size , -1, -1):
            total += nums[i]
            if total >= i:
                return i
        return 0
```

总体感觉这题目有点垃圾，不知所云的感觉。当作一个排序题目来看吧。。。

理解题意

这道问题理解题意要花很长时间，一个有效的办法就是：仔细研究示例，然后去理解题目的意思。我真正明白题目的意思是看到这句描述：

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。

所以 h 指数是 20 表示：引用次数大于等于 20 的文章数量最少是 20 篇。

再来理解一下题目中给出的定义：

N 篇论文中总共有 h 篇论文分别被引用了至少 h 次；
其余的 N - h 篇论文每篇被引用次数不超过 h 次。
h 指数想说的是这样一件事情：一个人的论文根据被引用的次数，有一个阈值（分水岭，就是这里的 h），引用次数大于等于这个阈值的论文是「高引用论文」。

所以理解 h 指数的时候可以把一个研究者的论文被引用的次数 按照升序排序。题目其实要我们找的是一条分割线，这条分割线的含义是：分割线右边的所有论文的引用次数都很高，并且：分割线右边的最少引用次数 >= 分割线右边的论文篇数。

重要的事情说 3 遍：

h 指数是 论文数量，不是引用次数。 h 指数是 论文数量，不是引用次数。 h 指数是 论文数量，不是引用次数。

题目要求返回的是论文数量。再看看题目的示例：
![1625998400 VBXQNr Image image](https://pic.leetcode-cn.com/1625998400-VBXQNr-image.png)
{:align=center}

这个例子有点儿特殊，论文被引用了 3 次，篇数有 3 篇。再来看一个更一般的例子：
![1625998502 XMZfqD Image image](https://pic.leetcode-cn.com/1625998502-XMZfqD-image.png)
{:align=center}

结论：这条分割线越靠左边，说明被引用的次数很多，文章还很多，h 指数越高。

在一个有范围的整数区间里中查找一个位置，可以使用二分查找，这件事情通常区别于「在有序数组里查找一个元素的值」，被称为「二分答案」。

方法：二分查找

首先确定整数的范围：

最差情况下，所有的论文被引用次数都为 0；
最好情况下，所有的论文的引用次数 >= 总共论文篇数。
因此整数区间为 [0..len]，这里 len 是输入数组的长度。

二分查找先猜一个 论文篇数 int mid = (left + right + 1) / 2（如果不太明白为什么加 1 的朋友，可以暂时先不管，这不重要）。

论文篇数和被引用次数的关系是：「高引用的被引用次数 >= 高引用的论文数」，这些论文才可以被称为「高引用」。因此在二分查找的循环体内部，可以遍历一次数组，数出大于等于 mid 的论文篇数。

如果大于等于 mid 的论文篇数大于等于 mid ，说明 h 指数至少是 mid。例如 [0,1,|3,5,6]，引用次数大于等于 2 的论文有 3 篇，说明答案至少是 2，最终答案落在区间 [mid..right] 里，此时设置 left = mid；
反面的情况不用思考，因为只要上面分析对了，最终答案落在区间 [mid..right] 的反面区间 [left..mid - 1] 里，此时设置 right = mid - 1。

```python
 class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        left = 0
        right = size
        while left < right:
            mid = (left + right + 1) // 2
            count = 0
            for c in citations:
                if c >= mid:
                    count += 1
            if count >= mid:
                left = mid
            else:
                right = mid - 1
        return left
```

再次回顾，好垃圾的题目！

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0
```

