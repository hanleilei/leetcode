# Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

#### 利用递归，注意满足的两个条件：左括号一定要大于零，右括号一定要大于零，且大于左括号的数量

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
