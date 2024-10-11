# Destination City

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

## Example 1

```text
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
```

## Example 2

```text
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
```

## Example 3

```text
Input: paths = [["A","Z"]]
Output: "Z"
```

## Constraints

```text
1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.
```

```python
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, end = set(), set()
        for p in paths:
            start.add(p[0])
            end.add(p[1])
        res = end - start
        return res.pop()
```

额外维护一个哈希集合 setB，用来存储那些「可能是答案」的 cityBi：

- 如果 cityAi 在 setB 中，那么 cityAi 必然不是答案，从 setB 中移除。代码实现时，可以简化为直接从 setB 中移除 cityAi ，无需检查其是否存在。
- 如果 cityBi 不在 setA 中，那么 cityBi 有可能是答案，加到 setB 中。
- 最后 setB 必然恰好剩下一个元素（题目保证），返回这个元素。

```python
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, end = set(), set()
        for a, b in paths:
            end.discard(a)
            if b not in start:
                end.add(b)
            start.add(a)
        return end.pop()
```
