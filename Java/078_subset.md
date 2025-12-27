# subset

[[dfs]] [[backtracking]]

Given an integer array nums of unique elements, return all possible

(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.

If nums = [1,2,3], a solution is:

```
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        if (nums == null) {return ans;}
        dfs(ans, nums, new ArrayList<Integer>(), 0);
        return ans;
    }

    private void dfs(List<List<Integer>> ans, int[] nums, List<Integer> list, int index){
        // terminator
        if (index == nums.length){
            ans.add(new ArrayList<Integer>(list));
            return;
        }
        dfs(ans, nums, list, index + 1);
        list.add(nums[index]);
        dfs(ans, nums, list, index + 1);

        // restore state
        list.remove(list.size() - 1);
    }
}
```
