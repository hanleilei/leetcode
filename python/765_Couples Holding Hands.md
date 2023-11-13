# Couples Holding Hands

[[graph]] [[bfs]] [[dfs]] [[unionfind]] [[greedy]]

There are n couples sitting in 2n seats arranged in a row and want to hold hands.

The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).

Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

## Example 1

```text
Input: row = [0,2,1,3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
```

## Example 2

```text
Input: row = [3,2,0,1]
Output: 0
Explanation: All couples are already seated side by side.
``` 

## Constraints

- 2n == row.length
- 2 <= n <= 30
- n is even.
- 0 <= row[i] < 2n
- All the elements of row are unique.

```python
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        d, swap = {x:i for i,x in enumerate(row)}, 0

        for i in range(0, len(row), 2):
            partner=row[i]+1 if row[i]%2==0 else row[i]-1
            j=d[partner]
            if j-i!=1:
                row[i+1], row[j]=row[j], row[i+1]
                d[row[j]]=j
                swap+=1
        return swap
```

或者：

```python
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        swaps = 0
        pos = {x:i for i,x in enumerate(row)}
        
        for i in range(len(row)):
            x = row[i]
            y = x+1 if x%2 == 0 else x-1
            j = pos[y]
            
            # check if we need swap
            if abs(i-j) > 1:
                row[i+1], row[j] = row[j], row[i+1]
                pos[row[i+1]] = i+1
                pos[row[j]] = j
                swaps += 1
                
        return swaps
```

union find:

```python
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        parent = [_ for _ in range(len(row))] # parent keeps the component number, have no relationship with the group!

        def find(group):
            if parent[group]==group:
                return group
            parent[group] = find(parent[group]) # path compression
            return parent[group]

        def union(group1, group2):
            c1, c2 = find(group1), find(group2)
            if c1 == c2:
                return

            parent[c1] = c2


        res = 0
        for group in range(len(row)//2):
            person1 = row[2*group]
            person2 = row[2*group+1]

            person1_group = person1//2
            person2_group = person2//2
            if person1_group != person2_group:
                if find(person1_group) != find(person2_group):
                    res += 1
                    union(person1_group, person2_group)

        return res
```


```python
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        loc = {x: i for (i, x) in enumerate(row)}
        ans = 0
        for i in range(0, len(row), 2):
            p = ((row[i] - 1) if (row[i] & 1) else (row[i] + 1))
            if (row[(i + 1)] != p):
                ans += 1
                ii = loc[p]
                (loc[row[(i + 1)]], loc[row[ii]]) = (loc[row[ii]], loc[row[(i + 1)]])
                (row[(i + 1)], row[ii]) = (row[ii], row[(i + 1)])
        return ans
```
