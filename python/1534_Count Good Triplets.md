# Count Good Triplets

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.

Constraints:

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000

方法一:暴力枚举

```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # 暴力枚举
        n=len(arr)
        count=0
        # 三重循环:三个下标索引各不相等
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        count+=1
        return count
```

枚举优化:减少重复计算

```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # 暴力枚举
        n=len(arr)
        count=0

        for i in range(n):
            for j in range(i+1,n):
                # 利用已经知道的关于i,j下标的限制减少循环次数
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1,n):
                        if abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                            count+=1
        return count
```


```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # 暴力枚举
        n = len(arr)
        count = 0

        # 进一步优化
        # 设计数组记录传入数组中元素<=i的数目,也即total[i]
        total = [0] * 1001
        for j in range(n):
            for k in range(j + 1, n):
                # 利用已经知道的关于i,j下标的限制减少循环次数
                if abs(arr[j] - arr[k]) <= b:
                    l_j, r_j = arr[j] - a, arr[j] + a
                    l_k, r_k = arr[k] - c, arr[k] + c
                    left = max(l_j, l_k, 0)
                    right = min(r_j, r_k, 1000)
                    # 寻找i<j 并且满足 left<=nums[i]<=right的下标i
                    if left <= right:
                        count += (
                            total[right]
                            if left == 0
                            else total[right] - total[left - 1]
                        )
            # 这里total[i]代表arr中小于等于i的元素数目
            for k in range(arr[j], 1001):
                total[k] += 1

        return count
```

速度最快的方法：

```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # 暴力枚举
        n = len(arr)
        count = 0
        # 上述算法在当数组内元素比较小而值域非常大时,需要大量的加法和更新操作,我们选取另外一种方式
        # 用record数组存储数组当中当下标小于j时 值域<=i的元素数目,也即 record[i]记录了在当前j取值下小于等于i的元素数目

        # 当right=1000时,record[1001]要求数组长度必须至少是1002
        record = [0] * 1002
        for j in range(n):
            for k in range(j + 1, n):
                # 剪枝:利用限制减少比较次数
                if abs(arr[j] - arr[k]) <= b:
                    left = max(0, arr[j] - a, arr[k] - c)
                    right = min(1000, arr[j] + a, arr[k] + c)
                    # 若left<=right,则
                    if left <= right:
                        # 元素都为整数
                        count += record[left] - record[right + 1]
            # record[i]记录了arr[:j]中大于等于i的元素数目
            for k in range(arr[j] + 1):
                record[k] += 1
        return count
```

```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        
        for j in range(n):
            # 收集左边的符合条件的元素并排序
            left_list = []
            for i in range(j):
                if abs(arr[i] - arr[j]) <= a:
                    left_list.append(arr[i])
            left_list.sort()
            
            # 收集右边的符合条件的元素并排序
            right_list = []
            for k in range(j + 1, n):
                if abs(arr[k] - arr[j]) <= b:
                    right_list.append(arr[k])
            right_list.sort()
            
            # 统计满足条件的三元组数目
            current = 0
            if len(left_list) <= len(right_list):
                for x in left_list:
                    lower = x - c
                    upper = x + c
                    left = bisect.bisect_left(right_list, lower)
                    right = bisect.bisect_right(right_list, upper)
                    current += right - left
            else:
                for y in right_list:
                    lower = y - c
                    upper = y + c
                    left = bisect.bisect_left(left_list, lower)
                    right = bisect.bisect_right(left_list, upper)
                    current += right - left
            count += current
        
        return count
```
