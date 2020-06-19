# trapping rain water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![](http://www.leetcode.com/static/images/problemset/rainwatertrap.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

```java
class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int lmax = 0;
        int rmax = 0;
        int res = 0;

        while(left < right) {
            if(height[left] < height[right]){
                lmax = Math.max(height[left], lmax);
                res += lmax - height[left];
                left += 1;
            }
            else {
                rmax = Math.max(height[right], rmax);
                res += rmax - height[right];
                right -= 1;
            }
        }
        return res;
    }
}
```
