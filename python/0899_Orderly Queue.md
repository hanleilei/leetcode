# Orderly Queue

You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

Example 1:

```
Input: s = "cba", k = 1
Output: "acb"
```

Explanation:

```
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
```

Example 2:

```
Input: s = "baaca", k = 3
Output: "aaabc"
```

Explanation:

```
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
```

Constraints:

```
1 <= k <= s.length <= 1000
s consist of lowercase English letters.
```

来看看 lee215 的思路和方案，把我的智商按在地上摩擦。。

Intuition:
First, this is string rotation.
12345 -> 23451 -> 34512 -> 45123 -> 51234
I use number instead of letters to make it clear.

If K == 1, we can only rotate the whole string.
There are S.length different states and
we return the lexicographically smallest string.

If K > 1, it means we can:

rotate the whole string,
rotate the whole string except the first letter.
012345 -> 023451 -> 034512 -> 045123 -> 051234
We can rotate i+1th big letter to the start (method 1),
then rotate ith big letter to the end (method 2).
2XXX01 -> XXX012

In this way, we can bubble sort the whole string lexicographically.
So just return sorted string.

```python
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        return "".join(sorted(S)) if K > 1 else min(S[i:] + S[:i] for i in range(len(S)))
```

```java
    public String orderlyQueue(String S, int K) {
        if (K > 1) {
            char S2[] = S.toCharArray();
            Arrays.sort(S2);
            return new String(S2);
        }
        String res = S;
        for (int i = 1; i < S.length(); i++) {
            String tmp = S.substring(i) + S.substring(0, i);
            if (res.compareTo(tmp) > 0) res = tmp;
        }
        return res;
    }
```

```cpp
    string orderlyQueue(string S, int K) {
        if (K > 1) {
            sort(S.begin(), S.end());
            return S;
        }
        string res = S;
        for (int i = 1; i < S.length(); i++)
            res = min(res, S.substr(i) + S.substr(0, i));
        return res;
    }
```
