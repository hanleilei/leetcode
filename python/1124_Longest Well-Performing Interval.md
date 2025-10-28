# Longest Well-Performing Interval

[[array]] [[hashtable]] [[stack]] [[prefix-sum]]

## Problem Description

We are given `hours`, a list of the number of hours worked per day for a given employee.

A day is considered to be a **tiring day** if and only if the number of hours worked is (strictly) greater than 8.

A **well-performing interval** is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return *the length of the longest well-performing interval*.

## Examples

**Example 1:**

```text
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
```

**Example 2:**

```text
Input: hours = [6,6,6]
Output: 0
```

## Constraints

- `1 <= hours.length <= 10^4`
- `0 <= hours[i] <= 16`

## 解法一：单调栈+前缀和（最优解）

```python
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        """
        使用单调栈和前缀和解决问题
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        n = len(hours)
        
        # 计算前缀和：>8的天数计为1，<=8的天数计为-1
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + (1 if hours[i - 1] > 8 else -1)
        
        # 构建单调递减栈，存储索引
        stack = [0]  # 初始化包含索引0
        for i in range(1, n + 1):
            if prefix_sum[i] < prefix_sum[stack[-1]]:
                stack.append(i)
        
        # 从右向左遍历，寻找最长区间
        max_length = 0
        for j in range(n, 0, -1):
            while stack and prefix_sum[j] > prefix_sum[stack[-1]]:
                max_length = max(max_length, j - stack.pop())
        
        return max_length
```

### 算法思路

**核心思想**：将问题转换为"寻找最长的子数组，使其元素和大于0"。

**转换步骤**：

1. **数组转换**：工作时间>8的天数记为+1，<=8的天数记为-1
2. **前缀和计算**：`prefix_sum[i]`表示前i天的累计分数
3. **区间判断**：区间`[i+1, j]`是well-performing当且仅当`prefix_sum[j] > prefix_sum[i]`

**算法关键**：

- **单调栈**：维护前缀和严格递减的索引序列
- **从右遍历**：确保找到的是最长的满足条件的区间

### 算法演示

以 `hours = [9,9,6,0,6,6,9]` 为例：

```text
原数组:    [9, 9, 6, 0, 6, 6, 9]
转换后:    [1, 1,-1,-1,-1,-1, 1]
前缀和:    [0, 1, 2, 1, 0,-1,-2,-1]
索引:      [0, 1, 2, 3, 4, 5, 6, 7]

构建单调栈:
- i=0: stack=[0], prefix_sum[0]=0
- i=1: prefix_sum[1]=1 > 0, 不加入
- i=2: prefix_sum[2]=2 > 0, 不加入  
- i=3: prefix_sum[3]=1 > 0, 不加入
- i=4: prefix_sum[4]=0 = 0, 不加入
- i=5: prefix_sum[5]=-1 < 0, 加入stack=[0,5]
- i=6: prefix_sum[6]=-2 < -1, 加入stack=[0,5,6]
- i=7: prefix_sum[7]=-1 > -2, 不加入

最终stack=[0,5,6]

从右向左遍历:
- j=7: prefix_sum[7]=-1 > prefix_sum[6]=-2, 长度=7-6=1
- j=7: prefix_sum[7]=-1 < prefix_sum[5]=-1, 停止
- j=6: 已处理
- j=5: 已处理  
- j=4: prefix_sum[4]=0 > prefix_sum[5]=-1 (但5已出栈)
- j=3: prefix_sum[3]=1 > prefix_sum[0]=0, 长度=3-0=3
- j=2: prefix_sum[2]=2 > prefix_sum[0]=0 (但0已出栈)

最大长度=3
```

**复杂度分析**：

- 时间复杂度：O(n) - 每个元素最多入栈出栈一次
- 空间复杂度：O(n) - 前缀和数组和栈的空间

## 解法二：哈希表优化

