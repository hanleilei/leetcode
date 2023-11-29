# Smallest Number in Infinite Set

[[heap]]

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

## Example 1

```text
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
```

## Constraints

```text
1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
```

有时候，总想着追求极致的完美，这是病，要治疗，看看数据量才1000，我是说这里：`if num not in self.heap:`

```python
class SmallestInfiniteSet:

    def __init__(self):
        import heapq
        self.heap = list(range(1, 1001))
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
```

下面是我卡了很长时间没有解决的代码：

```python
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list()
        self.n = 1

    def popSmallest(self) -> int:
        if self.heap and self.heap[0] < self.n:
            return heapq.heappop(self.heap)
        else:
            self.n += 1            
            return self.n - 1

    def addBack(self, num: int) -> None:
        if (self.heap and num < self.n) or (len(self.heap)== 0 and num < self.n):
            heapq.heappush(self.heap, num)

```

看起来似乎是没有问题，也确实，一共135个测试用例，最后133的报错了，测试结果很长，没办法debug。。大概率是某个 corner case 没考虑到的问题。

真没必要折磨自己。。😖😩

