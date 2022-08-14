## Non-decreasing Array

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

```
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
```

Example 2:

```
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
```

Constraints:

```
n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
```

要用到贪心算法：

```
算法思想
贪心算法

本题是要维持一个非递减的数列，所以遇到递减的情况时（nums[i] > nums[i + 1]），要么将前面的元素缩小，要么将后面的元素放大。

但是本题唯一的易错点就在这，

如果将nums[i]缩小，可能会导致其无法融入前面已经遍历过的非递减子数列；
如果将nums[i + 1]放大，可能会导致其后续的继续出现递减；
所以要采取贪心的策略，在遍历时，每次需要看连续的三个元素，也就是瞻前顾后，遵循以下两个原则：

需要尽可能不放大nums[i + 1]，这样会让后续非递减更困难；
如果缩小nums[i]，但不破坏前面的子序列的非递减性；
算法步骤：

遍历数组，如果遇到递减：
还能修改：
修改方案1：将nums[i]缩小至nums[i + 1]；
修改方案2：将nums[i + 1]放大至nums[i]；
不能修改了：直接返回false；
```

```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True
        flag  = nums[0] <= nums[1]
        # check 3 elements during iteration
        for i in range(1, len(nums) -1):
            if nums[i] > nums[i+1]: #decreasing..
                if flag: # modify if we have chance
                    if nums[i+1] >= nums[i-1]: # condition 1st
                        nums[i] = nums[i+1]
                    else:                      # condition 2nd
                        nums[i + 1] = nums[i]
                    flag = False               # the only chance consumed.
                else:
                    return False               # no chance any more
        return True
```

再来一个更简单的：

```python
The approach that we will be taking is greedy. From the problem statement, it's clear that we have to count the number of violations i.e. nums[i-1]>nums[i].

Input Array - [1, 2, 4, 3]

In above case, we find one violation at index 3. So this is a valid case, as we can make it non-decreasing by just modifying the violation which is

After fixing the violation - [1, 2, 3, 3]

As you can see, I just did nums[i-1]=nums[i] to fix the violation. After fixing the violation, the array is non-decreasing.

Now let's pick an invalid case.

Input Array - [3, 4, 2, 3]

Here if you see, there is only one violation at index 2.

Fixed violation at index 2 - [3, 2, 2, 3]

But after fixing the violation, the array is still not in non-decreasing order. Hence, it's an invalid case. So from this example we can observe that we need to take into account nums[i-2] as well.

Now let's take another example.

Input array - [3, 4, 2]

We find one violation at index 2. Here instead of doing nums[i-1]=nums[i], we do nums[i]=nums[i-1].

resultant array - [3, 4, 4]

From the above details, we can observe the following:

We need the count of violations in the input array. If at any point count > 1, we return False
For any violation, we have to make an additional check for nums[i-2]. If nums[i-2]>nums[i], we perform nums[i]=nums[i-1] to fix the violation.
Taking above things into consideration, below is my implemenation using greeedy.
```

```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt_violations=0
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                if cnt_violations==1:
                    return False
                cnt_violations+=1
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]
        return True
```
