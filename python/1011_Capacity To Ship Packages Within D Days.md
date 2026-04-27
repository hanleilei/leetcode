# Capacity To Ship Packages Within D Days

[[binarysearch ]]

A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Constraints:

1 <= days <= weights.length <= 5 * 10^4
1 <= weights[i] <= 500

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = 1
        for w in weights:
            left = max(left, w)
            right += w

        while left < right:
            mid = left + (right - left) // 2
            if self.f(weights, mid) <= days:
                right = mid
            else:
                left = mid + 1

        return left

    # 定义：当运载能力为 x 时，需要 f(x) 天运完所有货物
    # f(x) 随着 x 的增加单调递减
    def f(self, weights: List[int], x: int) -> int:
        days = 0
        i = 0
        while i < len(weights):
            # 尽可能多装货物
            cap = x
            while i < len(weights):
                if cap < weights[i]:
                    break
                else:
                    cap -= weights[i]
                    i += 1
            days += 1
        return days
```

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            need = 1
            current = 0
            for weight in weights:
                if current + weight > mid:
                    need += 1
                    current = 0
                current += weight
            if need > days:
                left = mid + 1
            else:
                right = mid
        return left
```

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(k:int, pre_sum:List[int], days:int) -> bool:
            i = 0
            n = len(pre_sum)
            pre = 0
            while days > 0:  # 划分days次
                j = bisect_right(pre_sum, k+pre, i) - 1
                if j < 0:
                    return False
                pre = pre_sum[j]  # 前面几次运输的总重量
                i = j + 1
                days -= 1
            return i == n  # 是否到达最后一个物品

        n = len(weights)
        left = sum(weights)//days   # k最小值总重量的平均值
        right = ceil(n/days)*max(weights) # 将n个物品平均分配到每一天，并且都是最大重量的物品
        pre_sum = list(accumulate(weights, initial=0))
        while left <= right:
            mid = (left+right)//2
            if check(mid, pre_sum, days):
                right = mid - 1
            else:
                left = mid + 1
        return left
```
