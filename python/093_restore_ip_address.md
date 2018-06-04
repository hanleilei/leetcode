# restore ip address

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:
```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

```python
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res=[]
        self.dfs(s,4,[])
        return ['.'.join(x) for x in self.res]

    def dfs(self,s,k,path):
        if len(s)>k*3:
            return
        if k==0:
            self.res.append(path)
        else:
            for i in range(min(3,len(s)-k+1)):
                if i==2 and int(s[:3])>255 or i>0 and s[0]=='0':
                    continue
                self.dfs(s[i+1:],k-1,path+[s[:i+1]])
```

再来一个容易理解的：每次把1到3个数字当作一个IP段，多个数字时要注意首位不能为0，因为 01.0.0.0 这样的IP是不符合规范的，此外三个数字时还不能超过255。当递归的序列为空，且此时正好集齐四个IP段，则得到一个正确答案。在递归的序列为空或者IP段数目达到4时都应该终止递归。+



```python
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self._restoreIpAddresses(0, s, [], result)
        return result

    def _restoreIpAddresses(self, length, s, ips, result):
        if not s:
            if length == 4:
                result.append('.'.join(ips))
            return
        elif length == 4:
            return
        self._restoreIpAddresses(length + 1, s[1:], ips + [s[:1]], result)
        if s[0] != '0':
            if len(s) >= 2:
                self._restoreIpAddresses(length + 1, s[2:], ips + [s[:2]], result)
            if len(s) >= 3 and int(s[:3]) <= 255:
                self._restoreIpAddresses(length + 1, s[3:], ips + [s[:3]], result)
```
