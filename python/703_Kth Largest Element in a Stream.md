# 703. Kth Largest Element in a Stream

## 问题描述

Design a class to find the **kth largest element** in a stream.
Note that it is the kth largest element in the **sorted order**,
not the kth distinct element.

Implement `KthLargest` class:

- `KthLargest(int k, int[] nums)` Initializes the object with the
  integer k and the stream of integers nums.
- `int add(int val)` Appends the integer val to the stream and
  returns the element representing the kth largest element in the
  stream.

## 示例

**Example 1:**

```text
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

## 约束条件

- 1 <= k <= 10^4
- 0 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls will be made to add
- It is guaranteed that there will be at least k elements in the
  array when you search for the kth element

## 解法

### 方法1：最小堆（推荐）

核心思想：维护一个大小为k的最小堆，堆顶就是第k大的元素。

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        
        # 只保留k个最大的元素
        while len(self.heap) > k:
            heappop(self.heap)
    
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heapreplace(self.heap, val)
        
        return self.heap[0]
```

### 方法2：优化的最小堆（更简洁）

无论堆的大小，都先push再pop，逻辑更清晰。

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        
        while len(self.heap) > k:
            heappop(self.heap)
    
    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        
        return self.heap[0]
```

### 方法3：使用 nlargest 初始化

利用 nlargest 直接获取k个最大元素。

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # 直接获取k个最大元素，自动构成最小堆
        self.heap = nlargest(k, nums)
        heapify(self.heap)
    
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappushpop(self.heap, val)
        
        return self.heap[0]
```

## 算法分析

### 复杂度分析

| 操作 | 方法1/2/3 | 说明 |
|------|----------|------|
| 初始化 | O(n log k) | heapify是O(n)，但弹出n-k个元素需O((n-k) log k) |
| add | O(log k) | 堆的插入/删除操作 |
| 空间 | O(k) | 只维护k个元素 |

其中 n 是初始数组 nums 的长度。

为什么用最小堆而不是最大堆？

- 最小堆：维护k个最大元素，堆顶是第k大 ✅
- 最大堆：需要维护所有元素，堆顶是第1大 ❌

heapreplace vs heappushpop：

- `heapreplace(heap, val)`：先pop再push，可能会弹出刚插入的元素
- `heappushpop(heap, val)`：先push再pop，等价于方法2的两步操作

### 执行过程示例

以 k = 3, nums = [4, 5, 8, 2] 为例。

初始化过程：

```text
nums = [4, 5, 8, 2]
heapify后：[2, 4, 8, 5]（最小堆）
len(heap) = 4 > k = 3，弹出最小的2
heap = [4, 5, 8]（保留3个最大的）
堆顶heap[0] = 4（第3大的元素）
```

add(3)：

```text
当前heap = [4, 5, 8]
3 < heap[0] = 4，不需要插入
返回 heap[0] = 4
```

add(5)：

```text
当前heap = [4, 5, 8]
5 > heap[0] = 4，替换堆顶
heapreplace(heap, 5) -> 弹出4，插入5
heap = [5, 5, 8]
返回 heap[0] = 5
```

add(10)：

```text
当前heap = [5, 5, 8]
10 > heap[0] = 5，替换堆顶
heapreplace(heap, 10) -> 弹出5，插入10
heap = [5, 8, 10]（堆调整后）
返回 heap[0] = 5
```

add(9)：

```text
当前heap = [5, 8, 10]
9 > heap[0] = 5，替换堆顶
heapreplace(heap, 9) -> 弹出5，插入9
heap = [8, 9, 10]（堆调整后）
返回 heap[0] = 8
```

add(4)：

```text
当前heap = [8, 9, 10]
4 < heap[0] = 8，不需要插入
返回 heap[0] = 8
```

## 常见错误

### 错误1：使用最大堆

```python
# 错误：使用最大堆需要维护所有元素
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = [-x for x in nums]  # 转负数模拟最大堆
        heapq.heapify(self.heap)
    
    def add(self, val):
        heapq.heappush(self.heap, -val)
        # 需要弹出k-1次才能得到第k大
        # 空间O(n)，时间O(k log n)
```

**问题：** 空间复杂度高，时间复杂度也不优。

### 错误2：初始化时不清理多余元素

```python
# 错误：堆的大小可能超过k
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # 忘记弹出多余元素！
    
    def add(self, val):
        heapq.heappush(self.heap, val)
        return heapq.nsmallest(self.k, self.heap)[-1]  # 错误且慢
```

**问题：** 每次add都要O(n log k)，应该维护固定大小的堆。

### 错误3：边界条件处理不当

```python
# 错误：当len(heap) < k时没有特殊处理
def add(self, val):
    if val > self.heap[0]:  # 当heap为空时会报错！
        heapq.heapreplace(self.heap, val)
    return self.heap[0]
```

**问题：** 初始时heap可能不足k个元素，需要先检查。

正确做法：

```python
def add(self, val):
    if len(self.heap) < self.k:
        heapq.heappush(self.heap, val)
    elif val > self.heap[0]:
        heapq.heapreplace(self.heap, val)
    return self.heap[0]
```

### 错误4：混淆heapreplace和heappushpop

```python
# 错误使用heapreplace
heapq.heapreplace(heap, 3)  # 如果heap=[5,8,10]
# 结果：先弹出5，再插入3，heap=[3,8,10]
# 第k大变成了3，错误！

# 应该先判断
if val > heap[0]:
    heapq.heapreplace(heap, val)
```

**原因：** `heapreplace` 无条件替换堆顶，可能让堆变小。

## 相关题目

- [0215. Kth Largest Element in an Array](./215_kth_largest_element_in_an_array.md)
- [0692. Top K Frequent Words](./692_Top_K_Frequent_Words.md)
- [0347. Top K Frequent Elements](./347_top_k_frequent_elements.md)
- [0295. Find Median from Data Stream](./295_find_median_from_data_stream.md)
- [0973. K Closest Points to Origin](./973_k_closest_points_to_origin.md)

