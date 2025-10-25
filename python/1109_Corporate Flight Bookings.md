# Corporate Flight Bookings

There are `n` flights that are labeled from `1` to `n`.

You are given an array of flight bookings `bookings`, where `bookings[i] = [firsti, lasti, seatsi]` represents a booking for flights `firsti` through `lasti` (**inclusive**) with `seatsi` seats reserved for **each flight** in the range.

Return *an array* `answer` *of length* `n`*, where* `answer[i]` *is the total number of seats reserved for flight* `i`.

**Example 1:**

**Input:** bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
**Output:** [10,55,45,25,25]
**Explanation:**
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]

**Example 2:**

**Input:** bookings = [[1,2,10],[2,2,15]], n = 2
**Output:** [10,25]
**Explanation:**
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25
Hence, answer = [10,25]

**Constraints:**

- `1 <= n <= 2 * 104`
- `1 <= bookings.length <= 2 * 104`
- `bookings[i].length == 3`
- `1 <= firsti <= lasti <= n`
- `1 <= seatsi <= 104`

典型的差分数组题目。。。

```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for l, r, d in bookings:
            res[l - 1] += d
            if r < n:
                res[r] -= d
        return list(accumulate(res))
```

```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)  # 初始化 n+1 避免越界
        for first, last, seats in bookings:
            diff[first - 1] += seats
            if last < n:  # 防止越界（但 n+1 已经解决）
                diff[last] -= seats
            # 或者直接 diff[last] -= seats（因为 diff 是 n+1 长度）
        res = [0] * n
        res[0] = diff[0]
        for i in range(1, n):
            res[i] = res[i - 1] + diff[i]
        return res
```

```python
class Solution:
    def corpFlightBookings(self, bookings, n):
        # nums 初始化为全 0
        nums = [0] * n
        # 构造差分解法
        df = self.Difference(nums)

        for booking in bookings:
            # 注意转成数组索引要减一哦
            i = booking[0] - 1
            j = booking[1] - 1
            val = booking[2]
            # 对区间 nums[i..j] 增加 val
            df.increment(i, j, val)
        # 返回最终的结果数组
        return df.result()

    class Difference:
        # 差分数组
        def __init__(self, nums):
            assert len(nums) > 0
            self.diff = [0] * len(nums)
            # 构造差分数组
            self.diff[0] = nums[0]
            for i in range(1, len(nums)):
                self.diff[i] = nums[i] - nums[i - 1]

        # 给闭区间 [i, j] 增加 val（可以是负数）
        def increment(self, i, j, val):
            self.diff[i] += val
            if j + 1 < len(self.diff):
                self.diff[j + 1] -= val

        def result(self):
            res = [0] * len(self.diff)
            # 根据差分数组构造结果数组
            res[0] = self.diff[0]
            for i in range(1, len(self.diff)):
                res[i] = res[i - 1] + self.diff[i]
            return res
```
