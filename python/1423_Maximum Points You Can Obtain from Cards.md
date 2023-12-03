# Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

## Example 1

```text
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
```

## Example 2

```text
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
```

## Example 3

```text
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
```

## Constraints

```text
1 <= cardPoints.length <= 105
1 <= cardPoints[i] <= 104
1 <= k <= cardPoints.length
```

自制的dummy方法：

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        windows = [0] + cardPoints[:k][::-1] + cardPoints[-k:][::-1]
        res = float('-inf')

        for i in range(1, len(windows)):
            windows[i] += windows[i - 1]

        for i in range(len(windows) - k):
            res = max(res, windows[i + k] - windows[i])
        return res
```

再来一个速度快的，这里的套路就是：
1. 算出来前k的和，然后依次加上最后一个元素，减去第k个元素，以此类推，比我的方法减少了很多计算，也少了构造数组的问题。

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        windowSum = sum(cardPoints[:k])
        res = windowSum

        for i in range(1,k+1):
            windowSum = windowSum + cardPoints[-i] - cardPoints[k-i]
            res = max(res, windowSum)
        
        return res
```

或者另一种方法：

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxpoint = current = sum(cardPoints[:k])

        for i in range(k-1,-1,-1):
            current = current - cardPoints[i] + cardPoints[i-k]
            maxpoint = max(current, maxpoint)
        return maxpoint
```

两种方法思路一样，但是下面的方法要快一些，很奇怪。。