# Longest Palindromic Substring

Given a string s, return the longest in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

```java
class Solution {
    private int maxLength = 0;
    private int start = 0;

    public String longestPalindrome(String s) {
        if (s == null || s.length() < 2) {
            return s;
        }
        for (int i = 0; i < s.length(); i++){
            extendPal(s, i, i);
            extendPal(s, i, i+1);
            if (maxLength == s.length()){
                return s.substring(start, start + maxLength);
            }
        }
        return s.substring(start, start + maxLength);
    }

    private void extendPal(String s, int left, int right){
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
        }

        int length = right - left - 1;
        if (length > maxLength){
            maxLength = length;
            start = left + 1;
        }
    }
}
```
