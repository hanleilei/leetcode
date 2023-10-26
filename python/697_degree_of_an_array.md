# Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

Input: `nums = [1,2,2,3,1]`
Output: `2`
Explanation:

```
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
```

Example 2:

Input: `nums = [1,2,2,3,1,4,2]`

Output: `6`
Explanation:

```
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
```

Constraints:

```
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
```

找到度，然后找到满足度条件的最小子数组。
其实就很简单，满足度的条件，一共有几个子数组，他们的最大和最小位置组成的子数组长度，找出最小的。

```python
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_freq = collections.defaultdict(list)
        for i, n in enumerate(nums):
            nums_freq[n].append(i)
        max_degree = len(max(nums_freq.values(), key=len))
        res = float('inf')
        for k, v in nums_freq.items():
            if len(v) == max_degree:
                res = min(res, v[-1] - v[0] + 1)
        return res

```

看看 lee215 的方法：

One pass on A,
For each different number a in A,
we need to count its frequency and it first occurrence index.

If a has the maximum frequency,
update the degree = count[a] and res = i - first[A[i]] + 1.

If a is one of the numbers that has the maximum frequency,
update the res = min(res, i - first[A[i]] + 1)

```Java:

    public int findShortestSubArray(int[] A) {
        Map<Integer, Integer> count = new HashMap<>(), first = new HashMap<>();
        int res = 0, degree = 0;
        for (int i = 0; i < A.length; ++i) {
            first.putIfAbsent(A[i], i);
            count.put(A[i], count.getOrDefault(A[i], 0) + 1);
            if (count.get(A[i]) > degree) {
                degree = count.get(A[i]);
                res = i - first.get(A[i]) + 1;
            } else if (count.get(A[i]) == degree)
                res = Math.min(res, i - first.get(A[i]) + 1);
        }
        return res;
    }
```

```C++:

    int findShortestSubArray(vector<int>& A) {
        unordered_map<int, int> count, first;
        int res = 0, degree = 0;
        for (int i = 0; i < A.size(); ++i) {
            if (first.count(A[i]) == 0) first[A[i]] = i;
            if (++count[A[i]] > degree) {
                degree = count[A[i]];
                res = i - first[A[i]] + 1;
            } else if (count[A[i]] == degree)
                res = min(res, i - first[A[i]] + 1);
        }
        return res;
    }
```

```python
    def findShortestSubArray(self, A):
        first, count, res, degree = {}, {}, 0, 0
        for i, a in enumerate(A):
            first.setdefault(a, i)
            count[a] = count.get(a, 0) + 1
            if count[a] > degree:
                degree = count[a]
                res = i - first[a] + 1
            elif count[a] == degree:
                res = min(res, i - first[a] + 1)
        return res
```

日常智商被按在地上摩擦。。欣慰的是我的方法效率高
