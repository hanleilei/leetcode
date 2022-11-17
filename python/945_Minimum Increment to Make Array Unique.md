# Minimum Increment to Make Array Unique

You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

```
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
```

Example 2:

```
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
```

Constraints:

```
1 <= nums.length <= 105
0 <= nums[i] <= 105
```

继续膜拜 lee215 的方案

## Solution 1: Just Sort, O(NlogN)

Sort the input array.
Compared with previous number,
the current number need to be at least prev + 1.

Time Complexity: O(NlogN) for sorting
Space: O(1) for in-space sort

Note that you can apply "O(N)" sort in sacrifice of space.
Here we don't talk further about sort complexity.

```cpp
    int minIncrementForUnique(vector<int>& A) {
        sort(A.begin(), A.end());
        int res = 0, need = 0;
        for (int a: A) {
            res += max(need - a, 0);
            need = max(a, need)+1;
        }
        return res;
    }
```

```Java
    public int minIncrementForUnique(int[] A) {
        Arrays.sort(A);
        int res = 0, need = 0;
        for (int a : A) {
            res += Math.max(need - a, 0);
            need = Math.max(a, need) + 1;
        }
        return res;
    }
```

```Python
    def minIncrementForUnique(self, A):
        res = need = 0
        for i in sorted(A):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res
```

## Solution 2, O(KlogK)

Same idea as solution 1 above.
But instead of assign value one by one,
we count the input numbers first, and assign values to all same value at one time.

This solution has only O(N) time for cases like [1,1,1,1,1,1,.....]

Time Complexity:
O(NlogK) using TreeMap in C++/Java
O(N + KlogK) using HashMap in Python
Space: O(K) for in-space sort

```C++:

    int minIncrementForUnique(vector<int>& A) {
        map<int,int> count;
        for (int a : A) count[a]++;
        int res = 0, need = 0;
        for (auto x: count) {
            res += x.second * max(need - x.first, 0) + x.second * (x.second - 1) / 2;
            need = max(need, x.first) + x.second;
        }
        return res;
    }
```

```Java:

    public int minIncrementForUnique(int[] A) {
        TreeMap<Integer, Integer> count = new TreeMap<>();
        for (int a : A) count.put(a, count.getOrDefault(a, 0) + 1);
        int res = 0, need = 0;
        for (int x: count.keySet()) {
            int v = count.get(x);
            res += v * Math.max(need - x, 0) + v * (v - 1) / 2;
            need = Math.max(need, x) + v;
        }
        return res;
    }
```

```Python:

    def minIncrementForUnique(self, A):
        c = collections.Counter(A)
        res = need = 0
        for x in sorted(c):
            res += c[x] * max(need - x, 0) + c[x] * (c[x] - 1) / 2
            need = max(need, x) + c[x]
        return res
```

## Solution 3: Union Find, O(N)

Time: Amortized O(N)
Space: O(N)

```C++

    unordered_map<int, int> root;
    int minIncrementForUnique(vector<int>& A) {
        int res = 0;
        for (int a : A)
            res += find(a) - a;
        return res;
    }
    int find(int x) {
        return root[x] = root.count(x) ? find(root[x] + 1) : x;
    }
```

```Python

    def minIncrementForUnique(self, A):
        root = {}
        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]
        return sum(find(a) - a for a in A)
```
