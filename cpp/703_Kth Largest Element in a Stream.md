# 703. Kth Largest Element in a Stream

[[heap]]

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

核心思想：维护一个大小为k的最小堆，堆顶就是第k大的元素。

```java
#include<vector>
#include<queue>

using namespace std;

class KthLargest {
    priority_queue<int, vector<int>, greater<int> > heap;
    int size;

public:
    KthLargest(int k, vector<int> &nums) {
        size = k;
        for (int &num: nums) {
            if (heap.size() < size) {
                heap.push(num);
            } else {
                if (num > heap.top()) {
                    heap.pop();
                    heap.push(num);
                }
            }
        }

    }

    int add(int val) {
        if (heap.size() < size) {
            heap.push(val);
        } else {
            if (val > heap.top()) {
                heap.pop();
                heap.push(val);
            }
        }
        return heap.top();
    }
};
```

## 相关题目

- [0215. Kth Largest Element in an Array](./215_kth_largest_element_in_an_array.md)
- [0692. Top K Frequent Words](./692_Top_K_Frequent_Words.md)
- [0347. Top K Frequent Elements](./347_top_k_frequent_elements.md)
- [0295. Find Median from Data Stream](./295_find_median_from_data_stream.md)
- [0973. K Closest Points to Origin](./973_k_closest_points_to_origin.md)

