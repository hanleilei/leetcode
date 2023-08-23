# Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:
```
Input: s = "aab"
Output: "aba"
```
Example 2:
```
Input: s = "aaab"
Output: ""
```

Constraints:

- 1 <= s.length <= 500
- s consists of lowercase English letters.

直接上heap, 想起多年前做过一个类似的题目：有多个颜色的小球，要求重新排列，使相邻的小球不能颜色重复。

The idea is to build a max heap with freq. count
a) At each step, we choose the element with highest freq (a, b) where b is the element, to append to result.
b) Now that b is chosen. We cant choose b for the next loop. So we dont add b with decremented value count immediately into the heap. Rather we store it in prev_a, prev_b variables.
c) Before we update our prev_a, prev_b variables as mentioned in step 2, we know that whatever prev_a, prev_b contains, has become eligible for next loop selection. so we add that back in the heap.

In essence,

at each step, we make the currently added one ineligible for next step, by not adding it to the heap
at each step, we make the previously added one eligible for next step, by adding it back to the heap


```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = list()
        c = Counter(s)
        pq = [(-val, key) for key, val in c.items()]
        heapq.heapify(pq)

        pa, pb = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            if pa < 0:
                heapq.heappush(pq, (pa, pb))
            a += 1
            pa, pb = a, b
        res = "".join(res)
        if len(res) != len(s): return ""
        return res
```
下面是解释，比较详细的阐述了while里面的作用：

```
So at max we need the top 2 highest counts.
so p_a, p_b is to store the previous a and b which is (count and value)

lets go with example string aab
if you take the counts and put that in heap it becomes [(-2, 'a'), (-1, 'b')]
Now you need a way to alternate the top 2 picks (just so their adj charecters are diffrent)
you already know p_a and p_b is to store the prev counts, so initially they are 0 and "" (0counts and noString)
1st iteration:

a, b = heapq.heappop(pq) -> Taking out the top value which is (-2, 'a')
res += b => add that to result string ; result string becomes "a"
a += 1 => since we took 1 a out of 2 a we increment the count so now the heap value of a becomes (-1, 'a')
p_a, p_b = a, b => capture the a and updated count 1 to p_a and p_b
2nd iteration:
now the heap only has (-1, 'b') (why? heappoped (-2,a) in 1st iteration
now perform 1, 2 from 1st iteration => result string becomes "ab"
now check your prev p_a and p_b since there is a reamining count of -1 for p_a which means the prev top element is not exhausted yet, so push it back to heap heapq.heappush(pq, (p_a, p_b))

3 iteration:
Same as 1st iteration.

since you dont have any values in the heap you check if the res string is == S, why ? (if your input is like 'aaa' then the heap approach will give you 'aaa' which is same as S)
```
