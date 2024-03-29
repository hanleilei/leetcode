# Champagne Tower

[[dp]]

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png)

Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

## Example 1
```text
Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.
```

## Example 2

```text
Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
```

## Example 3

```text
Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000
```

## Constraints


- ```0 <= poured <= 109```
- ```0 <= query_glass <= query_row < 100```

```python
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 定义当前层
        dp2 = [poured]
        for i in range(1, query_row + 1):
            # 定义下一层
            dp1 = [0] * (i + 1)
            for j, v in enumerate(dp2):
                if v > 1:
                    half = (v - 1) / 2
                    dp1[j] += half
                    dp1[j + 1] += half
                dp2 = dp1
        return min(1, dp2[query_glass])
```

再来一个二维的：

```python
class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        # DP solution 
        res = [[0.0 for _ in range(i)] for i in range(1, query_row + 2)]
        res[0][0] = poured
        
        for i in range(query_row):
            for j in range(len(res[i])):
                if res[i][j] > 1 :
                    res[i+1][j] += (res[i][j] - 1) / 2.0
                    res[i+1][j+1] += (res[i][j] - 1) / 2.0
        
        return res[query_row][query_glass] if res[query_row][query_glass] <= 1 else 1
```
