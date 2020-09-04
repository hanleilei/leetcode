# stream of characters

Implement the StreamChecker class as follows:

* StreamChecker(words): Constructor, init the data structure with the given words.
* query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.


Example:
```
StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
````

Note:
```
1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
```
这个问题， 现在是必须要用Trie来解决, 先来一个速度最快的：

```Python

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class StreamChecker:

    def __init__(self, words: List[str]):
        trie = {}

        for word in words:
            subtrie = trie

            for char in word[::-1]:
                if char in subtrie:
                    subtrie = subtrie[char]
                else:
                    subtrie[char] = {}
                    subtrie = subtrie[char]
            subtrie['end'] = True

        self.trie = trie
        self.arr = []

    def query(self, letter: str) -> bool:
        arr = self.arr
        arr.append(letter)
        trie = self.trie

        for i in range(len(arr)-1, -1, -1):
            l = arr[i]
            if l not in trie:
                return False
            else:
                trie = trie[l]

            if 'end' in trie:
                return True

        return False
```

再来一个Lee215的方法：

```Python
class StreamChecker:

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w[::-1], self.trie)['#'] = True
        self.S = ""
        self.W = max(map(len, words))

    def query(self, letter):
        self.S = (letter + self.S)[:self.W]
        cur = self.trie
        for c in self.S:
            if c in cur:
                cur = cur[c]
                if cur['#'] == True:
                    return True
            else:
                break
        return False

```
写的有点牛逼， 这样构造trie也是可以的。

再来一个：

```Python
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.letters = []
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        i = len(self.letters) - 1
        node = self.trie.root
        while i >= 0:
            if node.isEnd:
                return True
            if self.letters[i] not in node.children:
                return False
            node = node.children[self.letters[i]]
            i -= 1
        return node.isEnd
```
