# Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle

以下解释来自于这个链接：http://blog.csdn.net/linhuanmars/article/details/21314059
这是一道非常经典的动态规划的题目，用到的思路我们在别的动态规划题目中也很常用，以后我们称为”局部最优和全局最优解法“。

基本思路是这样的，在每一步，我们维护两个变量，一个是全局最优，就是到当前元素为止最优的解是，一个是局部最优，就是必须包含当前元素的最优的解。接下来说说动态规划的递推式（这是动态规划最重要的步骤，递归式出来了，基本上代码框架也就出来了）。假设我们已知第i步的global[i]（全局最优）和local[i]（局部最优），那么第i+1步的表达式是：

local[i+1]=Math.max(A[i], local[i]+A[i]

就是局部最优是一定要包含当前元素，所以不然就是上一步的局部最优local[i]+当前元素A[i]（因为local[i]一定包含第i个元素，所以不违反条件），但是如果local[i]是负的，那么加上他就不如不需要的，所以不然就是直接用A[i]：

global[i+1]=Math(local[i+1],global[i])

有了当前一步的局部最优，那么全局最优就是当前的局部最优或者还是原来的全局最优（所有情况都会被涵盖进来，因为最优的解如果不包含当前元素，那么前面会被维护在全局最优里面，如果包含当前元素，那么就是这个局部最优）。

接下来我们分析一下复杂度，时间上只需要扫描一次数组，所以时间复杂度是O(n)。空间上我们可以看出表达式中只需要用到上一步local[i]和global[i]就可以得到下一步的结果，所以我们在实现中可以用一个变量来迭代这个结果，不需要是一个数组，也就是如程序中实现的那样，所以空间复杂度是两个变量（local和global），即O(2)=O(1)。

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

另外，还有一个方法，还是DP，来自于这个链接：http://www.tuicool.com/articles/IbiMjaI

如果看过Mark Allen Weiss写的数据结构与算法分析一书，可以发现是第二章为了介绍算法的魅力，逐步从三次方的时间复杂度一直优化到线性时间复杂度的一个例子。有一点小区别，就是书中给的例子简化了，如果全为负数，则认为最大子序列和为0，所以有一点点出入，不过基本思路是完全一样的。

现在对线性时间解法做一下解释，属于一种DP问题。已知了前k个元素的最大子序列和为maxSub（已经被记录下来了），以及一个临时和sum，如果添加了第k+1这个元素，由于是连续子序列这个限制，所以如果k+1这个元素之前的和是小于0的，那么对于增大k+1这个元素从而去组成最大子序列是没有贡献的，所以可以把sum 置0。举个例子，-1， -2 ，4， -5， 7这里假定7为第k+1个元素，那么很明显可以看出，之前的sum = -5 + 4 =-1，那么这样对于7来说只会减少它，所以直接置sum = 0， 0 + 7才能得到正确的答案。再拓展这个数组， -1， -2， 4， -5， 7， 1 这里1之前的sum = 7 > 0，对于后面的1来组成最大子序列是有贡献的，所以sum = 7 + 1 =8。再注意一点，只要sum不减到负数，中间出现小于0的元素是没关系的，sum仍然可以继续累加。

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
这两个算法可以说的上是大同小异。下面在看一个Kadane 算法，来自于这个链接：http://blog.csdn.net/joylnwang/article/details/6859677

对于一个包含负值的数字串array[1...n]，要找到他的一个子串array[i...j]（0<=i<=j<=n），使得在array的所有子串中，array[i...j]的和最大。

这里我们需要注意子串和子序列之间的区别。子串是指数组中连续的若干个元素，而子序列只要求各元素的顺序与其在数组中一致，而没有连续的要求。对于一个元素数为n的数组，其含有2^n个子序列和n(n+1)/2个子串。如果使用穷举法，则至少需要O(n^2)的时间才能得到答案。卡耐基梅隆大学的Jay Kadane的给出了一个线性时间算法，我们就来看看，如何在线性时间内解决最大子串和问题。

要说明Kadane算法的正确性，需要两个结论。首先，对于array[1...n]，如果array[i...j]就是满足和最大的子串，那么对于任何k(i<=k<=j)，我们有array[i...k]的和大于0。因为如果存在k使得array[i...k]的和小于0，那么我们就有array[k+1...j]的和大于array[i...j]，这与我们假设的array[i...j]就是array中和最大子串矛盾。

其次，我们可以将数组从左到右分割为若干子串，使得除了最后一个子串之外，其余子串的各元素之和小于0，且对于所有子串array[i...j]和任意k（i<=k<j），有array[i...k]的和大于0。此时我们要说明的是，满足条件的和最大子串，只能是上述某个子串的前缀，而不可能跨越多个子串。我们假设array[p...q]，是array的和最大子串，且array[p...q]，跨越了array[i...j]，array[j+1...k]。根据我们的分组方式，存在i<=m<j使得array[i...m]的和是array[i...j]中的最大值，存在j+1<=n<k使得array[j+1...n]的和是array[j+1...k]的最大值。由于array[m+1...j]使得array[i...j]的和小于0。此时我们可以比较array[i...m]和array[j+1...n]，如果array[i...m]的和大于array[j+1...n]则array[i...m]>array[p...q]，否array[j+1...n]>array[p...q]，无论谁大，我们都可以找到比array[p...q]和更大的子串，这与我们的假设矛盾，所以满足条件的array[p...q]不可能跨越两个子串。对于跨越更多子串的情况，由于各子串的和均为负值，所以同样可以证明存在和更大的非跨越子串的存在。对于单元素和最大的特例，该结论也适用。

根据上述结论，我们就得到了Kadane算法的执行流程，从头到尾遍历目标数组，将数组分割为满足上述条件的子串，同时得到各子串的最大前缀和，然后比较各子串的最大前缀和，得到最终答案。我们以array={−2, 1, −3, 4, −1, 2, 1, −5, 4}为例，来简单说明一下算法步骤。通过遍历，可以将数组分割为如下3个子串（-2），（1，-3），（4，-1，2，1，-5，4），这里对于（-2）这样的情况，单独分为一组。各子串的最大前缀和为-2，1，6，所以目标串的最大子串和为6。


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

肯定还有其他方法实现，divide and conquer肯定也可以实现，复杂度应该是nlogn，后续在更新吧。

再加上一个速度超级快的python版本：

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
