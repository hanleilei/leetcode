## Contains duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

就是看数组中是否有重复的参数，直接用集合的概念搞定

```python
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
```

```python
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
```

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for i in nums:
            if i not in s:
                 s.add(i)
            else:
                return True
        return False
```

```rust
use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let unique_nums: HashSet<i32> = nums.iter().cloned().collect();
        nums.len() != unique_nums.len()
    }
}
```

```go
func containsDuplicate(nums []int) bool {
    nS := make(map[int] struct{})
    for _, num := range nums {
        if _, exists := nS[num]; exists {
            return true
        }
        nS[num] = struct{}{}
    }
    return false
}
```

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> found = new HashSet<>();
        for(final int n : nums){
            if(!found.add(n)){
                return true;
            }
        }
        return false;
    }
}
```

```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n=nums.size();
        sort(nums.begin(),nums.end());
        int left=0;
        int right=1;
        while(right<n){
            if(nums[left]==nums[right]){
                return true;
            }
            left++;
            right++;

        }
        return false;
    }
};
```
