# Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9

## 解法一：二分查找（推荐）

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        使用二分查找确定最小吃香蕉速度
        时间复杂度：O(n log m)，其中 n 是 piles 的长度，m 是 piles 中的最大值
        空间复杂度：O(1)
        """
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)  # 计算以 mid 速度吃完所有香蕉所需的小时数
            
            if hours > h:
                left = mid + 1  # 吃得太慢，增加速度
            else:
                right = mid  # 吃得足够快，尝试降低速度
        return left
```

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        n = len(piles)
        left = 0
        right = max(piles)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if sum((p - 1) // mid  for p in piles) <= h - n:
                right = mid
            else:
                left = mid
        return right
```

## 解法二：二分查找（labuladong 方法）

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = 1000000000 + 1

        while left < right:
            mid = left + (right - left) // 2
            if self.f(piles, mid) <= H:
                right = mid
            else:
                left = mid + 1
        return left

    # 定义：速度为 x 时，需要 f(x) 小时吃完所有香蕉
    # f(x) 随着 x 的增加单调递减
    def f(self, piles: List[int], x: int) -> int:
        hours = 0
        for pile in piles:
            hours += pile // x
            if pile % x > 0:
                hours += 1
        return hours
```


