# Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

### 略蛋疼，实在是不喜欢有这样的溢出限定。。

```java
public class Solution {
    public int reverse(int x){
        long res = 0;
        int sign = x > 0 ? 1 : -1;
        long xo = x;

        if (sign == -1){
            xo = xo * -1;
        }

        while (xo > 0){
            long digit = xo % 10;
            res = res * 10 + digit;
            if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE){
                return 0;
            }
            xo = xo / 10;
        }
        return (int)(res * sign);
    }
}
```

下面是最快的算法

```java
public class Solution {
    public int reverse(int x) {
        long res = 0;
        while(x != 0){
            int b = x%10;
            x = x/10;
            res = res*10 + b;
            if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE){
                return 0;
            }
        }
        return (int)res;
    }
}
```
