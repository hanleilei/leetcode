# Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



### Example 1:
```
Input: ["bella","label","roller"]
Output: ["e","l","l"]
```

### Example 2:
```
Input: ["cool","lock","cook"]
Output: ["c","o"]
```

### Note:
```
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
```

来一个第一反应：

```python
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())
```
oneline:

```python
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        return list(reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())

```

再来一个最快的：

```python
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return_list = list()
        for letter in string.ascii_lowercase:
            letter_count = float("inf")
            for word in A:
                letter_count = min(letter_count, word.count(letter))
                if letter_count == 0:
                    break
            for i in range(letter_count):
                return_list.append(letter)
        return return_list
```
