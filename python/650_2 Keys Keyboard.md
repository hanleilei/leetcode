# 2 Keys Keyboard

[[dp]]

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

To get the DP solution, analyses the pattern first by generating first few solutions
1: 0
2: 2
3: 3
4: 4
5: 5
6: 5
7: 7
8: 6
9: 6
10: 7
11: 11
12: 7
13: 13
14: 9
15: 8

Now, check the solution.
Eg: n=6
To get 6, we need to copy 3 'A's two time. (2)
To get 3 'A's, copy the 1 'A' three times. (3)
So the answer for 6 is 5

Now, take n=9.
We need the lowest number just before 9 such that (9% number =0). So the lowest number is 3.
So 9%3=0. We need to copy 3 'A's three times to get 9. (3)
For getting 3 'A's, we need to copy 1 'A' three times. (3)
So the answer is 6

Finally to analyses the below code, take n=81.
To get 81 we check
if (81 % 2 ==0) No
if (81 % 3 ==0) Yes
So we need to copy 81/3 = 27 'A's three times (3)
Now to get 27 'A's, we need to copy 27/3= 9 'A's three times (3)
To get 9 'A's, we need to copy 9/3=3 'A's three times (3)
And to get 3 'A's, we need to copy 3/3=1 'A's three times (3)
Final answer is 3+3+3+3 = 12

Last Example, n=18
18/2 = 9 Copy 9 'A's 2 times (2)
9/3=3 Copy 3 'A's 3 times (3)
3/3=1 Copy 1'A's 3 times (3)
Answer: 2+3+3= 8

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
