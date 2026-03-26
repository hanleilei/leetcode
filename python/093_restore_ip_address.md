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

再来一个容易理解的：每次把 1 到 3 个数字当作一个 IP 段，多个数字时要注意首位不能为 0，因为 01.0.0.0 这样的 IP 是不符合规范的，此外三个数字时还不能超过 255。当递归的序列为空，且此时正好集齐四个 IP 段，则得到一个正确答案。在递归的序列为空或者 IP 段数目达到 4 时都应该终止递归。+

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

方法一：三重循环，枚举分割位置

问题相当于把 s 切三刀，分割成四段。

写个三重循环，枚举这三刀（三个点号）的位置 i,j,k：

第一段从 0 到 i−1。
第二段从 i 到 j−1。
第三段从 j 到 k−1。
第四段从 k 到 n−1。其中 n 是 s 的长度。
对于每一段（子串 t），还需要判断子串 t 是不是合法的，也就是：

如果 t 的长度大于 1 且 t[0]=‘0’，那么 t 有前导零，不符合要求。
否则，t 对应的整数必须 ≤255，否则不符合要求。可以先判断 t 的长度是否超过 3，超过就直接判定为不合法。

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(t: str) -> bool:
            if len(t) > 3 or len(t) > 1 and t[0] == '0':
                return False
            return int(t) <= 255
        
        n = len(s)
        res = []
        for i in range(1, n):
            if not is_valid(s[:i]):
                break
            for j in range(i + 1, n):
                if not is_valid(s[i:j]):
                    break
                for k in range(j + 1, n):
                    if not is_valid(s[j:k]):
                        break
                    if is_valid(s[k:]):
                        res.append(f"{s[:i]}.{s[i:j]}.{s[j:k]}.{s[k:]}")
        return res
```

复杂度分析

时间复杂度：O(n^4)，其中 n 是 s 的长度。写了一个 O(n^3) 的三重循环，再算上生成 IP 地址字符串的 O(n) 时间，一共是 O(n^4)。
空间复杂度：O(1)。返回值不计入。

方法二：回溯

推荐先完成 131. 分割回文串，因为 131 题没有分割段数的要求，而本题要求分成恰好 4 段，所以本题相对来说更复杂一些。

写法一：选或不选（是否分割）

在 131 题的基础上，我们需要额外知道：

当前在第几段。
当前分割的子串，对应的数值是多少，便于我们判断子串是否合法。
定义 dfs(i,j,ipVal)，表示：

剩余字符从 s[i] 到 s[n−1]。
现在在第 j 段（j 从 0 开始）。
第 j 段的数值目前为 ipVal。
递归过程中，首先把 s[i] 加到当前这一段的末尾，即更新 ipVal 为 ipVal⋅10+int(s[i])。例如在 12 的末尾添加 3，数值更新为 12⋅10+3=123。

分类讨论：

不分割，前提是不能有前导零，即此时 ipVal>0。往下递归到 dfs(i+1,j,ipVal)。注意，如果有前导零的话，会在前导零那个字符处发现 ipVal=0，不会往下递归。
分割，s[i] 作为当前这段子串的右端点。把 j 加一，ipVal 重置为 0。往下递归到 dfs(i+1,j+1,0)。
递归边界：

i=n 时，s 分割完毕，如果此时 j=4，把分割结果加入答案。
否则，如果 j=4，由于此时已经分出 4 段，不能再分割，所以不再递归。
递归入口：dfs(0,0,0)。

⚠注意：下面代码中，path 的长度是固定的 4，可以直接覆盖 path[j]，无需恢复现场。如果是 path 初始化为空列表的那种写法，就需要恢复现场。

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        path = [0] * 4  # path[i] 表示第 i 段的结束位置 + 1（右开区间）

        # 分割 s[i] 到 s[n-1]，现在在第 j 段（j 从 0 开始），数值为 ip_val
        def dfs(i: int, j: int, ip_val: int) -> None:
            if i == n:  # s 分割完毕
                if j == 4:  # 必须有 4 段
                    a, b, c, _ = path
                    ans.append(f"{s[:a]}.{s[a:b]}.{s[b:c]}.{s[c:]}")
                return

            if j == 4:  # j=4 的时候必须分割完毕，不能有剩余字符
                return

            # 手动把字符串转成整数，这样字符串转整数是严格 O(1) 的
            ip_val = ip_val * 10 + int(s[i])
            if ip_val > 255:  # 不合法
                return

            # 不分割，不以 s[i] 为这一段的结尾
            if ip_val > 0:  # 无前导零
                dfs(i + 1, j, ip_val)

            # 分割，以 s[i] 为这一段的结尾
            path[j] = i + 1  # 记录下一段的开始位置
            dfs(i + 1, j + 1, 0)

        dfs(0, 0, 0)
        return ans
```

写法二：枚举选哪个（枚举子串右端点）

在 131 题的基础上，我们需要额外知道当前在第几段。

定义 dfs(i,j)，表示：

剩余字符从 s[i] 到 s[n−1]。
现在在第 j 段（j 从 0 开始）。
递归过程中，当前子串左端点为 i，我们枚举右端点 right=i,i+1,i+2,…,n−1，同时像写法一那样维护 ipVal。如果 ipVal>255 则退出循环。否则下一段的左端点为 right+1，j 增加 1，递归到 dfs(right+1,j+1)。循环末尾如果发现 ipVal=0，那么对于后续循环来说有前导零，不合法，也退出循环。

递归边界：

剪枝：还剩下 n−i 个字符，需要分成 4−j 段，每段至少 1 个字符，至多 3 个字符，所以必须满足 4−j≤n−i≤(4−j)⋅3，若不满足则返回。
i=n 时，s 分割完毕，把分割结果加入答案。注意我们上面剪枝了，此时 j=4 一定成立。
递归入口：dfs(0,0)。

⚠注意：下面代码中，path 的长度是固定的 4，可以直接覆盖 path[j]，无需恢复现场。如果是 path 初始化为空列表的那种写法，就需要恢复现场。

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        path = [''] * 4

        # 分割 s[i] 到 s[n-1]，现在在第 j 段（j 从 0 开始）
        def dfs(i: int, j: int) -> None:
            # 剪枝：还剩下 n-i 个字符，需要分成 4-j 段，每段至少 1 个字符，至多 3 个字符，所以 4-j <= n-i <= (4-j)*3
            if not 4 - j <= n - i <= (4 - j) * 3:
                return

            if i == n:  # s 分割完毕
                ans.append('.'.join(path))
                return

            # 子串左端点为 i
            # 枚举子串右端点 right
            ip_val = 0
            for right in range(i, n):
                ip_val = ip_val * 10 + int(s[right])
                if ip_val > 255:  # 不合法
                    break
                path[j] = s[i: right + 1]  # 直接覆盖 path[j]，无需恢复现场
                dfs(right + 1, j + 1)
                if ip_val == 0:  # 前导零，对于后续循环不合法
                    break

        dfs(0, 0)
        return ans
```
