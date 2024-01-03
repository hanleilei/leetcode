# Minimum Time to Make Rope Colorful

[[dp]]

Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

## Example 1

```text
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.
```

## Example 2

```text
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
```

## Example 3

```text
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
```

## Constraints

```text
n == colors.length == neededTime.length
1 <= n <= 105
1 <= neededTime[i] <= 104
colors contains only lowercase English letters.
```

参考一下lee215的方法：

## Intuition

For a group of continuous same characters,
we need to delete all the group but leave only one character.

## Explanation

For each group of continuous same characters,
we need cost = sum_cost(group) - max_cost(group)

## Complexity

Time O(N)
Space O(1)

```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res, most_cost = 0, 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                most_cost = 0
            res += min(most_cost, neededTime[i])
            most_cost = max(most_cost, neededTime[i])
        return res
```

来一个速度快的：

```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0 
        index = 0
        i = 1
        while i < len(colors):
            if colors[i] == colors[index]:
                if neededTime[i] >= neededTime[index]:
                    res += neededTime[index]
                    index = i
                else:
                    res += neededTime[i]
            else:
                index = i
            i += 1
        return res
```
