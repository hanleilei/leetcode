# candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

* Each child must have at least one candy.
* Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

## Example 1

```text
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
```

## Example 2

```text
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
```

Constraints:

`n == ratings.length`
`1 <= n <= 2 * 10**4`
`0 <= ratings[i] <= 2 * 10**4`

## 解法一：两次遍历（简单易懂）

核心思想是使用两次遍历的贪心算法。

Greedy，从左到右，然后从右到左。

```python
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = len(ratings) * [1]
        for i in range(1, len(ratings)):  # from left to right
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in range(len(ratings)-1, 0, -1):  # from right to left
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1], res[i]+1)
        return sum(res)
```

## 解法二：一次遍历（推荐）

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = n = len(ratings)  # 先给每人分一个
        i = 0
        while i < n:
            start = i - 1 if i > 0 and ratings[i - 1] < ratings[i] else i

            # 找严格递增段
            while i + 1 < n and ratings[i] < ratings[i + 1]:
                i += 1
            top = i  # 峰顶

            # 找严格递减段
            while i + 1 < n and ratings[i] > ratings[i + 1]:
                i += 1

            inc = top - start  # start 到 top 严格递增
            dec = i - top      # top 到 i 严格递减
            ans += (inc * (inc - 1) + dec * (dec - 1)) // 2 + max(inc, dec)
            i += 1
        return ans
```
