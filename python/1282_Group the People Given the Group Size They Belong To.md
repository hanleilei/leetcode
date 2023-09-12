# Group the People Given the Group Size They Belong To

There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

## Example 1

```text
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
```

## Example 2

```text
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
```

## Constraints

```text
groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
```

还是按照题目的本意直接实现了：

```python
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = list()
        d = defaultdict(list)

        for i, v in enumerate(groupSizes):
            d[v].append(i)

        for key in sorted(d.keys()):
            j = 0
            while j + key <= len(d[key]):
                res.append(d[key][j: j + key])
                j += key
        return res
```

来一个lee215的方案，思路基本一致：

```python
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        return [l[i:i + s]for s, l in count.items() for i in range(0, len(l), s)]
```

是不是觉得最后一行代码有点难理解？可以写成这样：

```python
res = []
for s, l in count.items():
    for i in range(0, len(l), s):
        res.append(l[i:i + s])
return res
```

