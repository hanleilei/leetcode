# remove element

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Hint:

Try two pointers.
Did you use the property of "the order of elements can be changed"?
What happens when the elements to remove are rare?

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size();
        int ret = 0;
        for(int i = 0; i<size; i++){
            if (nums[i] != val)
                nums[ret++] = nums[i];
        }
        return ret;
    }
};
```
下面的方法是超级牛逼的，只要4ms。。

```cpp
static const auto _____ = []()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        auto cur = 0;

		for(auto i=0; i < nums.size(); i++) {
			if (nums[i] != val) {
				nums[cur] = nums[i];
				cur++;
			}
		}
		return cur;
    }
```
