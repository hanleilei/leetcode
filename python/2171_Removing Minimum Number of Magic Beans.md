# Removing Minimum Number of Magic Beans

You are given an array of positive integers beans, where each integer represents the number of magic beans found in a particular magic bag.

Remove any number of beans (possibly none) from each bag such that the number of beans in each remaining non-empty bag (still containing at least one bean) is equal. Once a bean has been removed from a bag, you are not allowed to return it to any of the bags.

Return the minimum number of magic beans that you have to remove.


## Example 1

```text
Input: beans = [4,1,6,5]
Output: 4
Explanation: 
- We remove 1 bean from the bag with only 1 bean.
  This results in the remaining bags: [4,0,6,5]
- Then we remove 2 beans from the bag with 6 beans.
  This results in the remaining bags: [4,0,4,5]
- Then we remove 1 bean from the bag with 5 beans.
  This results in the remaining bags: [4,0,4,4]
We removed a total of 1 + 2 + 1 = 4 beans to make the remaining non-empty bags have an equal number of beans.
There are no other solutions that remove 4 beans or fewer.
```

## Example 2

```text
Input: beans = [2,10,3,2]
Output: 7
Explanation:
- We remove 2 beans from one of the bags with 2 beans.
  This results in the remaining bags: [0,10,3,2]
- Then we remove 2 beans from the other bag with 2 beans.
  This results in the remaining bags: [0,10,3,0]
- Then we remove 3 beans from the bag with 3 beans. 
  This results in the remaining bags: [0,10,0,0]
We removed a total of 2 + 2 + 3 = 7 beans to make the remaining non-empty bags have an equal number of beans.
There are no other solutions that removes 7 beans or fewer.
```

## Constraints

```text
1 <= beans.length <= 10**5
1 <= beans[i] <= 10**5
```

```python
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        s, n = sum(beans), len(beans)
        return min(s - x * (n - i) for i, x in enumerate(beans))
```

我们可以将 beans\textit{beans}beans 从小到大排序后，枚举最终非空袋子中魔法豆的数目 vvv，将小于 vvv 的魔法豆全部清空，大于 vvv 的魔法豆减少至 vvv，这样所有非空袋子中的魔法豆就都相等了。

由于拿出魔法豆 + 剩余魔法豆 = 初始魔法豆之和，我们可以考虑最多能剩下多少个魔法豆，从而计算出最少能拿出多少个魔法豆。

![](https://pic.leetcode-cn.com/1644881496-veNnxl-2171.drawio%20(2).png)

如上图所示，可以保留蓝色矩形区域内的魔法豆。设 beans\textit{beans}beans 的长度为 n，以 n−i 为矩形底边长，v=beans[i]为矩形高，则矩形面积为

(n−i) * v

用 ∑beans[i] 减去矩形面积的最大值，即为拿出魔法豆的最小值。

```python
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        return sum(beans) - max((len(beans) - i) * v for i, v in enumerate(beans))
```

还是脑筋急转弯的问题，不过好像我没转过来。。
