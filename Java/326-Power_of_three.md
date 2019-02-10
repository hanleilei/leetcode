# Power of three

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

###### 不用循环和迭代，但是需要理解math库的pow函数和log函数的使用方法


```java
class Solution {
    public boolean isPowerOfThree(int n) {
        if (n <= 0) {
            return false;
        } else {
            return Integer.toString(n, 3).matches("10*");
        }
    }
}
```
