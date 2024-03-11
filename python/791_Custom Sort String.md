# Custom Sort String

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

## Example 1

```text
Input:  order = "cba", s = "abcd" 

Output:  "cbad" 

Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".

Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
```

## Example 2

```text
Input:  order = "bcafg", s = "abcd" 

Output:  "bcad" 

Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.

Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.
```

## Constraints

```text
1 <= order.length <= 26
1 <= s.length <= 200
order and s consist of lowercase English letters.
All the characters of order are unique.
```

就是阅读理解，虽然写出来感觉自己的代码很挫。。

```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = dict(zip(order, list(range(len(order)))))
        d = defaultdict(list)
        res = list()
        not_in = [i for i in s if i not in order_dict]
        for i in s:
            if i in order_dict:
                d[order_dict[i]].append(i)
        for j in sorted([int(i) for i in d.keys()]):
            res.append("".join(d[j]))
        res.append(''.join(not_in))
        return ''.join(res)
```

再来一个官网速度最快的

```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        sb = []
        for o in order:
            for i in range(counter[o]):
                sb.append(o)  # 解决多个重复元素的问题
            counter[o] = 0

        for key in counter:
            for i in range(counter[key]):
                sb.append(key)
        
        return ''.join(sb)
```
