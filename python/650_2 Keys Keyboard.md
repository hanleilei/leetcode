# 2 Keys Keyboard

There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

## Example 1

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

## Example 2

```text
Input: n = 1
Output: 0
```

Constraints:

1 <= n <= 1000

第一先到的就是一维的DP问题：

```python
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(2, n+1):
            dp[i] = i
            for j in range(i-1, 1, -1):
                # if sequence of length 'j' can be pasted multiple times to get length 'i' sequence
                if i % j == 0:
                    # we just need to paste sequence j (i/j - 1) times, hence additional (i/j) times since we need to copy it first as well.
                    # we don't need checking any smaller length sequences 
                    dp[i] = dp[j] + i // j
                    break
        return dp[n]
```

```python
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n = n//d
            d += 1
        return ans
```

```java
class Solution {
    public int minSteps(int n) {
        int ans = 0;
        int d = 2;
        while (n > 1){
            while (n % d == 0) {
                ans += d;
                n = n / d;
            }
            d += 1;
        }
        return ans;
    }
}
```

```cpp
class Solution {
public:
    int minSteps(int n) {
        int ans = 0;
        int d = 2;
        while (n > 1){
            while (n % d == 0) {
                ans += d;
                n = n / d;
            }
            d++;
        }
        return ans;
    }
};
```

```golang
func minSteps(n int) int {
    d := 2
    sum := 0
    for n > 1 {
        for n % d == 0 {
            sum+= d
            n /= d
        }
        d++
    }
    return sum
}
```

```rust
impl Solution {
    pub fn min_steps(n: i32) -> i32 {
        let mut n = n;
        let mut ans = 0;
        let mut d = 2;

        while n > 1 {
            while n % d == 0{
                ans += d;
                n /= d;
            }
            d += 1;
        }
        ans
    }
}
```
