# trapping rain water

[[MonotonicStack]] [[stack]] [[2points]]

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

## Example 1

![Rainwatertrap image](http://www.leetcode.com/static/images/problemset/rainwatertrap.png)

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

## Example 2

Input: height = [4,2,0,3,2,5]
Output: 9

## Constraints

n == height.length
1 <= n <= 2 * 10**4
0 <= height[i] <= 10**5

谁小先算谁，指针走到哪里记到哪。

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = (int)height.size() - 1;
        int left_max = 0, right_max = 0, ans = 0;
        while (left < right){
            left_max = max(left_max, height[left]);
            right_max = max(right_max, height[right]);
            if (left_max <= right_max){
                ans += left_max - height[left];
                ++left;
            }
            else{
                ans += right_max - height[right];
                --right;
            }
        }
        return ans;
    }
};
```
