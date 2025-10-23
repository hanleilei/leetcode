# Lexicographically Smallest String After Applying Operations

[[math]] [[bfs]] [[dfs]]

You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.

You can apply either of the following two operations any number of times and in any order on s:

    Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
    Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".

Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.

 

Example 1:

Input: s = "5525", a = 9, b = 2
Output: "2050"
Explanation: We can apply the following operations:
Start:  "5525"
Rotate: "2555"
Add:    "2454"
Add:    "2353"
Rotate: "5323"
Add:    "5222"
Add:    "5121"
Rotate: "2151"
Add:    "2050"​​​​​
There is no way to obtain a string that is lexicographically smaller than "2050".

Example 2:

Input: s = "74", a = 5, b = 1
Output: "24"
Explanation: We can apply the following operations:
Start:  "74"
Rotate: "47"
​​​​​​​Add:    "42"
​​​​​​​Rotate: "24"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller than "24".

Example 3:

Input: s = "0011", a = 4, b = 2
Output: "0011"
Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".

 

Constraints:

    2 <= s.length <= 100
    s.length is even.
    s consists of digits from 0 to 9 only.
    1 <= a <= 9
    1 <= b <= s.length - 1

看一个纯数学的，具体看灵神的解答吧。懒得敲了。

```python
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # 使用数学的方式解决
        s = list(map(int,s))
        n = len(s)
        step = gcd(b,n)
        g = gcd(a,10)
        ans = [inf] # 方便比较大小

        def modify(start):
            ch = t[start]
            inc = (ch % g - ch) % 10 # 确定第一位达到最小字典序所需要的增幅
            if inc:
                for j in range(start,n,2):
                    t[j] = (t[j] + inc) % 10
        
        for i in range(0,n,step):
            t = s[i:] + s[:i]
            modify(1)
            if step % 2:
                modify(0)
            ans = min(ans,t)
        return "".join(map(str,ans))

```

dfs:

```python
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        # this map holds the new value of every digit after addition by a % 10
        incremented = {str(n):str((n+a)%10) for n in range(10)}

        # function applying the addition operation
        def addOp(s):
            res = ""
            for i in range(n):
                res += s[i] if i % 2 == 0 else incremented[s[i]]
            return res

        # function applying the rotation operation
        def rotOp(s):
            return s[n-b:] + s[:n-b]


        seen = set()
        def dfs(s):
            if s in seen:
                return
            seen.add(s)
            dfs(addOp(s))
            dfs(rotOp(s))
            return

        dfs(s)
        return min(seen)
```

bfs:

```python
        res,q = set(),deque([tuple(map(int,s))])
        while q:
            t = q.pop()
            for t in tuple((d+a)%10 for d,a in zip(t,cycle((0,a)))),t[-b:]+t[:-b]:
                if t not in res: res.add(t);q.append(t)
        
        return ''.join(map(str,min(res)))
```
