# remove duplicates from sorted array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question.

```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2) return nums.size();

        int index = 2;
        for(int i = 2; i < nums.size(); i++){
            if (nums[index - 2] != nums[i]){
                nums[index++] = nums[i];
            }
        }
        return index;
    }
};
```

这个是网上的票最多的答案，我是想不出来这么优雅的解答：

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        for (int n : nums)
            if (i < 2 || n > nums[i-2])
                nums[i++] = n;
        return i;
    }
};    
```

下面的这个更简洁。。

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        const int n = nums.size();
        int index = 0;
        for (int i = 0; i < n; ++i){
            if (i > 0 && i < n-1&& nums[i] == nums[i-1]&& nums[i] == nums[i+1])
                continue;
            nums[index++] = nums[i];
        }
        return index;
    }
};    
```
