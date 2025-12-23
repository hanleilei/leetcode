# Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

Subscribe to see which companies asked this question

用标准库：

```python
class Solution:
    # @param {integer} x
    # @return {integer}
    import math
    def mySqrt(self, x):
        return int(math.sqrt(x))
```

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

或者二分法：

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high, mid = 0, x, x // 2
        while low <= high:
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) // 2
        return int(mid)
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
int getLastMatch(int lo, int hi, function<bool(int)> matcher){
    while (lo <= hi){
        int mid = (lo + hi) >> 1;
        if (matcher(mid)) lo = mid + 1;
        else hi = mid - 1;
    }
    return lo - 1;
}
```

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

