# word ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

```Python
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        front, back = set([beginWord]), set([endWord])
        wordDict = set(wordList)
        length = 2
        width = len(beginWord)
        charSet = 'abcdefghijklmnopqrstuvwxyz'

        if endWord not in wordDict:
            return 0

        while front:
            newFront = set()

            for phase in front:
                for i in range(width):
                    for c in charSet:
                        nw = phase[:i] + c + phase[i+1:]
                        if nw in back:
                            return length
                        if nw in wordDict:
                            newFront.add(nw)
            front = newFront

            if len(front) > len(back):
                front,back = back,front

            wordDict -= wordDict & front
            length += 1

        return 0
```
