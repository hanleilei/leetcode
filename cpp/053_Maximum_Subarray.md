# Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle

对于此类一纬的动态规划题目可以参考下面注释中的状态转移方程：

时间复杂度是O(n), 空间复杂度O(n)
```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // nums [-2,1,-3, 4,-1,2,1,-5,4]
        // f    [-2,1,-2, 4, 3,5,6,1,5]

        // f[i] // maxSubArray(0...i)
        // f[i] = f[i-1] > 0 ? nums[i] + f[i-1] : nums[i]
        vector<int> f(nums.size());
        f[0] = nums[0];
        for(int i = 1; i<nums.size(); ++i)
            f[i] = max(f[i-1] + nums[i], nums[i]);

        return *std::max_element(f.begin(), f.end());
    }
};
```

下面是一个O(1)空间复杂度的方法：

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // nums [-2,1,-3, 4,-1,2,1,-5,4]
        // f    [-2,1,-2, 4, 3,5,6,1,5]

        // f[i] // maxSubArray(0...i)
        // f[i] = f[i-1] > 0 ? nums[i] + f[i-1] : nums[i]
        int sum = nums[0];
        int ans = nums[0];
        for(int i = 1; i<nums.size(); ++i){
            sum = max(sum + nums[i], nums[i]);
            if (sum > ans) ans = sum;
        }
        return ans;
    }
};
```
