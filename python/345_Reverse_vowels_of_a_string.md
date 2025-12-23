# reversed vowels of a string

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

## 双指针

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(list("aeiouAEIOU"))
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
        return ''.join(s)


```
再来一个用栈实现的。

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        rtype = list()
        v = [i for i in s if i in vowels]
        for i in s:
            if i in vowels:
                rtype += v.pop()
            else:
                rtype += i
        return ''.join(rtype)



```
再来一个stefan大大的：

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
```

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)
```
