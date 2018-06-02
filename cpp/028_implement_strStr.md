# Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

还是直接上KMP吧。。。虽然比python的cmp算法要长不少。。

```c++
class Solution {
public:
    int strStr(string haystack, string needle) {
        // return haystack.find(needle);
        // kmp
        if(needle.size() == 0)
            return 0;

        int needle_size = needle.size();
        vector<int> next(needle_size +1, 0);
        next[0] = -1;

        for(int i = 1, j = -1; i < needle_size; i++){
            while(j!= -1 && needle[j+1] != needle[i])
                j = next[j];
            j = (j == -1) ? (needle[0] == needle[i]) -1: j + 1;
            next[i] = j;
        }
        for (int i = 0, j = -1; i<haystack.size(); i++){
            while (j != -1 && needle[j+1] != haystack[i])
                j = next[j];
            j = (j == -1) ? (haystack[i] == needle[0]) -1: j+1;
            if (j == needle.size() -1)
                return i - needle_size + 1;
        }
        return -1;
    }
};
```
