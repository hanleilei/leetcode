# Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

### 使用最挫的算法，挨个遍历，居然也能过：

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
```

### 参考[网页](http://blog.csdn.net/coder_orz/article/details/51706442)，还有两个算法，一个是先排序:

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        strs.sort()
        res = ''
        for i in range(len(strs[0])):
            if i >= len(strs[-1]) or strs[-1][i] != strs[0][i]:
                return res
            res += strs[0][i]
        return res
```
还有一个是使用zip方法，非常简练：

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)
```

最终结果还是比较有趣的，先排序的时间居然最少。

再来一个时间最少的：

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        res = 0
        for chars in zip(*strs):
            if len(set(chars)) > 1:
                return strs[0][:res]
            res += 1
        return min(strs)
```

注意这里的 zip(\*strs)的做法，可以通过这样的方式求转置。

还有一个先找到最短长度的方法：

```python
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        shortest = min(strs, key=len)
        for i, v in enumerate(shortest):
            for s in strs:
                if s[i] != v:
                    return s[:i]
        return shortest
```
