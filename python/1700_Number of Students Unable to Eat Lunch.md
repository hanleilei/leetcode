# Number of Students Unable to Eat Lunch

[[array]] [[simulation]] [[queue]] [[counting]]

## Problem Description

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a **stack**. At each step:

- If the student at the front of the queue **prefers** the sandwich on the top of the stack, they will take it and leave the queue.
- Otherwise, they will **leave it** and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `i​​​​​​th` sandwich in the stack (`i = 0` is the top of the stack) and `students[j]` is the preference of the `j​​​​​​th` student in the initial queue (`j = 0` is the front of the queue). Return the number of students that are unable to eat.

## Examples

**Example 1:**

```text
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
```

**Example 2:**

```text
Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
```

## Constraints

- `1 <= students.length, sandwiches.length <= 100`
- `students.length == sandwiches.length`
- `sandwiches[i]` is `0` or `1`.
- `students[i]` is `0` or `1`.

## 解法一：计数法（最优解）

```python
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        通过计数学生偏好，避免模拟整个过程
        时间复杂度：O(n)，空间复杂度：O(1)
        """
        # 统计学生偏好
        count = Counter(students)

        # 按顺序检查三明治
        for i, sandwich in enumerate(sandwiches):
            if count[sandwich] == 0:
                # 没有学生喜欢当前三明治，剩余学生都无法进食
                return len(sandwiches) - i
            count[sandwich] -= 1

        # 所有学生都能进食
        return 0
```

### 算法思路

**核心洞察**：我们不需要模拟整个排队过程，只需要关注学生偏好的数量。

**关键观察**：

1. 学生在队列中的顺序可以任意调整（通过移到队尾）
2. 三明治必须按栈的顺序取出（从顶部开始）
3. 当某种三明治没有对应偏好的学生时，游戏结束

**算法步骤**：

1. 统计每种偏好的学生数量
2. 按三明治栈的顺序检查每个三明治
3. 如果当前三明治有对应偏好的学生，消耗一个学生
4. 如果没有，返回剩余三明治数量（即无法进食的学生数）

### 算法演示

以 `students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]` 为例：

```text
初始统计: count = {0: 2, 1: 4}

检查三明治栈:
i=0, sandwich=1: count[1]=4>0, count={0:2, 1:3}
i=1, sandwich=0: count[0]=2>0, count={0:1, 1:3}  
i=2, sandwich=0: count[0]=1>0, count={0:0, 1:3}
i=3, sandwich=0: count[0]=0, 没有学生喜欢0类型三明治

剩余三明治数量: 6-3=3
返回: 3
```

**复杂度分析**：

- 时间复杂度：O(n) - 遍历两个数组各一次
- 空间复杂度：O(1) - 只需要常数额外空间（计数器最多2个元素）

## 解法二：模拟过程

```python
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        直接模拟排队和取餐的过程
        时间复杂度：O(n²)，空间复杂度：O(n)
        """
        from collections import deque

        student_queue = deque(students)
        sandwich_stack = deque(sandwiches)

        # 记录连续多少个学生拒绝了顶部三明治
        consecutive_rejections = 0

        while student_queue and sandwich_stack:
            current_student = student_queue[0]
            top_sandwich = sandwich_stack[0]

            if current_student == top_sandwich:
                # 学生喜欢顶部三明治，取走并离开
                student_queue.popleft()
                sandwich_stack.popleft()
                consecutive_rejections = 0
            else:
                # 学生不喜欢，移到队尾
                student_queue.append(student_queue.popleft())
                consecutive_rejections += 1

                # 如果所有学生都拒绝了当前三明治，结束
                if consecutive_rejections == len(student_queue):
                    break

        return len(student_queue)
```

### 核心思想

**直接模拟**：按照题目描述的规则逐步执行。

**终止条件**：当所有学生都拒绝了当前顶部三明治时，游戏结束。

**复杂度分析**：

- 时间复杂度：O(n²) - 最坏情况下每个学生可能遍历整个队列
- 空间复杂度：O(n) - 使用了双端队列存储

## 解法三：简化计数法

```python
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        更简洁的计数实现
        时间复杂度：O(n)，空间复杂度：O(1)
        """
        # 直接统计两种偏好的数量
        count_0 = students.count(0)
        count_1 = students.count(1)

        for sandwich in sandwiches:
            if sandwich == 0:
                if count_0 > 0:
                    count_0 -= 1
                else:
                    return count_0 + count_1
            else:  # sandwich == 1
                if count_1 > 0:
                    count_1 -= 1
                else:
                    return count_0 + count_1

        return 0
```

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 计数法 | O(n) | O(1) | 最优解，避免模拟 |
| 模拟过程 | O(n²) | O(n) | 直观理解，但效率低 |
| 简化计数 | O(n) | O(1) | 代码更简洁 |

## 边界情况处理

1. **所有学生都能进食**：返回0
2. **所有学生都无法进食**：返回学生总数
3. **单个学生**：检查偏好是否匹配
4. **偏好不均衡**：一种偏好的学生很多，另一种很少

## 关键要点

1. **问题抽象**：将复杂的模拟过程转换为简单的计数问题
2. **顺序重要性**：三明治的顺序是固定的，学生的顺序可以调整
3. **终止条件**：当某种三明治没有对应偏好学生时游戏结束
4. **效率优化**：避免不必要的模拟，直接计算结果

## 常见错误

1. **过度模拟**：不必要地模拟整个排队过程
2. **终止条件错误**：没有正确判断游戏结束的条件
3. **计数错误**：没有正确维护学生偏好的计数
4. **边界遗漏**：没有处理特殊情况

## 算法扩展

1. **多种三明治类型**：如果有超过2种三明治？
2. **学生偏好变化**：如果学生偏好会动态改变？
3. **优先级队列**：如果某些学生有优先权？

## 相关题目

- [622. Design Circular Queue](622_design_circular_queue.md) - 设计循环队列
- [933. Number of Recent Calls](933_number_of_recent_calls.md) - 最近的请求次数
- [1046. Last Stone Weight](1046_last_stone_weight.md) - 最后一块石头的重量

这道题展示了如何通过数学思维将复杂的模拟问题简化为高效的计数问题。
