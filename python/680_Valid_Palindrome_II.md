# Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

## Example 1

```text
Input: "aba"
Output: True
```

## Example 2

```text
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
```

## Note

- The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

下面的这个纯粹就是思路问题：
先双指针，然后确定找到出现的第一个不同字符的位置。然后根据这两个位置的坐标，由于不确定是删除哪个字符，所以就可以得到两个数组，他们的偏移位置为1。

```Python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        begin, end = 0, len(s) -1

        while begin < end:
            if s[begin] != s[end]:
                first, second = s[begin:end], s[begin+1:end+1]
                return first == first[::-1] or second == second[::-1]
            begin, end = begin + 1, end - 1
        return True
```

再看看Lee215的方法，思路一样，只是省略了中间数组的拷贝：

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        while i < len(s) // 2 and s[i] == s[-(i + 1)]:
            i += 1
        s = s[i:len(s) - i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]
```

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1   
            else:   
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True
```
