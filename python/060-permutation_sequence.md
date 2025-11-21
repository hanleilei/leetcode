# permutation sequence

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive

## 方法

首先是要生成所需要的字符串，然后用itertools模块中的方法生成所要的序列。
最后要注意的是，可能所生成的字符串，一定要用迭代的方式，这样很节省时间，否则总是超时。

```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from itertools import permutations
        s = ''
        k = k-1
        count = 0
        for i in range(1,n+1):
            s+= str(i)
        for i in permutations(s,n):
            if count == k:
                return ''.join(i)
            else:
                count += 1
```



```cpp
class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> fact(n, 1);
        for (int i = 1; i < n; i++){
            fact[i] = fact[i-1] * i;
        }
        string ans;
        k--;
        vector<bool> used(n);
        for (int i = n - 1; i >= 0; i--){
            int idx = k / fact[i];
            int digit = 0;
            for (int cnt = 0; ; digit ++){
                if (used[digit]) continue;
                if (idx == cnt++) break;
            }
            ans += (digit + '1');
            used[digit] = true;
            k %= fact[i];
        }
        return ans;
    }
};
```

```cpp
class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> fact(n, 1);
        // for (int i = 1; i < n; i++){
        //     fact[i] = fact[i-1] * i;
        // }
        iota(fact.begin() + 1, fact.end(), 1);
        // 1,1,2,3,4,5
        partial_sum(fact.begin(), fact.end(), fact.begin(), multiplies<int>());
        // 1,1,2,6,24,120
        string ans;
        k--;
        vector<bool> used(n);
        for (int i = n - 1; i >= 0; i--){
            int idx = k / fact[i];
            // int digit = 0;
            // for (int cnt = 0; ; digit ++){
            //     if (used[digit]) continue;
            //     if (idx == cnt++) break;
            // }
            int digit = find_if(used.begin(), used.end(), [&,cnt=0](bool used) mutable{
                return !used && idx == cnt++;
            }) - used.begin();
            ans += (digit + '1');
            used[digit] = true;
            k %= fact[i];
        }
        return ans;
    }
};
```

```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        使用数学方法（康托展开）直接计算第k个排列
        
        时间复杂度：O(n²)
        空间复杂度：O(n)
        """
        # 计算阶乘表：fact[i] = i!
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i-1] * i
        
        ans = ""
        k -= 1  # 转换为0-indexed
        used = [False] * n  # 标记数字是否已使用
        
        # 从高位到低位确定每一位数字
        for i in range(n - 1, -1, -1):
            # 计算当前位应该选择第几个未使用的数字
            idx = k // fact[i]
            
            # 找到第idx个未使用的数字
            digit = 0
            cnt = 0
            while True:
                if not used[digit]:
                    if idx == cnt:
                        break
                    cnt += 1
                digit += 1
            
            # 添加到结果，标记为已使用
            ans += str(digit + 1)  # +1因为数字从1开始
            used[digit] = True
            
            # 更新k为剩余部分的索引
            k %= fact[i]
        
        return ans
```