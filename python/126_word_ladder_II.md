# word ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
## Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

## Example 1:
```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
```
Example 2:
```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []
```

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

```python
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        words = set(wordList)
        if endWord not in wordList:
            return []

        words.add(beginWord)
        graph = collections.defaultdict(set)
        if not self.bfs(beginWord, endWord, graph, words):
            return []

        paths, path = [], [beginWord]
        self.dfs(graph, endWord, paths, path)
        return paths

    def bfs(self, beginWord, endWord, graph, words):
        n = len(beginWord)
        levels = [set([beginWord]), set([endWord])]

        while levels[0] and levels[1]:
            idx = 0 if len(levels[0]) < len(levels[1]) else 1
            preLevel = levels[idx]
            levels[idx] = set()
            isFound = False

            for word in preLevel:
                words.remove(word)
            for word in preLevel:
                for i in range(n):
                    prefix, suffix = word[:i], word[i + 1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        w = prefix + c + suffix
                        if w in words:
                            if w in levels[1 - idx]:
                                isFound = True
                            levels[idx].add(w)
                            if idx == 0:
                                graph[word].add(w)
                            else:
                                graph[w].add(word)
            if isFound:
                return True
        return False

    def dfs(self, graph, endWord, paths, path):
        if path[-1] == endWord:
            paths.append(list(path))
        for neighbor in graph[path[-1]]:
            path.append(neighbor)
            self.dfs(graph, endWord, paths, path)
            path.pop()
```

再来一个速度超级快的算法：

```python
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList or not endWord or not beginWord:
            return []
        wordList = set(wordList)
        forward, backward = {beginWord}, {endWord}
        direction = 1
        parents = collections.defaultdict(set)
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                # We need to trace the direction in order to distinguish the parents
                direction *= -1

            # The new set of words which will be forward in the next iteration
            next_foward = set()

            # Because all words in forward will be modified by one character
            wordList -= forward
            for word in forward:
                for i in range(len(word)):
                    first, second = word[:i], word[i+1:]
                    for ch in string.ascii_lowercase:
                        combined_word = first + ch + second
                        if combined_word in wordList:
                            next_foward.add(combined_word)
                            # Because at the last part, we find parents by indexing dictionary from endWord
                            # So when direction == 1, the combined_word is the key
                            # otherwise, the combined_word should be the value of dictionary.
                            if direction == 1:
                                parents[combined_word].add(word)
                            else:
                                parents[word].add(combined_word)

            # next_foward and backward are always in different direction,
            # so if they have common elements we find a path.
            # We check and return this function inside is because this problem finds the all shortest paths
            if next_foward & backward:
                # Starting from the endWord, we find its parent and append to results
                # And do this until we reach the beginWord
                results = [[endWord]]
                while results[0][0] != beginWord:
                    results = [ [parent] + result for result in results for parent in parents[result[0]] ]
                return results
            forward = next_foward
        return []

```
