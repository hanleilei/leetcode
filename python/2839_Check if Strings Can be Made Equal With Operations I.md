# Check if Strings Can be Made Equal With Operations I

You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

    Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.

Return true if you can make the strings s1 and s2 equal, and false otherwise.

Example 1:

Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: We can do the following operations on s1:

- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
- Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.

Example 2:

Input: s1 = "abcd", s2 = "dacb"
Output: false
Explanation: It is not possible to make the two strings equal.

Constraints:

    s1.length == s2.length == 4
    s1 and s2 consist only of lowercase English letters.

其实就是判断奇数位和偶数位的字符是否相同，顺序不重要，所以可以用哈希表或者计数器来统计每个位置的字符出现的次数，最后比较即可。

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even, odd = defaultdict(int), defaultdict(int)

        for i, v in enumerate(s1):
            if i % 2 == 0:
                even[v] += 1
            else:
                odd[v] += 1

        for i, v in enumerate(s2):
            if i % 2 == 0:
                if v not in even or even[v] <= 0:
                    return False
                even[v] -= 1
            else:
                if v not in odd or odd[v] <= 0:
                    return False
                odd[v] -= 1
        return True
```

单行：

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
```

扩展一下，如果是任意长度的字符串，那么我们只需要判断每个位置的字符出现的次数是否相同即可：

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        k=2 #为测试本题库用
        return all(s2[i::k] in s1[i::k]*2 for i in range(k))
```
