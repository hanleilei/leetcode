# car polling

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

## Example 1

```text
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

## Example 2

```text
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

## Constraints

```text
1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
```

十秒想出来的方法：

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res = [0] * max([i[2] for i in trips])
        for passenger, f,t in trips:
            for i in range(f, t ):
                res[i] += passenger
                if res[i] > capacity:
                    return False
        return True
```

显然，这个是糟糕透顶的方法！留着作为耻辱吧。

差分数组：

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * (max(trip[2] for trip in trips) + 1 )

        for (count, start, end) in trips:
            passengers[start] += count
            passengers[end] -= count

        curr_no_of_passengers = 0
        for no_of_passengers in passengers:
            curr_no_of_passengers += no_of_passengers
            if curr_no_of_passengers > capacity:
                return False
            
        return True
```

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * (1000+1)
        for p, s, e in trips:
            diff[s] += p
            diff[e] -= p

        cur_passengers = 0
        for i in range(len(diff)):
            cur_passengers += diff[i]
            if cur_passengers > capacity:
                return False
        return True
```

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = [0] * 1001
        for num, from_, to in trips:
            d[from_] += num
            d[to] -= num
        return all(s <= capacity for s in accumulate(d))
```

查分数组的问题，是一类数组的问题：对于区间的数字做加法和减法。要注意边界条件，也就是第一个元素和最后一个元素。

另外，对于Python而言，最后的通过差分数组还原结果数组的时候，可以使用导入：
`from itertools import accumulate` 然后使用 accumulate 函数作为生成器是实现。

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 最多有 1000 个车站
        nums = [0] * 1001
        # 构造差分解法
        df = self.Difference(nums)

        for trip in trips:
            # 乘客数量
            val = trip[0]
            # 第 trip[1] 站乘客上车
            i = trip[1]
            # 第 trip[2] 站乘客已经下车，
            # 即乘客在车上的区间是 [trip[1], trip[2] - 1]
            j = trip[2] - 1
            # 进行区间操作
            df.increment(i, j, val)

        res = df.result()

        # 客车自始至终都不应该超载
        for i in range(len(res)):
            if capacity < res[i]:
                return False
        return True

    # 差分数组工具类
    class Difference:
        # 差分数组
        def __init__(self, nums: List[int]):
            # 输入一个初始数组，区间操作将在这个数组上进行
            # 根据初始数组构造差分数组
            self.diff = [nums[0]] + [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        # 给闭区间 [i, j] 增加 val（可以是负数）
        def increment(self, i: int, j: int, val: int) -> None:
            self.diff[i] += val
            if j + 1 < len(self.diff):
                self.diff[j + 1] -= val

        # 返回结果数组
        def result(self) -> List[int]:
            res = [self.diff[0]]
            # 根据差分数组构造结果数组
            for i in range(1, len(self.diff)):
                res.append(res[i - 1] + self.diff[i])
            return res
```
