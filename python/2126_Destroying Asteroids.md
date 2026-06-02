# Destroying Asteroids

[[binarysearch]]

You are given an integer mass, which represents the original mass of a planet. You are further given an integer array asteroids, where asteroids[i] is the mass of the ith asteroid.

You can arrange for the planet to collide with the asteroids in any arbitrary order. If the mass of the planet is greater than or equal to the mass of the asteroid, the asteroid is destroyed and the planet gains the mass of the asteroid. Otherwise, the planet is destroyed.

Return true if all asteroids can be destroyed. Otherwise, return false.

Example 1:

Input: mass = 10, asteroids = [3,9,19,5,21]
Output: true
Explanation: One way to order the asteroids is [9,19,5,3,21]:

- The planet collides with the asteroid with a mass of 9. New planet mass: 10 + 9 = 19
- The planet collides with the asteroid with a mass of 19. New planet mass: 19 + 19 = 38
- The planet collides with the asteroid with a mass of 5. New planet mass: 38 + 5 = 43
- The planet collides with the asteroid with a mass of 3. New planet mass: 43 + 3 = 46
- The planet collides with the asteroid with a mass of 21. New planet mass: 46 + 21 = 67
All asteroids are destroyed.

Example 2:

Input: mass = 5, asteroids = [4,9,23,4]
Output: false
Explanation:
The planet cannot ever gain enough mass to destroy the asteroid with a mass of 23.
After the planet destroys the other asteroids, it will have a mass of 5 + 4 + 9 + 4 = 22.
This is less than 23, so a collision would not destroy the last asteroid.

Constraints:

1 <= mass <= 10^5
1 <= asteroids.length <= 10^5
1 <= asteroids[i] <= 10^5

二分法：

```python
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        n = len(asteroids)
        left = 0
        while left < n:
            # 找到第一个 > mass 的位置，这样 asteroids[left:right] 都是 <= mass 的
            right = bisect.bisect_right(asteroids, mass, left)
            if right == left:   # 没有可吸收的小行星，但还有剩余 → 失败
                return False
            mass += sum(asteroids[left:right])
            left = right
        return True
```

前缀和：

```python
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        acc = accumulate(asteroids, initial=mass)
        return all(x <= y for x, y in zip(asteroids, acc))
```

heap:

```python
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heapq.heapify(asteroids)
        while asteroids:
            minial = heappop(asteroids)
            if mass >= minial:
                mass += minial
            else:
                return False
        return True
```

再来吧累加玩的花一点，每次都把能吃掉的都吃掉，直到不能吃了为止：

所以时间复杂度是 O(n^2)，因为每次都要遍历 asteroids 来找能吃掉的。配合剪枝，如果一次都吃不掉了，那么就直接返回 False。

```python
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        mx = max(asteroids)

        while asteroids:
            uneaten = []
            for aster in asteroids:
                if mass < aster:
                    uneaten.append(aster)
                else:
                    mass += aster
                    if mass >= mx:
                        return True
            if len(uneaten) == len(asteroids):
                return False
            
            asteroids = uneaten
        
        return True
```

按二进制长度分组

这个做法基于一个简单的事实：

    一个 ≥2^k 的数，加上另一个 ≥2^k 的数，和一定 ≥2^(k+1)。

基于这一事实，我们可以把 asteroids 中的元素按照二进制长度分组：

    在 [2^0,2^1) 中的数分到同一组。
    在 [2^1,2^2) 中的数分到同一组。
    在 [2^2,2^3) 中的数分到同一组。
    ……

设行星的质量为 M。如果 M≥ 组内最小值，那么 M 加上组内最小值后，结果一定大于组内的每个值，所以这一组的质量可以全部加到 M 中。如此一来，我们只需统计每一组的最小值，以及每一组的元素和，无需对组内元素排序。

```python
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        max_width = max(asteroids).bit_length()
        mn = [inf] * max_width
        sum_ = [0] * max_width

        for x in asteroids:
            i = x.bit_length() - 1
            mn[i] = min(mn[i], x)
            sum_[i] += x

        for m, s in zip(mn, sum_):
            if m == inf:
                continue
            if mass < m:  # 无法摧毁这组的任意小行星
                return False
            mass += s  # 获得这组小行星的质量
        return True
```

```python
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        mn = defaultdict(lambda: inf)
        sum_ = defaultdict(int)
        mask = 0

        for x in asteroids:
            i = x.bit_length() - 1
            mn[i] = min(mn[i], x)
            sum_[i] += x
            mask |= 1 << i

        while mask:
            lowbit = mask & -mask  # mask 的最低位
            i = lowbit.bit_length() - 1
            if mass < mn[i]:  # 无法摧毁这组的任意小行星
                return False
            mass += sum_[i]  # 获得这组小行星的质量
            mask ^= lowbit  # 移除 mask 的最低位
        return True
```
