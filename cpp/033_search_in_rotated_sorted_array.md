# search in rotated sorted array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

#### stefhan大大的方案。。中间的那一坨算事数组变换
Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

If target is let's say 7, then we adjust nums to this:
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

And then we can simply do ordinary binary search.

Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at. And the adjustment is done by comparing both the target and the actual element against nums[0].

If nums[mid] and target are "on the same side" of nums[0], we just take nums[mid]. Otherwise we use -infinity or +infinity as needed.

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lo = 0, hi = nums.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;

            double num = (nums[mid] < nums[0]) == (target < nums[0])
                       ? nums[mid]
                       : target < nums[0] ? -INFINITY : INFINITY;

            if (num < target)
                lo = mid + 1;
            else if (num > target)
                hi = mid;
            else
                return mid;
        }
        return -1;
    }
};
```

再来个好理解的：

```c++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size();
        while (low != high){
            const int mid = low + (high - low) / 2;
            if (target == nums[mid])
                return mid;

            if (nums[low] < nums[mid]){
                if (nums[low] <= target && target < nums[mid])
                    high = mid;
                else
                    low = mid + 1;
            }
            else{
                if (target <= nums[high -1] && nums[mid] < target)
                    low = mid + 1;
                else
                    high = mid ;

            }
        }
        return -1;
    }
};
```
