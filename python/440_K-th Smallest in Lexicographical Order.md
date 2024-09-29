# K-th Smallest in Lexicographical Order

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1

Constraints:

1 <= k <= n <= 109

```text
直接构造法

初始令答案ans = 1，当k值＞0时执行循环：

计算ans与ans + 1之间的数字个数gap

若gap <= k：则令ans = ans + 1，k = k - gap

否则令ans = ans * 10，k = k - 1

当n, p, q = 35769, 3, 4时，findGap函数执行过程如下：
```

```text
p        q         gap
3        4         1
30       40        11
300      400       111
3000     4000      1111
30000    40000     6881
```

Actually this is a denary tree (each node has 10 children). Find the kth element is to do a k steps preorder traverse of the tree.

Initially, image you are at node 1 (variable: curr),
the goal is move (k - 1) steps to the target node x. (substract steps from k after moving)
when k is down to 0, curr will be finally at node x, there you get the result.

we don't really need to do a exact k steps preorder traverse of the denary tree, the idea is to calculate the steps between curr and curr + 1 (neighbor nodes in same level), in order to skip some unnecessary moves.

## Main function

Firstly, calculate how many steps curr need to move to curr + 1.

if the steps <= k, we know we can move to curr + 1, and narrow down k to k - steps.

else if the steps > k, that means the curr + 1 is actually behind the target node x in the preorder path, we can't jump to curr + 1. What we have to do is to move forward only 1 step (curr * 10 is always next preorder node) and repeat the iteration.

## calSteps function

how to calculate the steps between curr and curr + 1?
Here we come up a idea to calculate by level.
Let n1 = curr, n2 = curr + 1.
n2 is always the next right node beside n1's right most node (who shares the same ancestor "curr")
(refer to the pic, 2 is right next to 1, 20 is right next to 19, 200 is right next to 199).

so, if n2 <= n, what means n1's right most node exists, we can simply add the number of nodes from n1 to n2 to steps.

else if n2 > n, what means n (the biggest node) is on the path between n1 to n2, add (n + 1 - n1) to steps.

organize this flow to "steps += Math.min(n + 1, n2) - n1; n1 *= 10; n2 *= 10;"

```python
class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        k -= 1

        while k > 0:
            step = self._count_steps(n, curr, curr + 1)
            # If the steps are less than or equal to k, we skip this prefix's subtree
            if step <= k:
                # Move to the next prefix and decrease k by the number of steps we skip
                curr += 1
                k -= step
            else:
                # Move to the next level of the tree and decrement k by 1
                curr *= 10
                k -= 1

        return curr

    # To count how many numbers exist between prefix1 and prefix2
    def _count_steps(self, n, prefix1, prefix2):
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps
```

简化一下：

```python
class Solution(object):
    def findKthNumber(self, n, k):
        cur = 1
        k = k - 1
        while k > 0:
            steps = self.calSteps(n, cur)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur

    def calSteps(self, n, cur):
        steps = 0
        n1, n2 = cur, cur + 1
        while n1 <= n:
            steps += min(n + 1, n2) - n1
            n1 *= 10
            n2 *= 10
        return steps
```
