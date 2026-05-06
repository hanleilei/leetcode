# single number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

还是别用标准库了。

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                s.remove(i)
        return list(s)
```

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorm = 0
        for num in nums:
            xorm ^= num

        # 2. 找到结果中最低位的 1，将数组中的所有元素根据这个位进行分组。
        k = 0
        while xorm & 1 == 0:
            k += 1
            xorm >>= 1

        # 3. 在每个组中，找到出现两次的元素。
        ans = [0, 0]
        for num in nums:
            if (num >> k) & 1 == 1:
                ans[1] ^= num
            else:
                ans[0] ^= num

        return ans
```

## 1. 异或有几个重要性质

1. a ^ a = 0
2. a ^ 0 = a
3. 异或满足交换律和结合律：a ^ b ^ c = a ^ c ^ b

----

如果整个数组里只有 一个数字只出现一次，其他都出现两次，用 XOR 就能直接得到它：

```python
res = 0
for num in nums:
    res ^= num
```

最终 res 就是那个只出现一次的数字，因为相同的数字异或会消掉。

----

## 2. 扩展到两个数字

当有 两个只出现一次的数字（设为 x 和 y）时：

* XOR 整个数组得到 k = x ^ y
* 因为 x != y，所以 k != 0
* k 的二进制至少有一位是 1，表示 x 和 y 在这一位上不同

```python
k = 0
for i in nums:
    k ^= i  # k = x ^ y
```

## 3. 找到 区分 x 和 y 的位

k & -k 是一个常见的位运算技巧，作用是 找出 k 二进制中最右边的 1。

* s = k & -k
* 这个 s 就表示 x 和 y 在这一位上一定不同（一个是 0，一个是 1）

```python
k = 6 = 0110
-k = -6 = 1010 (补码表示)
k & -k = 0010  # 最右边的 1
```

## 4. 利用这个位分组

我们可以用这一位把数组分成两组：

1. i & s != 0 → 这组包含了 x 或 y 中的一个
2. i & s == 0 → 这组包含了另一个

在每一组中，其他重复出现的数字还是成对出现，异或就能消掉，只留下那个单独的数字。

```python
r = 0
for i in nums:
    if i & s:   # 属于“这一位为 1”的组
        r ^= i
```

* 这时 r 就是其中一个只出现一次的数字（假设是 x）
* 另一个数字就是 r ^ k（因为 x ^ y = k，所以 y = k ^ x）

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        k = 0
        for i in nums:
            k ^= i

        s = k & -k

        r = 0
        for i in nums:
            if i & s: # 属于“这一位为 1”的组
                r ^= i
        return [r, r ^ k]
```
