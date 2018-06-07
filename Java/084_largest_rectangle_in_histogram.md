# largest rectangle in histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

![](https://leetcode.com/static/images/problemset/histogram.png)

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

![](https://leetcode.com/static/images/problemset/histogram_area.png)


The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:
```
Input: [2,1,5,6,2,3]
Output: 10
```



```java
public class LargestRectangleHistogram{
    public int largestRectangleArea(int[] heights){
        if (heights == null || heights.length == 0) return 0;
        Stack<integer> stack = new stack<>();
        int res = 0;
        for(int i = 0; i <= heights.length; i++){
            int h = i == heights.length? 0:heights[i];
            whiel(!stack.isEmpty() && h < heights[stack.peek()]){
                int height = heights[stack.pop()];
                int start = stack.isEmpty() ? -1: stack.peek();
                int area = height * (i-start -1);
                res = Math.max(res, area);
            }
            return res;
        }
    }
}
```
