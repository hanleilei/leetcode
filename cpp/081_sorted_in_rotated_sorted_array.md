# Search in Rotated Sorted Array II

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates

#### 正常的按照二分法来做。注意会有重复元素.

```cpp
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int first = 0;
        int last = nums.size();
        while (first != last){
            const int mid = first + (last - first) / 2;
            if (nums[mid] == target)
                return true;
            if (nums[first] < nums[mid]){
                if (nums[first] <= target && target < nums[mid])
                    last = mid;
                else
                    first = mid + 1;
            }
            else if (nums[first] > nums[mid]){
                if (nums[mid] < target && target <= nums[last-1])
                    first = mid + 1;
                else
                    last = mid;
            }
            else
                first++; // skip duplicate one
        }
        return false;

    }
};
```
