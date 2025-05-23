# container with most water

[[greedy]]

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

有个高度数组，就相当于隔板的高度，求数组中任意两隔板间盛水的最大量。隔板间的距离与较低隔板的高度乘积即为盛水的容量。这个有点像是贪心法

```java
class Solution {
    public int maxArea(int[] height) {
        int n = height.length;
        int res = 0;
        for (int i = 0, j = n - 1; i < j;) {
            res = Math.max(res, Math.min(height[i], height[j]) * (j - i));
            if (height[i] < height[j]) {
                i++;
            } else {
                j--;
            }
        }
        return res;
    }
}
```

套路都一样

```java
class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        for (int i = 0, j = height.length - 1; i < j;){
            int minHeight = height[i] < height[j] ? height[i++]: height[j--];
            max = Math.max(max, (j - i + 1 ) * minHeight);
        }
        return max;
    }
}
```
