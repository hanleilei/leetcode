# Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question

找出最长序列的长度，一个可行的办法是转换成ascii码，然后遍历字符串，

```cpp
class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    int ans = 0;
    int dic[256];
    memset(dic,-1,sizeof(dic));
    int len = s.size();
    int idx = -1;

    for (int i=0;i<len;i++)
    {
      char c = s[i];
      if (dic[c]>idx)
        idx = dic[c];

      ans = max(ans,i-idx);

      dic[c] = i;
    }

    return ans;
  }
};
```
