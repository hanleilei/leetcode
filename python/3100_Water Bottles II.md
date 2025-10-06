# Water Bottles II

You are given two integers numBottles and numExchange.

numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

Drink any number of full water bottles turning them into empty bottles.
Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.

Return the maximum number of water bottles you can drink.

 

Example 1:

![](https://assets.leetcode.com/uploads/2024/01/28/exampleone1.png)

Input: numBottles = 13, numExchange = 6
Output: 15
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.


Example 2:

![](https://assets.leetcode.com/uploads/2024/01/28/example231.png)

Input: numBottles = 10, numExchange = 3
Output: 13
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
 

Constraints:

1 <= numBottles <= 100 
1 <= numExchange <= 100


```python
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        empty = numBottles

        while empty >= numExchange:
            res += 1
            empty -= numExchange - 1
            numExchange += 1
        
        return res
```


​数学推导过程​

​1. 问题建模​

每次兑换后：
​消耗​ k个空瓶 → 兑换 1 个满瓶（喝掉后得到 1 个空瓶）。
​净消耗​：k - 1个空瓶（因为喝掉后又还回 1 个空瓶）。
​兑换比率增长​：k += 1（每次兑换后 k增加 1）。
设总共兑换 x次，则：
​初始空瓶​：n（喝完初始 n瓶后得到 n个空瓶）。
​总净消耗​：
第 1 次兑换：消耗 k - 1空瓶。
第 2 次兑换：消耗 (k + 1) - 1 = k空瓶。
...
第 x次兑换：消耗 (k + x - 1) - 1 = k + x - 2空瓶。
​总净消耗约束​：(k - 1) + k + (k + 1) + ... + (k + x - 2) ≤ n

2. 求和公式​

这是一个 ​等差数列求和​：
首项 a₁ = k - 1，末项 aₓ = k + x - 2，项数 x。
求和公式：
S = x * (a₁ + aₓ) / 2 ≤ n

x * [(k - 1) + (k + x - 2)] / 2 ≤ n
x * (2k + x - 3) / 2 ≤ n
x² + (2k - 3)x - 2n ≤ 0

​3. 解二次方程​

解 x² + (2k - 3)x - 2n = 0：
判别式：Δ = (2k - 3)² + 8n
正根： x = [-(2k - 3) + √(Δ)] / 2
x = (-2k + 3 + √(4k² - 12k + 9 + 8n)) / 2

4. 总瓶子数​
初始喝 n瓶。
每次兑换喝 1瓶，共 x次。
​总瓶子数​：n + xb

```python
class Solution:
    def maxBottlesDrunk(self, n: int, k: int) -> int:
        return int(n+((-2*k+3+sqrt(4*k*k+8*n-12*k+1))/2))
```
