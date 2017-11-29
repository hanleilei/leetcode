# find median from data stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

```Python

```

以下是用标准库，但是TLE了。。显然使用median函数带来了很多重复的计算，是不行的。
```Python
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # from collections import deque
        self.q = list()

        # self.c = 0


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.q.append(num)
        # self.c += 1


    def findMedian(self):
        """
        :rtype: float
        """
        from statistics import median
        return float(median(self.q))
        # return float(self.q) / self.c



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```
