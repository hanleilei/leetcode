# 差分数组

构造差分数组的目的是为了快速处理区间更新问题。给定一个数组 `nums`，我们可以通过构造一个差分数组 `diff` 来实现对 `nums` 的区间加法操作。

```python
import sys
from typing import List

# -- core code template start
class Solution:
    def getModifiedArray(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n + 1)
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = nums[i] - nums[i - 1]

        for op in operations:
            i, j, val = op[0], op[1], op[2]
            prefix[i] += val
            if j + 1 < n:
                prefix[j + 1] -= val

        res = [0] * n
        res[0] = prefix[0]
        for i in range(1, n):
            res[i] = res[i - 1] + prefix[i]
        return res



        
# -- core code template end

lines = sys.stdin.read().strip().split('\n')
idx = 0
while idx < len(lines):
    n = int(lines[idx])
    idx += 1
    nums = list(map(int, lines[idx].split()))
    idx += 1
    m = int(lines[idx])
    idx += 1
    operations = []
    for _ in range(m):
        op = list(map(int, lines[idx].split()))
        operations.append(op)
        idx += 1

    result = Solution().getModifiedArray(nums, operations)

    for num in result:
        print(num)
```
