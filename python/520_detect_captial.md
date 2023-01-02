# detect captials

We define the usage of capitals in a word to be right when one of the following cases holds:

- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".
  Given a string word, return true if the usage of capitals in it is right.

Example 1:

```
Input: word = "USA"
Output: true
```

Example 2:

```
Input: word = "FlaG"
Output: false
```

Constraints:

- 1 <= word.length <= 100
- word consists of lowercase and uppercase English letters.

**有点智商被侮辱的感觉。。。**

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.lower() or word == word.capitalize() or word == word.upper()
```

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.istitle() or word.islower() or word.isupper()
```
