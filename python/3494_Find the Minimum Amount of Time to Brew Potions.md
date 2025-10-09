# Find the Minimum Amount of Time to Brew Potions

[[dp]] [[prefixSum]]

You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.

 

Example 1:

Input: skill = [1,5,2,4], mana = [5,1,4,2]

Output: 110

Explanation:

| i   | skill[i] | lastFinish[i] | 完成时间        |
| :-- | :------- | :------------ | :-------------- |
| 0   | 1        | 5             | 5+1=6           |
| 1   | 5        | 30            | max(6,30)+5=35  |
| 2   | 2        | 40            | max(35,40)+2=42 |
| 3   | 4        | 60            | max(42,60)+4=64 |

As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.

Example 2:

Input: skill = [1,1,1], mana = [1,1,1]

Output: 5

Explanation:

Preparation of the 0th potion begins at time t = 0, and is completed by time t = 3.
Preparation of the 1st potion begins at time t = 1, and is completed by time t = 4.
Preparation of the 2nd potion begins at time t = 2, and is completed by time t = 5.
Example 3:

Input: skill = [1,2,3,4], mana = [1,2]

Output: 21

 

Constraints:

n == skill.length
m == mana.length
1 <= n, m <= 5000
1 <= mana[i], skill[i] <= 5000
 
## 解法：

都是来自灵神。。我只能想到第一个。。

1. 正反两次扫描：

为了计算酿造药水的时间，定义 lastFinish[i] 表示巫师 i 完成上一瓶药水的时间。

示例 1 在处理完 mana[0] 后，有 `res=[5,30,40,60]`

如果接着 res 继续酿造下一瓶药水 mana[1]=1，完成时间是多少？注意开始酿造的时间不能早于 res[i]。

| i   | skill[i] | lastFinish[i] | 完成时间        |
| :-- | :------- | :------------ | :-------------- |
| 0   | 1        | 5             | 5+1=6           |
| 1   | 5        | 30            | max(6,30)+5=35  |
| 2   | 2        | 40            | max(35,40)+2=42 |
| 3   | 4        | 60            | max(42,60)+4=64 |

题目要求「药水在当前巫师完成工作后必须立即传递给下一个巫师并开始处理」，也就是说，酿造药水的过程中是不能有停顿的。

从 64 开始倒推，可以得到每名巫师的实际完成时间。比如倒数第二位巫师的完成时间，就是 64 减去最后一名巫师花费的时间 4⋅1，得到 60。

| i   | skill[i+1] | 实际完成时间 |
| :-- | :--------- | :----------- |
| 3   | -          | 64           |
| 2   | 4          | 64−4⋅1=60    |
| 1   | 2          | 60−2⋅1=58    |
| 0   | 5          | 58−5⋅1=53    |


按照上述过程处理每瓶药水，最终答案为 res[n−1]。

```python
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        res = [0] * n
        for m in mana:
            sum_t = 0
            for x, last in zip(skill, res):
                sum_t = max(sum_t, last)
                sum_t += x * m
            res[-1] = sum_t
            for i in range(n - 2, -1, -1):
                res[i] = res[i+1] - skill[i + 1] * m
        return res[-1]
```

时间复杂度：O(nm)，其中 n 是 skill 的长度，m 是 mana 的长度。
空间复杂度：O(n)。

2. 递推开始时间
由于酿造药水的过程是连续的，所以知道了开始时间（或者完成时间）就能知道每个 lastFinish[i]。所以 lastFinish 数组是多余的。

设开始酿造 mana[j] 的时间为 $start_j$ ，那么有 $lastFinish_j[i] = start_j + mana[j] * \displaystyle\sum_{k=0}^i skill[k]$

在已知 $start_{j−1}$ 的前提下，能否递推算出 start_j？

哪位巫师决定了开始时间？假设第 i 位巫师决定了开始时间，那么这位巫师完成 mana[j−1] 的时间，同时也是他开始 mana[j] 的时间。

所以有 $lastFinish_{j - 1}[i] + mana[j] * skill[i] = lastFinish_j[i]$

两边带入$lastFinish_j[i]$的式子，得到：$start_{j-1} + mana[j-1] * \displaystyle\sum_{k=0}^i skill[k] + mana[j] * skill[i] = start_j  + mana[j] * \displaystyle\sum_{k=0}^i skill[k]$

移项得: $start_j = start_{j-1} + mana[j-1]*\displaystyle\sum_{k=0}^i skill[k] - mana[j] * \displaystyle\sum_{k=0}^{i-1} skill[k]$

计算 skill 的 前缀和数组 s，上式为 $skill_j = skill_{j-1} + mana[j-1] * s[i+1] - mana[j]* s[i]$

枚举 i，取最大值，得到：$skill_j = skill_{j-1} + \displaystyle\max_{i=0}^{n-1} \{mana[j-1] * s[i+1] - mana[j]*s[i]\}$

初始值 $start_0 = 0$

答案为： $lastFinish_{m-1}[n-1] = start_{m-1} + mana[m-1] * s[n]$

```python
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        s = list(accumulate(skill, initial=0))  # skill 的前缀和
        start = 0
        for pre, cur in pairwise(mana):
            start += max(pre * s[i + 1] - cur * s[i] for i in range(n))
        return start + mana[-1] * s[-1]
```
时间复杂度：O(nm)，其中 n 是 skill 的长度，m 是 mana 的长度。
空间复杂度：O(n)。如果在遍历的同时计算前缀和，则可以做到 O(1) 空间。

