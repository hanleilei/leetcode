# Maximum Length Substring With Two Occurrences

[[2points]]

Given a string s, return the maximum length of a  such that it contains at most two occurrences of each character.

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:
The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:

Input: s = "aaaa"

Output: 2

Explanation:
The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

Constraints:

    2 <= s.length <= 100
    s consists only of lowercase English letters.

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = left = 0
        d = defaultdict(int)
        for right, c in enumerate(s):
            d[c] += 1
            while d[c] > 2:
                d[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
```

```cpp
class Solution {
public:
    int maximumLengthSubstring(string& s) {
        int freq[26]={0};
        int l=0, n=s.size(), len=0;
        for(int r=0; r<n; r++){
            int x=s[r]-'a';
            freq[x]++;
            while(l<r && freq[x]>2){
                freq[s[l]-'a']--;
                l++;
            }
            len=max(len, r-l+1);
        }
        return len;
    }
};
```
