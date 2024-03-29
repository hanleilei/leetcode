# assign cookies

[[greedy]]

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

## Note

You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

## Example 1

```text
Input: [1,2,3], [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
```

## Example 2

```text
Input: [1,2], [1,2,3]

Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.
```

standard greedy solution:

先对g, s两个数组进行排序

贪心算法
贪心思想1 优先满足需求因子较小的孩子。因为如果较小需求的孩子无法被满足，则之后的较大的需求更不可能能被满足了。
贪心思想2 尽量用较小的糖果去优先满足孩子。

```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i = j = res = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
            j += 1
        return res
```

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = 0
        for cookie in s:
            if cookie >= g[n]:
                n += 1
            if n == len(g):
                return n
        return n
```
