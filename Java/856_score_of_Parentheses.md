# score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

* () has score 1
* AB has score A + B, where A and B are balanced parentheses strings.
* (A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:
```
Input: "()"
Output: 1
```
Example 2:
```
Input: "(())"
Output: 2
```
Example 3:
```
Input: "()()"
Output: 2
```
Example 4:
```
Input: "(()(()))"
Output: 6
```


```java
class Solution {
    private int score(char arr[], int idx[]){
        int accScore = 0;
        while(idx[0] < arr.length && arr[idx[0]] != ')'){
            idx[0]++;
            accScore += score(arr, idx);
            idx[0]++;
        }   
        if(idx[0] < arr.length){
            accScore = accScore ==0 ? 1 : 2*accScore;
        }
        return accScore;
    }
    
    public int scoreOfParentheses(String S) {
        if(S.length() ==0) return 0;
        int []arr = new int[1];
        arr[0] = 0;
       return score(S.toCharArray(), arr);
    }
}
```
