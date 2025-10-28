# Make Array Elements Equal to Zero

[[array]] [[simulation]] [[prefix-sum]]

## Problem Description

You are given an integer array `nums`.

Start by selecting a starting position `curr` such that `nums[curr] == 0`, and choose a movement direction of either left or right.

After that, you repeat the following process:

1. If `curr` is out of the range `[0, n - 1]`, this process ends.
2. If `nums[curr] == 0`, move in the current direction by incrementing `curr` if you are moving right, or decrementing `curr` if you are moving left.
3. Else if `nums[curr] > 0`:
   - Decrement `nums[curr]` by 1.
   - Reverse your movement direction (left becomes right and vice versa).
   - Take a step in your new direction.

A selection of the initial position `curr` and movement direction is considered **valid** if every element in `nums` becomes 0 by the end of the process.

Return the number of possible valid selections.

## Examples

**Example 1:**

```text
Input: nums = [1,0,2,0,3]
Output: 2
Explanation:
The only possible valid selections are:
1. Choose curr = 3, direction = left
2. Choose curr = 3, direction = right
```

**Example 2:**

```text
Input: nums = [2,3,4,0,4,1,0]
Output: 0
Explanation: There are no possible valid selections.
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`
- There is at least one element `i` where `nums[i] == 0`.

## 解法：前缀和差值分析（最优解）

```python
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        """
        转换为小球碰撞问题，使用前缀和分析
        时间复杂度：O(n)，空间复杂度：O(1)
        """
        total_sum = sum(nums)  # 总和
        prefix_sum = 0         # 前缀和
        result = 0
        
        for num in nums:
            if num != 0:
                prefix_sum += num
            else:
                # 当前位置为0，可以作为起始点
                suffix_sum = total_sum - prefix_sum  # 后缀和
                
                if prefix_sum == suffix_sum:
                    # 左右完全平衡，两个方向都可以
                    result += 2
                elif abs(prefix_sum - suffix_sum) == 1:
                    # 左右相差1，只有一个方向可以
                    result += 1
                # 其他情况不满足条件
        
        return result
```

### 算法思路

这道题可以转换为**小球碰撞问题**来理解：

**核心观察**：

1. 只能从值为0的位置开始
2. 小球在移动过程中会"消耗"非零元素，每次碰撞减1并反向
3. 最终所有元素都变为0，等价于小球的"左冲右撞"能够平衡整个数组

**关键洞察**：

- 从位置`i`开始，左边元素总和为`prefix_sum`，右边元素总和为`suffix_sum`
- 如果`prefix_sum == suffix_sum`：两个方向的"消耗量"相等，左右都可以成功
- 如果`abs(prefix_sum - suffix_sum) == 1`：相差1可以通过额外的一次移动补偿
- 如果差值大于1：无法通过有限次移动平衡

### 算法演示

以 `nums = [1,0,2,0,3]` 为例：

```text
位置: 0  1  2  3  4
数值: 1  0  2  0  3
      ↑     ↑     
   不可选  可选   可选

位置1 (nums[1] = 0):
- prefix_sum = 1 (左边：[1])
- suffix_sum = 5 (右边：[2,0,3])
- |1 - 5| = 4 > 1，不满足条件

位置3 (nums[3] = 0):
- prefix_sum = 3 (左边：[1,0,2])
- suffix_sum = 3 (右边：[3])
- 3 == 3，完全平衡，result += 2

总计：2种有效选择
```

### 为什么这个方法有效？

**物理直觉**：

- 小球从0位置出发，会在非零元素处"反弹"并减少元素值
- 左右两边的总"反弹次数"必须平衡，才能让所有元素归零
- 相差1的情况下，多出的那一次可以通过边界处的"出界"来消耗

**数学证明**：

- 小球每次碰撞都会减少数组总和1
- 最终总和必须变为0，所以总碰撞次数等于初始总和
- 左右平衡意味着碰撞分布均匀，能够覆盖所有元素

**复杂度分析**：

- 时间复杂度：O(n) - 遍历数组一次
- 空间复杂度：O(1) - 只使用常数额外空间

## 边界情况处理

1. **全为0的数组**：每个位置都满足条件，结果为`2 * count_of_zeros`
2. **只有一个0**：根据左右和的关系判断
3. **极端不平衡**：左右和相差很大，返回0

## 关键要点

1. **问题转换**：将复杂的模拟过程转换为数学问题
2. **前缀和技巧**：利用前缀和快速计算左右两边的总和
3. **平衡条件**：理解为什么相等或相差1是成功的充要条件
4. **物理直觉**：小球碰撞模型帮助理解问题本质

## 常见错误

1. **暴力模拟**：试图完整模拟整个过程，导致超时
2. **条件理解错误**：不理解为什么相差1也可以成功
3. **边界遗漏**：没有正确处理数组边界的特殊情况
4. **计数错误**：忘记完全平衡的情况有两个方向

## 算法扩展

1. **如果允许从任意位置开始？** - 需要考虑更复杂的状态转移
2. **如果数组很大怎么办？** - 当前O(n)算法已经是最优的
3. **如果要求输出具体的路径？** - 需要额外的回溯或构造算法

## 相关题目

- [1658. Minimum Operations to Reduce X to Zero](1658_minimum_operations_to_reduce_x_to_zero.md) - 将x减到0的最小操作数
- [724. Find Pivot Index](724_find_pivot_index.md) - 寻找数组的中心索引
- [1991. Find the Middle Index in Array](1991_find_the_middle_index_in_array.md) - 找到数组的中间位置

这道题展示了如何将复杂的模拟问题转换为优雅的数学分析，是前缀和和问题建模的绝佳例子。
