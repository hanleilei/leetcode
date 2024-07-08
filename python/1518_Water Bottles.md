# Water Bottles

There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

Example 1:

![](https://assets.leetcode.com/uploads/2020/07/01/sample_1_1875.png)

Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Example 2:

![](https://assets.leetcode.com/uploads/2020/07/01/sample_2_1875.png)

Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.

Constraints:

1 <= numBottles <= 100
2 <= numExchange <= 100

最简单的方法：直接仿真，一步步执行操作：

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        drank = 0
        while numBottles:
            drank += 1
            empty += 1
            numBottles -= 1
            if empty == numExchange:
                empty -= numExchange
                numBottles += 1
        return drank
```

You can exchange numExchange empty water bottles from the market with one full water bottle. In the other words, if you have (numExchange-1) empty water bottles, you can borrow one full water bottle from your friend, and drink it, then exchange numExchange empty bottles to one full bottle. Then return it to your friend. Therefore, for every (numExchange-1) empty water bottles, you can gain one free drink!

Adding more details to help on intuition, now you have numBottles, you take out one full bottle aside, for each step, you drink that bottle, and you take (numExchange-1) from your empty bottles, and exchange them to one full bottle and put it back. So the extra bottles number is: (numBottles-1)//(numExchange-1)

You can calculate the extra bottles by dividing your number of bottles by (numExchange-1). However, you always need to borrow one bottle for exchange, so the extra bottles is: (numBottles-1)/(numExchange-1).

So it is one line solution:

return numBottles + (numBottles-1)//(numExchange-1)

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)
```
