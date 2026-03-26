# Non-decreasing Subsequences

[[dfs]] [[backtracking]]

Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]

Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100

```python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(idx: int, cur_list: List[int]):
            # 只要当前递增序列长度大于1，就保存到结果中
            if len(cur_list) > 1:
                res.append(cur_list[:])
            
            used = set()  # 用于本层去重
            for i in range(idx + 1, len(nums)):
                if nums[i] in used:
                    continue
                
                used.add(nums[i])
                
                # 如果是起始位置或满足递增条件
                if idx == -1 or nums[i] >= nums[idx]:
                    cur_list.append(nums[i])
                    dfs(i, cur_list)
                    cur_list.pop()  # 回溯
        
        dfs(-1, [])
        return res
```

```java
class Solution {
    // 定义全局变量保存结果
    List<List<Integer>> res = new ArrayList<>();
    
    public List<List<Integer>> findSubsequences(int[] nums) {
        // idx 初始化为 -1，开始 dfs 搜索。
        dfs(nums, -1, new ArrayList<>());
        return res;
    }

    private void dfs(int[] nums, int idx, List<Integer> curList) {
        // 只要当前的递增序列长度大于 1，就加入到结果 res 中，然后继续搜索递增序列的下一个值。
        if (curList.size() > 1) {
            res.add(new ArrayList<>(curList));
        }

        // 在 [idx + 1, nums.length - 1] 范围内遍历搜索递增序列的下一个值。
        // 借助 set 对 [idx + 1, nums.length - 1] 范围内的数去重。
        Set<Integer> set = new HashSet<>();
        for (int i = idx + 1; i < nums.length; i++) {
            // 1. 如果 set 中已经有与 nums[i] 相同的值了，说明加上 nums[i] 后的所有可能的递增序列之前已经被搜过一遍了，因此停止继续搜索。
            if (set.contains(nums[i])) { 
                continue;
            }
            set.add(nums[i]);
            // 2. 如果 nums[i] >= nums[idx] 的话，说明出现了新的递增序列，因此继续 dfs 搜索（因为 curList 在这里是复用的，因此别忘了 remove 哦）
            if (idx == -1 || nums[i] >= nums[idx]) {
                curList.add(nums[i]);
                dfs(nums, i, curList);
                curList.remove(curList.size() - 1);
            }
        }
    }
}
```
