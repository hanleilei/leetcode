# Time Needed to Buy Tickets

[[queue]] [[simulation]] [[math]]

## Problem Description

There are `n` people in a line queuing to buy tickets, where the `0th` person is at the **front** of the line and the `(n - 1)th` person is at the **back** of the line.

You are given a **0-indexed** integer array `tickets` of length `n` where the number of tickets that the `ith` person would like to buy is `tickets[i]`.

Each person takes **exactly 1 second** to buy a ticket. A person can only buy **1 ticket at a time** and has to go back to the **end of the line** (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will **leave the line**.

Return _the time taken for the person at position_ `k` _(0-indexed) to finish buying tickets_.

## Examples

**Example 1:**

```text
Input: tickets = [2,3,2], k = 2
Output: 6
Explanation: 
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
```

**Example 2:**

```text
Input: tickets = [5,1,1,1], k = 0
Output: 8
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
- In the next 4 passes, only the person in position 0 is buying tickets.
The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.
```

## Constraints

- `n == tickets.length`
- `1 <= n <= 100`
- `1 <= tickets[i] <= 100`
- `0 <= k < n`

## 解法一：数学优化（推荐）

```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        数学解法：分析每个人对总时间的贡献
        时间复杂度：O(n)，空间复杂度：O(1)
        """
        total_time = 0
        target_tickets = tickets[k]  # 目标人员需要的票数
        
        for i, ticket_count in enumerate(tickets):
            if i <= k:
                # 在k位置之前（包括k）的人员
                # 他们最多能买到 target_tickets 张票
                total_time += min(ticket_count, target_tickets)
            else:
                # 在k位置之后的人员
                # 他们最多能买到 target_tickets - 1 张票
                # 因为当k买完最后一张票时，轮次结束
                total_time += min(ticket_count, target_tickets - 1)
        
        return total_time
```

**复杂度分析**：

- 时间复杂度：O(n) - 遍历一次数组
- 空间复杂度：O(1) - 只使用常数额外空间

## 解法二：数学优化（另一种写法）

```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        使用条件判断的写法
        逻辑更清晰的版本
        """
        total_time = 0
        target_tickets = tickets[k]
        
        for i in range(len(tickets)):
            # 计算每个位置对总时间的贡献
            contribution = min(tickets[i], target_tickets)
            
            # 如果在k之后且票数充足，需要减去1
            # 因为k买完最后一张票时，这些人还没机会买最后一轮
            if i > k and tickets[i] >= target_tickets:
                contribution -= 1
            
            total_time += contribution
        
        return total_time
```

## 解法三：一行代码（简洁版本）

```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        使用生成器表达式的一行解法
        """
        return sum(
            min(tickets[i], tickets[k] if i <= k else tickets[k] - 1)
            for i in range(len(tickets))
        )
```

## 解法四：队列模拟（直观但低效）

```python
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        模拟买票过程
        时间复杂度：O(sum(tickets))，空间复杂度：O(n)
        """
        queue = deque(range(len(tickets)))  # 队列存储人员索引
        time = 0
        
        while queue:
            # 队头的人买票
            current_person = queue.popleft()
            time += 1
            tickets[current_person] -= 1
            
            # 如果是目标人员且买完了所有票
            if current_person == k and tickets[current_person] == 0:
                return time
            
            # 如果还需要买票，重新排到队尾
            if tickets[current_person] > 0:
                queue.append(current_person)
        
        return time
```

**复杂度分析**：

- 时间复杂度：O(sum(tickets)) - 需要模拟所有购票过程
- 空间复杂度：O(n) - 队列存储人员索引

## 算法详解

### 数学解法核心思路

1. **问题转化**：
   - 不需要真实模拟买票过程
   - 直接计算每个人对总时间的贡献

2. **关键观察**：
   - k位置的人需要买 `tickets[k]` 张票
   - 在k之前的人最多参与 `tickets[k]` 轮购票
   - 在k之后的人最多参与 `tickets[k] - 1` 轮购票

3. **贡献计算**：
   - 位置i的人的贡献 = min(tickets[i], 可参与的轮次)

### 算法可视化

以 `tickets = [2,3,2], k = 2` 为例：

```text
目标：位置2的人需要买2张票

分析每个人的贡献：
- 位置0: min(2, 2) = 2 (可参与2轮，自己需要2张)
- 位置1: min(3, 2) = 2 (可参与2轮，自己需要3张但只能买2张)
- 位置2: min(2, 2) = 2 (可参与2轮，自己需要2张，正好买完)

总时间 = 2 + 2 + 2 = 6秒

详细过程：
第1轮: [2,3,2] -> [1,2,1] (3秒)
第2轮: [1,2,1] -> [0,1,0] (3秒)
位置2的人买完，总共6秒
```

以 `tickets = [5,1,1,1], k = 0` 为例：

```text
目标：位置0的人需要买5张票

分析每个人的贡献：
- 位置0: min(5, 5) = 5 (可参与5轮，需要5张)
- 位置1: min(1, 4) = 1 (只能参与4轮，需要1张)
- 位置2: min(1, 4) = 1 (只能参与4轮，需要1张)  
- 位置3: min(1, 4) = 1 (只能参与4轮，需要1张)

总时间 = 5 + 1 + 1 + 1 = 8秒
```

### 为什么k之后的人只能参与 tickets[k]-1 轮？

- 当k位置的人买完最后一张票时，这一轮就结束了
- k之后的人在这一轮中还没有机会买票
- 所以他们比k之前的人少参与一轮

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 数学优化 | O(n) | O(1) | 最优解，推荐 |
| 一行代码 | O(n) | O(1) | 简洁但可读性较差 |
| 队列模拟 | O(sum(tickets)) | O(n) | 直观但效率低 |

## 关键要点

1. **问题转化**：从模拟过程转为数学计算
2. **位置影响**：k之前和之后的人参与轮次不同
3. **贡献分析**：每个人的时间贡献独立计算
4. **边界理解**：k买完最后一张票时，轮次立即结束

## 相关题目

- [933. Number of Recent Calls](933_number_of_recent_calls.md) - 最近的请求次数
- [225. Implement Stack using Queues](225_implement_stack_using_queue.md) - 用队列实现栈
- [346. Moving Average from Data Stream](346_moving_average_data_stream.md) - 数据流中的移动平均值

这道题很好地展示了如何将复杂的模拟问题转化为简单的数学计算，是优化思维的好例子。
