# next permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

思路和cpp的版本不是非常的一致：
1. 两两相比，找到最后一个递增的子序列，返回左边的位置k
2. 如果是递减的序列，则直接求逆序
3. 从k的下一个元素开始，遍历，找到最后一个大于位置k的值，位置为l
4. 交换位置k和位置l的值。
5. 对于位置k之后的值求逆序。

```python
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n=nums.size(),k,l;
        for(k=n-2;k>=0;k--)
        {
            if(nums[k]<nums[k+1])
                break;
        }
        if(k<0)
            reverse(nums.begin(),nums.end());
        else
        {
            for(l=n-1;l>k;l--)
            {
                if(nums[l]>nums[k])
                    break;
            }
            swap(nums[k],nums[l]);
            reverse(nums.begin()+k+1,nums.end());
        }

    }
};
```
或者：

```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        next_permutation(nums.begin(),nums.end());
    }
};
```
