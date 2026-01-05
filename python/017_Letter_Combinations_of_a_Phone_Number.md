# Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want

标准dfs：

```python
mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        path = []

        def dfs(i: int):
            if i == len(digits):
                res.append("".join(path))
                return

            for c in mapping[int(digits[i])]:
                path.append(c)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res
```

```python
mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.res = []
        self._dfs(digits, 0, "")
        return self.res
    
    def _dfs(self, digits: str, idx: int, current: str):
        if idx == len(digits):
            self.res.append(current)
            return
        
        digit = int(digits[idx])
        for char in mapping[digit]:
            self._dfs(digits, idx + 1, current + char)
```

这个最简单的思路，其实就是和第六题的哪个zigzag的一样：

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        if len(digits) <= 0:
            return res
        res = list(d[digits[0]])

        for n in list(digits)[1:]:
            chars = d[n]
            temp = []
            for i in range(len(res)):
                for c in chars:
                    temp.append(res[i]+c)
            res = temp

        return res
```

或者caikehe的backtrack:

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if len(digits) == 0:
            return []
        res = []
        self.dfs(digits, dic, 0, "", res)
        return res

    def dfs(self, digits, dic, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                self.dfs(digits, dic, i+1, path+j, res)
        
```

迭代：

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        stack = [("", 0)]  # (当前字符串, 当前处理到digits的index)
        while stack:
            path, index = stack.pop()
            if len(path) == len(digits):
                res.append(path)
                continue
            for char in phone[digits[index]]:
                stack.append((path + char, index + 1))
        return res
```

```python
mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = [""]
        for d in digits:
            res = [p + c for p in res for c in mapping[int(d)]]
        return res
```

自己手搓的backtracking：

```python
mapping = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = list()
        self.dfs(self.res, digits)
        return self.res
    
    def dfs(self, res, digits):
        if digits == "":
            return 
        
        if len(res) == 0:
            res = list(mapping[int(digits[0])])
        else:
            res = [i + j for i in res for j in list(mapping[int(digits[0])])]
        
        return self.dfs(res, digits[1:])
```

生成器：

```python
mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        def gen(i):
            if i == len(digits):
                yield ""
                return
            for c in mapping[int(digits[i])]:
                for rest in gen(i + 1):
                    yield c + rest

        return list(gen(0))
```

标准库：

```python
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        groups = [mapping[int(d)] for d in digits]
        return ["".join(p) for p in product(*groups)]
```
