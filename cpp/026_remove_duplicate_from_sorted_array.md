# remove duplicate from sorted array

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

##### 使用一个指针j，当i向后遍历数组时，如果遇到与A[j]不同的，将A[i]和A[j+1]交换，同时j=j+1，即j向后移动一个位置，然后i继续向后遍历

```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int index = 0;
        for (int i = 0; i < nums.size(); i++){
            if(nums[index] != nums[i]){
                nums[++index] = nums[i];
            }
        }
        return index + 1;
    }
};        
```
还可以用stl实现：

```c++
class Solution{
    int removeDuplicates(vector<int>& nums){
        return distance(nums.begin(), unique(nums.begin(), nums.end()));
    }
}
```
