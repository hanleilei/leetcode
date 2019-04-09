# camelcase matching

A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.



#### Example 1:
```
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation:
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
```

#### Example 2:
```
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation:
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
```

#### Example 3:
```
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation:
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
````

#### Note:

1. 1 <= queries.length <= 100
2. 1 <= queries[i].length <= 100
3. 1 <= pattern.length <= 100
4. All strings consists only of lower and upper case English letters.

这个问题化简为两个问题：
1. 假定两个query和pattern中的大写字母都一样。
2. 假定pattern是query的子序列。

```python
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # 保留大写字母
        def u(s):
            return [c for c in s if c.isupper()]

        def issup(s, t):
            it = iter(t)
            return all(c in it for c in s)
        return [u(pattern) == u(q) and issup(pattern, q) for q in queries]
```

再来一个作弊的方法：

```python
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [re.match("^[a-z]*" + "[a-z]*".join(pattern) + "[a-z]*$", q) != None for q in queries]
```
