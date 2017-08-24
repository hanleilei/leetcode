# Power of two

Given an integer, write a function to determine if it is a power of two.

#### 思路和python的一样，就是看与运算。

```java
class Solution {
    public boolean isPowerOfTwo(int n) {
        return (n > 0) & ((n & (n -1)) == 0);
    }
}

```
当然还有一种稍微复杂一点的写法。

```java
public class Solution{
    public boolean isPowerOfTwo(int n){
        if (n <= 0){
            return false;
        }

        int oneBitCount = 0;
        for (int i = 0; i < 32; i++){
            if ((n & 1) == 1){
                oneBitCount++;
            }
            n = n>> 1;
        }
        return oneBitCount == 1;
    }
}

```
