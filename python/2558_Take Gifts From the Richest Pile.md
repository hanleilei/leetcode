# Take Gifts From the Richest Pile

[[heap]]

You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.

## Example 1

```text
Input: gifts = [25,64,9,4,100], k = 4
Output: 29
Explanation: 
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.
```

## Example 2

```text
Input: gifts = [1,1,1,1], k = 4
Output: 4
Explanation: 
In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile. 
That is, you can't take any pile with you. 
So, the total gifts remaining are 4.
```

## Constraints

```text
1 <= gifts.length <= 103
1 <= gifts[i] <= 109
1 <= k <= 103
```

直接使用heapq

```python
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            heapq.heappush(gifts, -floor(sqrt(-heapq.heappop(gifts))))
        return -sum(gifts)
```

呃，有点忘记了heapq的用法了：

```python
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # 将所有礼物的负数值加入堆（模拟最大堆）
        nums = [-i for i in gifts]
        heapify(nums)  # 转化为最小堆

        for _ in range(k):
            # 弹出最大值（堆顶负数最小）
            max_val = -heappop(nums)
            # 计算新值
            min_val = floor(sqrt(max_val))
            # 将新值重新加入堆
            heappush(nums, -min_val)

        # 计算剩余值的总和
        return -sum(nums)
```
