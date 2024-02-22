# Find the Town Judge

[[graph]]

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n


1.如果存在法官，那么所有人都会信任法官，在结合条件1，可以得出信任法官的人数为n-1。
2.如果不存在法官，那么也可能存在某些人被所有人信任，这个人的信任人数也为n-1，但是他也会信任别人。
3.可以以此作为区分other和juage的条件，假设每个人都有信任值，那么定义一个数组长度为n，用来存放n个人的信任值:
1)如果一个人信任了别人，那么将这个人的信任值-1
2）如果一个人被别人信任，那么这个人的信任值＋1

当一个人被所有人信任，并且他没有信任其它人时，这个人的信任值就是n- 1，那么此人就是法官。
当一个人被所有人信任，但是他也信任了其他人时，这个人的信任值<n - 1。
其它情况下，每个人的信任值都会小于n -1。

![1](https://pic.leetcode-cn.com/1632973922-cIzHAa-image.png)
![2](https://pic.leetcode-cn.com/1632973922-cIzHAa-image.png)

```java
class Solution {
    public int findJudge(int n, int[][] trust) {

        // 定义数组用于存放每个人的信任值
        int[] trustValues = new int[n + 1]; // 人员编号从1开始，这里+1防止后续计算麻烦
        
        // 遍历trust数组计算每个人的信任值
        for(int[] t : trust){
            trustValues[t[0]]--;
            trustValues[t[1]]++;
        }

        // 遍历这n个人的信任值，如果存在 n - 1，则返回这个人的编号
        for(int i =1; i <= n;i++){
            if(trustValues[i] == (n - 1)) return i;
        }
        return -1;
    }
}
```

```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_val = [0] * (n + 1)
        for t in trust:
            trust_val[t[0]] -= 1
            trust_val[t[1]] += 1
        for i in range(1, n + 1):
            if trust_val[i] == n - 1: 
                return i
        return -1
```

```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1: return -1
        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)
        for i, j in trust:
            outdegree[i] += 1
            indegree[j] += 1
        for i in range(1, n+1):
            if indegree[i] == n-1 and outdegree[i] == 0: return i
        return -1
```
