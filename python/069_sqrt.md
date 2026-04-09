# Sqrt(x)

[[binarysearch]]

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:

    0 <= x <= 2^31 - 1

似乎标准库不是一个好的方法，下面用牛顿法：

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        t = x
        while t * t > x:
            t = int(t / 2.0 + x / (2.0 * t))
        return t
```

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)
```

写成递归形式：

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        def sqrts(x):
            res = (x + s / x)/ 2
            if res == x:
                return x
            else:
                return sqrts(res)
        s = x
        if x == 0:
            return 0
        return int(sqrts(x))
```

二分法,把这道题看成 查找右边界，也就是查找最后一个 <= sqrt(x) 的数:

```python
sqrt_max = isqrt(2 ** 31 - 1) 

class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, min(x, sqrt_max) + 1

        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return low - 1
```

或者：

```python
SQRT_MAX = isqrt(2 ** 31 - 1)

class Solution:
    def mySqrt(self, x: int) -> int:
        # 开区间 (left, right)
        left, right = 0, min(x, SQRT_MAX) + 1
        while left + 1 < right:  # 开区间不为空
            # 循环不变量：left^2 <= x
            # 循环不变量：right^2 > x
            m = (left + right) // 2
            if m * m <= x:
                left = m
            else:
                right = m
        # 循环结束时 left+1 == right
        # 此时 left^2 <= x 且 right^2 > x
        # 所以 left 最大的满足 m^2 <= x 的数
        return left
```

按照九章的模板：

```Python
class Solution:
    def sqrt(self, x):        
        start, end, mid = 0, x, x//2

        while start + 1 < end:
            if mid * mid == x:
                start = mid
            elif mid * mid > x:
                end = mid
            else:
                start = mid
            mid = start + (end - start) // 2

        if start * start == x:
            return start
        if end * end == x:
            return end
        return end-1
```

初步总结一个模板：

```cpp
int getLastMatch(int lo, int hi, function<bool(int)>matcher){
    while (lo <= hi){
        int mid = lo + ((hi - lo) >> 1);
        if (matcher(mid)) lo = mid + 1;
        else hi = mid - 1;
    }
    return lo - 1;
}

class Solution {
public:
    int mySqrt(int x) {
        return getLastMatch(0, x, [&](int64_t a){
            return a * a <= x;
        });
    }
};
```

或者：

```cpp
class Solution {
public:
    int mySqrt(int x) {
        int low = 0;
        int high = x;
        int ans;
        while (low <= high){
            int64_t mid = low + (high - low)/2; // 防止溢出
            if (mid * mid > x){
                high = mid - 1;
            }else{
                low = mid + 1;
                ans = mid;
            }
        }
        return ans;
    }
};
```

问题：

1. 这个模板是上界（最后一个满足）二分，如何写下界（第一个满足）二分呢？只需要把matcher的返回值反过来就行了。
2. 这类问题如何抽象，请找出特征：
   - 目标值单调变化
   - 目标值离散
   - 目标值有上下界
   - 目标值可通过函数判断是否满足
   - 目标值需要最后取整
   - 目标值需要找最后一个满足条件的值
