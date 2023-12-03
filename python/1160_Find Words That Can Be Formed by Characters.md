# Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

## Example 1

```text
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
```

## Example 2

```text
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
```

## Constraints

```text
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
```

```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsMap = Counter(char)
        result = 0
        
        for word in words:
            charsMapCopy = charsMap.copy()
            end = True
            for char in word:
                if char in charsMapCopy and charsMapCopy[char] > 0:
                    charsMapCopy[char] -= 1
                else:
                    end = False
                    break
            if end:
                result += len(word)

        return result
```

```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total, chars_counter = 0, collections.Counter(chars)
        for word in words:
            word_counter = collections.Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                total += len(word)
        return total
```
