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

差分熟组：

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
