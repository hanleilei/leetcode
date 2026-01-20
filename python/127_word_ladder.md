# word ladder

[[bfs]]

## Problem Description

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *the **number of words** in the **shortest transformation sequence** from* `beginWord` *to* `endWord`*, or* `0` *if no such sequence exists.*

**Example 1:**

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
**Output:** 5
**Explanation:** One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.

**Example 2:**

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
**Output:** 0
**Explanation:** The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

**Constraints:**

- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- `beginWord != endWord`
- All the words in `wordList` are **unique**.

---

## Solution Approaches

### Approach 1: Bidirectional BFS (Optimal)

**Key Insight:**
- Use bidirectional BFS from both beginWord and endWord simultaneously
- Search from the smaller frontier to reduce time complexity
- Meet in the middle when frontiers intersect

**Why Bidirectional BFS?**
- Regular BFS: explores all nodes at distance d before distance d+1
- Bidirectional BFS: searches from both ends, meeting in the middle
- Time complexity improvement: O(b^(d/2)) vs O(b^d) where b is branching factor, d is depth

**Time Complexity:** O(M² × N) where M is word length, N is wordList size
**Space Complexity:** O(M × N) for storing word sets

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert to set for O(1) lookup
        word_set = set(wordList)
        
        # endWord must be in wordList
        if endWord not in word_set:
            return 0
        
        # Initialize two frontiers
        front = {beginWord}
        back = {endWord}
        length = 2  # Start at 2 (beginWord + 1 step)
        word_len = len(beginWord)
        
        while front:
            # Generate all possible next words from current frontier
            new_front = set()
            
            for word in front:
                for i in range(word_len):
                    # Try all 26 letters at position i
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        
                        # Found connection between two frontiers
                        if new_word in back:
                            return length
                        
                        # Valid transformation found
                        if new_word in word_set:
                            new_front.add(new_word)
            
            # Move to next level
            front = new_front
            
            # Always expand the smaller frontier (optimization)
            if len(front) > len(back):
                front, back = back, front
            
            # Remove visited words to avoid cycles
            word_set -= front
            length += 1
        
        return 0
```

### Approach 2: Standard BFS with Queue

**Standard BFS approach** using a queue:

**Time Complexity:** O(M² × N)
**Space Complexity:** O(M × N)

```python
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])  # (current_word, steps)
        
        while queue:
            current_word, steps = queue.popleft()
            
            # Try all possible transformations
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                    if next_word == endWord:
                        return steps + 1
                    
                    if next_word in word_set:
                        word_set.remove(next_word)  # Mark as visited
                        queue.append((next_word, steps + 1))
        
        return 0
```

### Approach 3: BFS with Pre-computed Graph

**Key Insight:**
- Pre-compute all possible word transformations
- Build adjacency graph
- Run BFS on the graph

**Time Complexity:** O(M² × N) preprocessing + O(M × N) BFS
**Space Complexity:** O(M² × N) for the graph

```python
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Add beginWord to wordList if not present
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        # Build adjacency graph using intermediate states
        # e.g., "hot" -> "*ot", "h*t", "ho*"
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                neighbors[pattern].append(word)
        
        # BFS
        visited = {beginWord}
        queue = deque([(beginWord, 1)])
        
        while queue:
            current_word, steps = queue.popleft()
            
            # Generate all intermediate patterns for current word
            for i in range(len(current_word)):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                
                # Check all words matching this pattern
                for neighbor in neighbors[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
        
        return 0
```

---

## Key Takeaways

1. **Bidirectional BFS is optimal** for finding shortest path in unweighted graphs
2. **Always expand smaller frontier** in bidirectional search for better performance
3. **Remove visited nodes** from word_set to prevent cycles and redundant work
4. **Pre-computing patterns** can simplify neighbor finding but uses more space
5. **Early termination**: Check if endWord exists in wordList before starting

## Complexity Analysis Summary

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Bidirectional BFS | O(M² × N) | O(M × N) | Best for large search spaces |
| Standard BFS | O(M² × N) | O(M × N) | Simpler implementation |
| Pre-computed Graph | O(M² × N) | O(M² × N) | Good when multiple queries |

Where:
- M = length of each word
- N = size of wordList

## Related Problems

- LeetCode 126: Word Ladder II (find all shortest paths)
- LeetCode 433: Minimum Genetic Mutation
- LeetCode 752: Open the Lock
