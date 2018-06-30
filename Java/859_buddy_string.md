# buddy string

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

Example 1:
```
Input: A = "ab", B = "ba"
Output: true
```
Example 2:
```
Input: A = "ab", B = "ab"
Output: false
```
Example 3:
```
Input: A = "aa", B = "aa"
Output: true
```
Example 4:
```
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
```
Example 5:
```
Input: A = "", B = "aa"
Output: false
```

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.


```java
class Solution {
    
    int[] alpha = new int[26];
    int[] beta = new int[26];
    int numOfUniqLetters = 0;
    public boolean buddyStrings(String A, String B) {
        if(A==null || B==null || A.length() < 2 || B.length() <2 || A.length()!=B.length()) {
            return false;
        }

        int diff = 0;
        for(int i =0; i< A.length(); i++) {
            int c = A.charAt(i) - 'a';
            if(alpha[c] ==0) {
                numOfUniqLetters++;
            }
            alpha[c]++;

            c = B.charAt(i) - 'a';
            beta[c]++;

            if(A.charAt(i)!=B.charAt(i)) {
                diff++;
            }
        }

        if(A.equals(B)) {
            if(numOfUniqLetters < A.length()) {
                return true;
            } else {
                return false;
            }
        }

        for(int i =0; i< alpha.length; i++) {
            if(alpha[i] != beta[i]) {
                return false;
            }
        }
        
        return diff<=2;
    
    }
}
```
