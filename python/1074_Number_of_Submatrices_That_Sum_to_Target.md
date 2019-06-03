# Number of Submatrices That Sum to Target

Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.



Example 1:
```
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
```

Example 2:
```
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
```

Note:
```
1 <= matrix.length <= 300
1 <= matrix[0].length <= 300
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
```

```Python
class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        """
        For each row, calculate the prefix sum.
        For each pair of columns,
        calculate the sum rows.

        Now this problem is changed to, "find the subarray with target sum".

        """
        m, n = len(A), len(A[0])
        for row in A:
            for i in range(n - 1):
                row[i + 1] += row[i]
        res = 0
        for i in range(n):
            for j in range(i, n):
                c = collections.Counter({0: 1})
                cur = 0
                for k in range(m):
                    cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1
        return res

```

题意：给一个矩阵，问满足要求的子矩阵个数。
这里的要求是矩阵和等于给定的值。

思路：对于子矩阵问题，有一个万能的方法。
首先是枚举子矩阵的上面那条边，然后枚举矩阵的下面那条边，这个过程中，可以累积计算出每一列的值，目前复杂度O(n^2)。
这样，问题就转化为了有一个一维数组（列的累计值），求这个数组里面满足要求的子数组个数。
对于一维数组求子数组最优值，则需要具体情况具体分析了，但是复杂度不要超过O(n^2)，最优的是O(n)，次之是O(n log(n))。

比如对于最大子序列和，就是O(n)的复杂度。
这道题是求子序列和等于指定值的个数，那就只能统计前缀和O(n)，然后判断快速判断当前后缀是否存在答案了O(log(n))。

具体到这道题，如果当前位置为后缀的序列pre,pre+1,...,now有存在答案，则当前前缀1,2,3,..., now和减去前面的某个前缀和1,2,...,pre，等于指定值。
翻过来就是，当前前缀1,2,3,..., now减去指定值，存在某个1,2,...,pre等于这个差值。

这里使用map或者hash_map储存前缀和以及个数，然后查找是否存在，存在则找到一个答案。
```java
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        vector<int> sum(matrix[0].size(), 0);

        int ans = 0;
        for(int i=0; i<matrix.size(); i++){
            for(int j=0; j<sum.size(); j++) sum[j]=0;

            for(int t=i; t<matrix.size(); t++){
                for(int j=0; j<sum.size(); j++) sum[j]+=matrix[t][j];

                map<int, int> preSet;
                int preSum = 0;
                preSet[preSum] = 1;

                for(int j=0;j<sum.size();j++){
                    preSum += sum[j];
                    int tmp = preSum - target;
                    if(preSet.find(tmp) != preSet.end()){
                        ans += preSet[tmp];
                    }
                    preSet[preSum]++;
                }
            }

        }

        return ans;
    }
};
```
