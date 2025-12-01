# Remove Duplicates from Sorted Array II

[[array]] [[2points]]

## Problem Description

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates **in-place** such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` *after placing the final result in the first* `k` *slots of* `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array in-place** with O(1) extra memory.

## Examples

**Example 1:**

```text
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**

```text
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in **non-decreasing** order.

## 解法一：双指针法（最优解）

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
```

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = 0;
        for (int i = 0; i < nums.size(); i++){
            if (len < 2 || nums[len-2] != nums[i]){
                nums[len++] = nums[i];
            }
        }
        return len;
    }
};
```

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if res < 2 or nums[res - 2] != nums[i]:
                nums[res]= nums[i]
                res += 1
        return res
```

**核心思想：**

- 使用双指针技术，`i`表示当前要放置元素的位置
- 关键判断条件：`i < 2 or n > nums[i-2]`
  - `i < 2`：前两个位置直接放置
  - `n > nums[i-2]`：当前元素大于已放置的倒数第二个元素，说明不会造成连续三个相同

**时间复杂度：** O(n)
**空间复杂度：** O(1)

## 解法二：双指针变体

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2: 
            return len(nums)

        end = 2
        for n in nums[2:]:
            if n > nums[end-2]:
                nums[end] = n
                end += 1

        return end
```

这是解法一的变体，显式处理边界情况，从第三个元素开始遍历。逻辑相同但代码更清晰。

## 算法原理

这类题目的核心是"允许最多k个重复"的通用模板：

```python
def removeDuplicates(nums, k):
    i = 0
    for n in nums:
        if i < k or n > nums[i-k]:
            nums[i] = n
            i += 1
    return i
```

对于本题k=2，所以条件变成`i < 2 or n > nums[i-2]`。

## 相关题目

- [26. Remove Duplicates from Sorted Array](026_remove_duplicate_from_sorted_array.md) - 删除排序数组中的重复项
- [27. Remove Element](027_remove_element.md) - 移除元素