```python
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        """
        使用哈希表记录前缀和首次出现位置
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        prefix_sum = 0
        max_length = 0
        first_occurrence = {}  # 记录前缀和首次出现的位置
        
        for i, hour in enumerate(hours):
            # 更新前缀和
            prefix_sum += 1 if hour > 8 else -1
            
            if prefix_sum > 0:
                # 从开始到当前位置就是well-performing
                max_length = i + 1
            else:
                # 寻找prefix_sum-1首次出现的位置
                if prefix_sum - 1 in first_occurrence:
                    max_length = max(max_length, i - first_occurrence[prefix_sum - 1])
                
                # 记录当前前缀和首次出现的位置
                if prefix_sum not in first_occurrence:
                    first_occurrence[prefix_sum] = i
        
        return max_length
```

### 核心思想

**关键观察**：如果要使区间`[i+1, j]`为well-performing，需要`prefix_sum[j] > prefix_sum[i]`。

对于当前位置`j`，如果`prefix_sum[j] <= 0`，我们需要找到最早的位置`i`使得`prefix_sum[i] = prefix_sum[j] - 1`。

**复杂度分析**：

- 时间复杂度：O(n) - 一次遍历
- 空间复杂度：O(n) - 哈希表存储

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 单调栈+前缀和 | O(n) | O(n) | 最优解，技巧性强 |
| 哈希表优化 | O(n) | O(n) | 思路清晰，代码简洁 |


## 边界情况处理

1. **全是非疲劳天**：返回0
2. **全是疲劳天**：返回数组长度
3. **单个元素**：根据是否>8决定返回1或0
4. **交替模式**：正确处理+1,-1交替的情况

## 关键要点

1. **问题转换**：将well-performing问题转换为子数组和大于0的问题
2. **单调栈应用**：维护候选区间的左端点
3. **前缀和技巧**：快速计算区间内的累计分数
4. **贪心思想**：从右向左遍历确保找到最长区间

## 常见错误

1. **转换错误**：没有正确理解>8为+1，<=8为-1的转换
2. **边界混淆**：前缀和索引与原数组索引的对应关系
3. **单调栈理解**：不理解为什么要维护递减栈
4. **遍历方向**：没有理解为什么要从右向左遍历

## 算法扩展

1. **变化阈值**：如果判断标准不是8而是其他值？
2. **多种状态**：如果有三种状态（疲劳、正常、轻松）？
3. **在线算法**：如果数据是流式输入的？

## 相关题目

- [53. Maximum Subarray](053_maximum_subarray.md) - 最大子数组和
- [525. Contiguous Array](525_contiguous_array.md) - 连续数组
- [560. Subarray Sum Equals K](560_subarray_sum_equals_k.md) - 和为K的子数组

这道题巧妙地将计数问题转换为前缀和问题，展示了单调栈在优化区间查询中的强大作用。

单调栈写法的变种：

```python
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        # 转换数组：>8为1，否则为-1
        score = [1 if h > 8 else -1 for h in hours]
        # 计算前缀和
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + score[i - 1]
        
        # 构建单调递减栈
        stack = []
        for i in range(n + 1):
            if not stack or prefix[i] < prefix[stack[-1]]:
                stack.append(i)
        
        # 从右向左遍历
        res = 0
        for j in range(n, -1, -1):
            while stack and prefix[j] > prefix[stack[-1]]:
                res = max(res, j - stack[-1])
                stack.pop()
        return res
```

合并一下上面的三个循环：

```python
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        pos = [0] * (len(hours) + 2)  # 记录前缀和首次出现的位置
        ans = s = 0
        for i, h in enumerate(hours, 1):
            s -= 1 if h > 8 else -1  # 取反，改为减法
            if s < 0:
                ans = i
            else:
                if pos[s + 1]:  # 原本是 s-1，取反改为 s+1
                    ans = max(ans, i - pos[s + 1])  # 这里手写 if 会更快
                if pos[s] == 0:
                    pos[s] = i
        return ans
```
