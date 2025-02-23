# Generate Parentheses

[[dfs]]

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8

利用递归，注意满足的两个条件：左括号一定要大于零，右括号一定要大于零，且大于左括号的数量

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res=[]  
        tmp=['' for i in range(n+n)]  
        self.generate(res,n,n,tmp,0)  
        return res  

    def generate(self,res,l,r,tmp,index):  
        if l==0 and r==0:  
            res.append(''.join(tmp))  
            return  
        if l>0:  
            tmp[index]='('  
            self.generate(res,l-1,r,tmp,index+1)  
        if r>0 and r>l:  
            tmp[index]=')'  
            self.generate(res,l,r-1,tmp,index+1)  
```

再来看一个backtrack的方案：

```Python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']
        ans = []
        def backtrack(S = '',left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:k
                backtrack(S+'(',left + 1, right)
            if right < left:
                backtrack(S+')',left,right + 1)

        backtrack()
        return ans
```

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()
        self.helper(n, n, "", res)
        return res

    def helper(self, left, right, path, res):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.helper(left - 1, right, path + "(", res)
        if right > 0 and left < right:
            self.helper(left, right - 1, path + ")", res)
```

和一个dp的方案：

To generate all n-pair parentheses, we can do the following:

Generate one pair: ()

Generate 0 pair inside, n - 1 afterward: () (...)...

Generate 1 pair inside, n - 2 afterward: (()) (...)...

...

Generate n - 1 pair inside, 0 afterward: ((...))

I bet you see the overlapping subproblems here. Here is the code:

(you could see in the code that x represents one j-pair solution and y represents one (i - j - 1) pair solution, and we are taking into account all possible of combinations of them)

```Python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
```

看看caikehe的方案：

毫无疑问，这个非常好理解！

```Python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, n, "", res)
        return res

    def dfs(self, leftRemain, rightRemain, path, res):
        if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
            return  # backtracking
        if leftRemain == 0 and rightRemain == 0:
            res.append(path)
            return
        self.dfs(leftRemain-1, rightRemain, path+"(", res)
        self.dfs(leftRemain, rightRemain-1, path+")", res)
```

看看stefan大大的方案：

Solution 1

I used a few "tricks"... how many can you find? :-)

```python
def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)
```

Solution 2

Here I wrote an actual Python generator. I allow myself to put the yield q at the end of the line because it\'s not that bad and because in "real life" I use Python 3 where I just say yield from generate(...).

```python
def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in generate(p + '(', left-1, right): yield q
            for q in generate(p + ')', left, right-1): yield q
    return list(generate('', n, n))
```

Solution 3

Improved version of this. Parameter open tells the number of "already opened" parentheses, and I continue the recursion as long as I still have to open parentheses (n > 0) and I haven't made a mistake yet (open >= 0).

```python
def generateParenthesis(self, n, open=0):
    if n > 0 <= open:
        return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
               [')' + p for p in self.generateParenthesis(n, open-1)]
    return [')' * open] * (not n)

```

再来一个很牛的方法：

如果 n = 2， 那么递归树就长这样：

```text
                                       (0, 0, '')
                                         |    
                                    (1, 0, '(')  
                                   /           \
                            (2, 0, '((')      (1, 1, '()')
                               /                 \
                        (2, 1, '(()')           (2, 1, '()(')
                           /                       \
                    (2, 2, '(())')                (2, 2, '()()')
                              |                                 |
                    res.append('(())')             res.append('()()')
```

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                dfs(left + 1, right, s + '(')
            if right < left:
                dfs(left, right + 1, s + ')')
        res = list()
        dfs(0, 0, "")
        return res
```
