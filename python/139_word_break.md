# word break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Example 1

```text
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

## Example 2

```text
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

## Example 3

```text
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

## Constraints

- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.

先上一个stefan的算法：

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        return ok[-1]
```

再来一个改进的版本：

```python
class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        ok = [True]
        max_len = max(map(len,words+['']))
        words = set(words)
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(max(0, i-max_len),i)),
        return ok[-1]
```

words should be a set to get a O(1) lookup:
This changes the complexity of the approach, independent of the specific task
we don't have to check substrings against the dictionary that are longer than the longest entry in it
Could be considered a heuristic, as it's effect massively depends on the words.

再来一个bfs版本的：

```python
class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        queue = collections.deque()                                                                           
        visited = set()                                                                                       
        queue.appendleft(0)                                                                                   
        visited.add(0)                                                                                        
        while len(queue) > 0:                                                                                 
            curr_index = queue.pop()                                                                          
            for i in range(curr_index, len(s)+1):                                                             
                if i in visited:                                                                              
                    continue                                                                                  
                if s[curr_index:i] in words:
                    if i == len(s):                                                                           
                        return True                                                                           
                    queue.appendleft(i)                                                                       
                    visited.add(i)                                                                            
        return False
```

再来一个dp的方案：

The idea is the following:

- d is an array that contains booleans
- d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example:

- s = "leetcode"
- words = ["leet", "code"]
- d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"
- d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

The result is the last index of d.

```python
class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in words:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]
```
