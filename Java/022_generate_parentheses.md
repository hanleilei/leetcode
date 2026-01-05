# Generate Parentheses

[[dfs]] [[backtracking]]

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

```java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<String>();
        generateOneByOne("", result, n, n);
        return result;
    }
    public void generateOneByOne(String sublist, List<String> result, int left, int right){
        if (left == 0 && right == 0){
            result.add(sublist);
            return ;
        }
        if (left > 0){
            generateOneByOne(sublist + "(", result, left - 1, right);
        }
        if (right > left){
            generateOneByOne(sublist + ")", result, left, right - 1);
        }
    }
}
```
