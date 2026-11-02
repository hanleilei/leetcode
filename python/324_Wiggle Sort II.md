# Wiggle Sort II

Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.

Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]

Constraints:

$1 <= nums.length <= 5 * 10^4$
$0 <= nums[i] <= 5000$
It is guaranteed that there will be an answer for the given input nums.

Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?

排序 + 分半 + 倒序交叉填充:

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2
        
        left = nums[:mid]
        right = nums[mid:]
        
        l, r = mid - 1, len(right) - 1
        
        for i in range(n):
            if i % 2 == 0:
                nums[i] = left[l]
                l -= 1
            else:
                nums[i] = right[r]
                r -= 1
```

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums[::2], nums[1::2] = nums[:(len(nums) + 1) // 2][::-1], nums[(len(nums) + 1)//2:][::-1]
```

桶排序：

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 创建计数桶（题目数据范围 0 <= nums[i] <= 5000）
        bucket = [0] * 5001
        for num in nums:
            bucket[num] += 1
        
        length = len(nums)
        
        # 2. 根据数组长度的奇偶性，确定奇偶索引的填充边界
        if length % 2 == 1:   # 奇数长度：偶数位比奇数位多一个
            small = length - 1 # 最后一个偶数索引
            big = length - 2   # 最后一个奇数索引
        else:                 # 偶数长度：奇偶位数量相等
            small = length - 2 # 最后一个偶数索引
            big = length - 1   # 最后一个奇数索引
        
        j = 5000  # 从最大值开始往下找
        
        # 3. 先将桶中较大的数字，从大到小依次填入奇数索引
        for i in range(1, big + 1, 2):
            while bucket[j] == 0:
                j -= 1
            nums[i] = j
            bucket[j] -= 1
        
        # 4. 再将桶中剩余的数字（较小的），接着往下找并填入偶数索引
        for i in range(0, small + 1, 2):
            while bucket[j] == 0:
                j -= 1
            nums[i] = j
            bucket[j] -= 1
```

还是stefan的代码：

```cpp
class Solution {
public:
void wiggleSort(vector<int>& nums) {
    int n = nums.size();
    
    // Step 1: 用 nth_element 找到中位数（平均 O(n)）
    auto midptr = nums.begin() + n / 2;
    nth_element(nums.begin(), midptr, nums.end());
    int mid = *midptr;
    
    // Step 2 & 3: 虚拟索引 + 三向切分
    // 映射函数 A(i) 将逻辑下标 i 映射到物理下标
    #define A(i) nums[(1 + 2 * (i)) % (n | 1)]
    
    int i = 0, j = 0, k = n - 1;
    while (j <= k) {
        if (A(j) > mid) {
            swap(A(i++), A(j++));
        } else if (A(j) < mid) {
            swap(A(j), A(k--));
        } else {
            j++;
        }
    }
}
};
```
