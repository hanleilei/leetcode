# Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want

#### 千万别用itertools里面的product方法，根本没法用。

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {
               "0":  (),
               "1":  (),
               "2": ("a", "b", "c"),
               "3": ("d", "e", "f"),
               "4": ("g", "h", "i"),
               "5": ("j", "k", "l"),
               "6": ("m", "n", "o"),
               "7": ("p", "q", "r", "s"),
               "8": ("t", "u", "v"),
               "9": ("w", "x", "y", "z")
               }
        result1 = [ "" ]
        result2 = [ ]
        if digits == "":
            return result2
        for ch in digits:
            lt = d[ch]
            if 0 == len(lt):
                continue
            for str in result1:
                for suffix in lt:
                    result2.append(str + suffix)
            result1 = result2
            result2 = [ ]
        return result1
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
