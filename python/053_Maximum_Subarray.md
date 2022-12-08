# Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle

以下解释来自于这个链接：http://blog.csdn.net/linhuanmars/article/details/21314059
这是一道非常经典的动态规划的题目，用到的思路我们在别的动态规划题目中也很常用，以后我们称为”局部最优和全局最优解法“。

基本思路是这样的，在每一步，我们维护两个变量，一个是全局最优，就是到当前元素为止最优的解是，一个是局部最优，就是必须包含当前元素的最优的解。接下来说说动态规划的递推式（这是动态规划最重要的步骤，递归式出来了，基本上代码框架也就出来了）。假设我们已知第 i 步的 global[i]（全局最优）和 local[i]（局部最优），那么第 i+1 步的表达式是：

local[i+1]=Math.max(A[i], local[i]+A[i]

就是局部最优是一定要包含当前元素，所以不然就是上一步的局部最优 local[i]+当前元素 A[i]（因为 local[i]一定包含第 i 个元素，所以不违反条件），但是如果 local[i]是负的，那么加上他就不如不需要的，所以不然就是直接用 A[i]：

global[i+1]=Math(local[i+1],global[i])

有了当前一步的局部最优，那么全局最优就是当前的局部最优或者还是原来的全局最优（所有情况都会被涵盖进来，因为最优的解如果不包含当前元素，那么前面会被维护在全局最优里面，如果包含当前元素，那么就是这个局部最优）。

接下来我们分析一下复杂度，时间上只需要扫描一次数组，所以时间复杂度是 O(n)。空间上我们可以看出表达式中只需要用到上一步 local[i]和 global[i]就可以得到下一步的结果，所以我们在实现中可以用一个变量来迭代这个结果，不需要是一个数组，也就是如程序中实现的那样，所以空间复杂度是两个变量（local 和 global），即 O(2)=O(1)。

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        gb = nums[0]
        local = nums[0]
        for i in range(1, len(nums)):
            local = max(nums[i], local + nums[i])
            gb = max(local, gb)
        return gb
```

另外，还有一个方法，还是 DP，来自于这个链接：http://www.tuicool.com/articles/IbiMjaI

如果看过 Mark Allen Weiss 写的数据结构与算法分析一书，可以发现是第二章为了介绍算法的魅力，逐步从三次方的时间复杂度一直优化到线性时间复杂度的一个例子。有一点小区别，就是书中给的例子简化了，如果全为负数，则认为最大子序列和为 0，所以有一点点出入，不过基本思路是完全一样的。

现在对线性时间解法做一下解释，属于一种 DP 问题。已知了前 k 个元素的最大子序列和为 maxSub（已经被记录下来了），以及一个临时和 sum，如果添加了第 k+1 这个元素，由于是连续子序列这个限制，所以如果 k+1 这个元素之前的和是小于 0 的，那么对于增大 k+1 这个元素从而去组成最大子序列是没有贡献的，所以可以把 sum 置 0。举个例子，-1， -2 ，4， -5， 7 这里假定 7 为第 k+1 个元素，那么很明显可以看出，之前的 sum = -5 + 4 =-1，那么这样对于 7 来说只会减少它，所以直接置 sum = 0， 0 + 7 才能得到正确的答案。再拓展这个数组， -1， -2， 4， -5， 7， 1 这里 1 之前的 sum = 7 > 0，对于后面的 1 来组成最大子序列是有贡献的，所以 sum = 7 + 1 =8。再注意一点，只要 sum 不减到负数，中间出现小于 0 的元素是没关系的，sum 仍然可以继续累加。

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            if sum < 0:
                sum = 0
            sum += nums[i]
            maxSum = max(maxSum, sum)
        return maxSum
```

这两个算法可以说的上是大同小异。下面在看一个 Kadane 算法，来自于这个链接：http://blog.csdn.net/joylnwang/article/details/6859677

对于一个包含负值的数字串 array[1...n]，要找到他的一个子串 array[i...j]（0<=i<=j<=n），使得在 array 的所有子串中，array[i...j]的和最大。

这里我们需要注意子串和子序列之间的区别。子串是指数组中连续的若干个元素，而子序列只要求各元素的顺序与其在数组中一致，而没有连续的要求。对于一个元素数为 n 的数组，其含有 2^n 个子序列和 n(n+1)/2 个子串。如果使用穷举法，则至少需要 O(n^2)的时间才能得到答案。卡耐基梅隆大学的 Jay Kadane 的给出了一个线性时间算法，我们就来看看，如何在线性时间内解决最大子串和问题。

要说明 Kadane 算法的正确性，需要两个结论。首先，对于 array[1...n]，如果 array[i...j]就是满足和最大的子串，那么对于任何 k(i<=k<=j)，我们有 array[i...k]的和大于 0。因为如果存在 k 使得 array[i...k]的和小于 0，那么我们就有 array[k+1...j]的和大于 array[i...j]，这与我们假设的 array[i...j]就是 array 中和最大子串矛盾。

其次，我们可以将数组从左到右分割为若干子串，使得除了最后一个子串之外，其余子串的各元素之和小于 0，且对于所有子串 array[i...j]和任意 k(i<=k<j)，有 array[i...k]的和大于 0. 此时我们要说明的是，满足条件的和最大子串，只能是上述某个子串的前缀，而不可能跨越多个子串。我们假设 array[p...q]，是 array 的和最大子串，且 array[p...q]，跨越了 array[i...j]，array[j+1...k]。根据我们的分组方式，存在 i<=m<j 使得 array[i...m]的和是 array[i...j]中的最大值，存在 j+1<=n<k 使得 array[j+1...n]的和是 array[j+1...k]的最大值。由于 array[m+1...j]使得 array[i...j]的和小于 0。此时我们可以比较 array[i...m]和 array[j+1...n]，如果 array[i...m]的和大于 array[j+1...n]则 array[i...m]>array[p...q]，否 array[j+1...n]>array[p...q]，无论谁大，我们都可以找到比 array[p...q]和更大的子串，这与我们的假设矛盾，所以满足条件的 array[p...q]不可能跨越两个子串。对于跨越更多子串的情况，由于各子串的和均为负值，所以同样可以证明存在和更大的非跨越子串的存在。对于单元素和最大的特例，该结论也适用。

根据上述结论，我们就得到了 Kadane 算法的执行流程，从头到尾遍历目标数组，将数组分割为满足上述条件的子串，同时得到各子串的最大前缀和，然后比较各子串的最大前缀和，得到最终答案。我们以 array={−2, 1, −3, 4, −1, 2, 1, −5, 4}为例，来简单说明一下算法步骤。通过遍历，可以将数组分割为如下 3 个子串（-2），（1，-3），（4，-1，2，1，-5，4），这里对于（-2）这样的情况，单独分为一组。各子串的最大前缀和为-2，1，6，所以目标串的最大子串和为 6。

```cpp
int Kadane(const int array[], size_t length, unsigned int& left, unsigned int& right)
{
    unsigned int i, cur_left, cur_right;
    int cur_max, max;

    cur_max = max = left = right = cur_left = cur_right = 0;

    for(i = 0; i < length; ++i)
    {
        cur_max += array[i];

        if(cur_max > 0)
        {
            cur_right = i;

            if(max < cur_max)
            {
                max = cur_max;
                left = cur_left;
                right = cur_right;
            }
        }
        else
        {
            cur_max = 0;
            cur_left = cur_right = i + 1;
        }
    }

    return max;
}

```

这个算法没看懂怎么弄的，见笑了。

再加上一个速度超级快的 python 版本：

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lo = psum = 0
        max_psum = nums[0]
        for i in nums:
            psum += i
            max_psum = max(psum - lo, max_psum)
            lo = min(lo, psum)
        return max_psum
```

类似的变体：

```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)
```

```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import functools

        return functools.reduce(lambda r, x: (max(r[0], r[1]+x), max(r[1]+x,x)), nums, (max(nums), 0))[0]
```

```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        local = total = nums[0]
        for i in range(1, len(nums)):
            local = max(nums[i],  nums[i] + local)
            total = max(local, total)
        return total
```

再来一个和上面方法相似的：

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = max_val = nums[0]
        for i in range(1, len(nums)):
            localMax = max(nums[i], localMax + nums[i])
            max_val = max(max_val, localMax)
        return max_val
```

上面的方法是通过 Kadane 算法实现，参考这个链接：https://zhuanlan.zhihu.com/p/96014673

速度快的版本来一个：

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi, suma = 0, 0
        for elem in nums:
            suma += elem
            if maxi < suma:
                maxi = suma
            if suma < 0:
                suma = 0
        return maxi if maxi > 0 else max(nums)
```

下面更新一个 divide & conquer 的方法：

```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)
```

速度很慢，还是动态规划比较合适。
