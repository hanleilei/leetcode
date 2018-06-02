# Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:
```
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

```java
class Solution {
    public int minCut(String s) {
        if (s == null || s.length() == 0) return 0;
        int len = s.length();
        int[] cuts = new int[len];
        boolean[][] isPalindrome = new boolean[len][len];
        for ( int i = 0; i < len; i++){
            int min = i;
            for (int j = 0; j <=i; j++){
                if (s.charAt(i) == s.charAt(j) && (i - j < 2 || isPalindrome[j+1][i-1])){
                    isPalindrome[j][i] = true;
                    min = j == 0 ? 0 : Math.min(min, cuts[j - 1] + 1);
                }
            }
            cuts[i] = min;
        }
        return cuts[len - 1];
    }
}
```

下面是一个更简洁的版本，速度很快，只要了2ms

```java
class Solution {
    public int minCut(String s) {
        int n = s.length();
        if(n<=1) return 0;

        int[] cut = new int[n];
        for(int i = 0; i<n;i++) cut[i] = i;
        for(int i = 0; i<n; i++){
            dfs(s,cut,i,i);
            dfs(s,cut,i,i+1);
        }
        return cut[n-1];
    }

    public void dfs(String s, int[] cut, int l, int r){
        if(l >=0 && r < s.length() && s.charAt(l) == s.charAt(r)){
            if( l== 0) cut[r] = 0;
            else{
                cut[r] = Math.min(cut[r],cut[l-1]+1);
            }
            dfs(s,cut, l-1, r+1);
        }
    }

}
```
