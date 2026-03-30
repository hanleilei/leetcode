# Check if Strings Can be Made Equal With Operations II

You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

    Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.

Return true if you can make the strings s1 and s2 equal, and false otherwise.

Example 1:

Input: s1 = "abcdba", s2 = "cabdab"
Output: true
Explanation: We can apply the following operations on s1:

- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

Example 2:

Input: s1 = "abe", s2 = "bea"
Output: false
Explanation: It is not possible to make the two strings equal.

Constraints:

    n == s1.length == s2.length
    1 <= n <= 10^5
    s1 and s2 consist only of lowercase English letters.

直接用昨天的代码就能ac，昨天的代码是针对第一题的，第一题的条件更严格，所以第二题也满足条件。

```python
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
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