3. Record 优化

将递推式：$skill_j = skill_{j-1} + \displaystyle\max_{i=0}^{n-1} {mana[j-1] * s[i+1] - mana[j]*s[i]}$
变形为：$skill_j = skill_{j-1} + \displaystyle\max_{i=0}^{n-1} \{mana[j-1] - mana[j]) * s[i] + mana[j-1] * skill[i]\}$

设 d = mana[j-1] - mana[j]

- 如果 d>0。由于 s 是单调递增数组，如果 skill[3]<skill[5]，那么 i=3 绝对不会算出最大值；但如果 skill[3]>skill[5]，谁会算出最大值就不一定了。所以我们只需要考虑 skill 的逆序 record，这才是可能成为最大值的数据。其中逆序 record 的意思是，倒序遍历 skill，每次遍历到更大的数，就记录下标。
- 如果 d<0。由于 s 是单调递增数组，如果 skill[5]<skill[3]，那么 i=5 绝对不会算出最大值；但如果 skill[5]>skill[3]，谁会算出最大值就不一定了。所以我们只需要考虑 skill 的正序 record，这才是可能成为最大值的数据。其中正序 record 的意思是，正序遍历 skill，每次遍历到更大的数，就记录下标。
- d=0 的情况可以并入 d>0 的情况。

```python
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        s = list(accumulate(skill, initial=0))

        suf_record = [n - 1]
        for i in range(n - 2, -1, -1):
            if skill[i] > skill[suf_record[-1]]:
                suf_record.append(i)

        pre_record = [0]
        for i in range(1, n):
            if skill[i] > skill[pre_record[-1]]:
                pre_record.append(i)

        start = 0
        for pre, cur in pairwise(mana):
            record = pre_record if pre < cur else suf_record
            start += max(pre * s[i + 1] - cur * s[i] for i in record)
        return start + mana[-1] * s[-1]
```
由调和级数可知，record 的期望长度为 Θ(logn)。

时间复杂度：Θ(n+mlogn)，其中 n 是 skill 的长度，m 是 mana 的长度。
空间复杂度：O(n)。

4. 凸包 + 二分

将递推式：$skill_j = skill_{j-1} + \displaystyle\max_{i=0}^{n-1} {mana[j-1] * s[i+1] - mana[j]*s[i]}$ 中的 $\{mana[j-1] * s[i+1] - mana[j]*s[i]\}$ 改成点积的形式，这样我们能得到来自几何意义上的观察。

设向量 $v_i =(s[i],skill[i])$

设向量 $p=(mana[j−1]−mana[j],mana[j−1])$。

那么我们求的是: $\displaystyle\max_{i=0}^{n-1} \mathbf{p} \cdot \mathbf{v}_i$

根据点积的几何意义，我们求的是 $v_i$ 在 p 方向上的投影长度，再乘以 p 的模长 ∣∣p∣∣。由于 ∣∣p∣∣ 是个定值，所以要最大化投影长度。

考虑 $v_i$ 的上凸包（用 Andrew 算法计算），在凸包内的点，就像是山坳，比凸包顶点的投影长度短。所以只需考虑凸包顶点。

这样有一个很好的性质：顺时针（或者逆时针）遍历凸包顶点，p⋅v 
i
​
 会先变大再变小（单峰函数）。那么要计算最大值，就类似 852题目. 山脉数组的峰顶索引，二分首个「下坡」的位置


```python
class Vec:
    __slots__ = 'x', 'y'

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, b: "Vec") -> "Vec":
        return Vec(self.x - b.x, self.y - b.y)

    def det(self, b: "Vec") -> int:
        return self.x * b.y - self.y * b.x

    def dot(self, b: "Vec") -> int:
        return self.x * b.x + self.y * b.y

class Solution:
    # Andrew 算法，计算 points 的上凸包
    # 由于横坐标（前缀和）是严格递增的，所以无需排序
    def convex_hull(self, points: List[Vec]) -> List[Vec]:
        q = []
        for p in points:
            while len(q) > 1 and (q[-1] - q[-2]).det(p - q[-1]) >= 0:
                q.pop()
            q.append(p)
        return q

    def minTime(self, skill: List[int], mana: List[int]) -> int:
        s = list(accumulate(skill, initial=0))
        vs = [Vec(pre_sum, x) for pre_sum, x in zip(s, skill)]
        vs = self.convex_hull(vs)  # 去掉无用数据

        start = 0
        for pre, cur in pairwise(mana):
            p = Vec(pre - cur, pre)
            # p.dot(vs[i]) 是个单峰函数，二分找最大值
            check = lambda i: p.dot(vs[i]) > p.dot(vs[i + 1])
            i = bisect_left(range(len(vs) - 1), True, key=check)
            start += p.dot(vs[i])
        return start + mana[-1] * s[-1]
```
时间复杂度：O(n+mlogn)，其中 n 是 skill 的长度，m 是 mana 的长度。
空间复杂度：O(n)。

第二个方法向量化：

```python
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        s = np.array(skill).cumsum()
        s = np.insert(s, 0, 0)
        start = 0
        for pre, cur in pairwise(mana):
            terms = pre * s[1:] - cur * s[:-1]
            start += np.max(terms)
        return int(start + mana[-1] * s[-1])
```





