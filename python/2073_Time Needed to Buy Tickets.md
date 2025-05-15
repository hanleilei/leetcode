# Time Needed to Buy Tickets

There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

## Example 1

```text
Input: tickets = [2,3,2], k = 2
Output: 6
Explanation: 
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
```

## Example 2

```text
Input: tickets = [5,1,1,1], k = 0
Output: 8
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
- In the next 4 passes, only the person in position 0 is buying tickets.
The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.
```

## Constraints

```text
n == tickets.length
1 <= n <= 100
1 <= tickets[i] <= 100
0 <= k < n
```

反正把整个问题想象成一个两个长方形拼接。后一个比前一个高度少了1。

```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i in range(len(tickets)):
            res += min(tickets[i], tickets[k])
            if i > k and tickets[i] >= tickets[k]:
                res -= 1
        return res
```

或者：

```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                res += min(tickets[i], tickets[k] - 1)
        return res
```

感觉还是前面的更好。

写成单行：

```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(v, tickets[k] if i <= k else tickets[k] - 1) for i, v in enumerate(tickets))
```

labuladong 解法：

```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(range(len(tickets)))
        res = 0
        while queue:
            # 队头的人买票
            front = queue.popleft()
            res += 1
            tickets[front] -= 1
            
            if front == k and tickets[front] == 0:
                # 如果是 k 号买完票了，返回总时间
                return res

            if tickets[front] == 0:
                continue

            # 如果还要继续买票，重新排到队尾
            queue.append(front)
        return time
```

能工作，但是低效。
