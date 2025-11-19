# 692. Top K Frequent Words

## 问题描述

Given an array of strings `words` and an integer `k`, return the k
most frequent strings.

Return the answer **sorted by the frequency from highest to lowest**.
Sort the words with the same frequency by their **lexicographical
order**.

## 示例

**Example 1:**

```text
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
```

Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

**Example 2:**

```text
Input: words = ["the","day","is","sunny","the","the",
                 "the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
```

Explanation: "the", "is", "sunny" and "day" are the four most frequent
words, with the number of occurrence being 4, 3, 2 and 1 respectively.

## 约束条件

- 1 <= words.length <= 500
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters
- k is in the range [1, The number of unique words[i]]

**Follow-up:** Could you solve it in O(n log k) time and O(n) extra
space?

## 解法

### 方法1：排序法（推荐，最简洁）

核心思想：统计频率后，使用双关键字排序（频率降序，字典序升序）。

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 统计每个单词的频率
        counter = Counter(words)
        
        # 双关键字排序：
        # 1. -counter[x]: 频率降序
        # 2. x: 字典序升序
        result = sorted(counter.keys(), key=lambda x: (-counter[x], x))
        
        return result[:k]
```

### 方法2：最小堆（满足Follow-up要求）

使用大小为k的最小堆，满足O(n log k)的时间复杂度要求。

关键点：使用自定义比较类来实现正确的堆排序逻辑。

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        
        # 自定义比较类：频率小的优先弹出，同频率时字典序大的优先弹出
        class Word:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq
            
            def __lt__(self, other):
                if self.freq != other.freq:
                    return self.freq < other.freq  # 频率小的在堆顶
                return self.word > other.word  # 字典序大的在堆顶
        
        heap = []
        for word, freq in counter.items():
            heapq.heappush(heap, Word(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 取出堆中所有元素并排序
        result = []
        while heap:
            result.append(heapq.heappop(heap).word)
        
        # 反转（因为从堆中弹出的顺序是频率从小到大）
        return result[::-1]
```

### 方法3：桶排序（按频率分组）

将相同频率的单词放入同一个桶，从高频到低频遍历。

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 统计频率
        counter = Counter(words)
        
        # 按频率分组：freq -> [words]
        buckets = defaultdict(list)
        for word, freq in counter.items():
            buckets[freq].append(word)
        
        # 从高频到低频遍历
        result = []
        for freq in sorted(buckets.keys(), reverse=True):
            # 同频率的单词按字典序排序
            result.extend(sorted(buckets[freq]))
            
            # 提前终止：收集够k个就返回
            if len(result) >= k:
                return result[:k]
        
        return result
```

## 算法分析

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 满足Follow-up |
|------|-----------|-----------|------------|
| 排序法 | O(n log n) | O(n) | ❌ |
| 最小堆 | O(n log k) | O(n) | ✅ |
| 桶排序 | O(n log n) | O(n) | ❌ |

其中 n 是不同单词的数量（unique words）。

排序法详细分析：

- 统计频率：O(m)，m是words数组长度
- 排序：O(n log n)，n是不同单词数
- 取前k个：O(k)
- 总时间：O(m + n log n)

最小堆详细分析：

- 统计频率：O(m)
- 维护大小为k的堆：O(n log k)
- 堆排序：O(k log k)
- 总时间：O(m + n log k)，满足Follow-up要求

### 执行过程示例

以 words = ["the","day","is","sunny","the","the","sunny","is","is"],
k = 4 为例。

Step 1：统计频率

```text
Counter: {"the": 3, "is": 3, "sunny": 2, "day": 1}
```

Step 2：排序（方法1）

```text
排序规则：(-freq, word)
("the", 3) -> (-3, "the")
("is", 3)  -> (-3, "is")
("sunny", 2) -> (-2, "sunny")
("day", 1) -> (-1, "day")

排序后：["is", "the", "sunny", "day"]
因为 "is" < "the"（字典序）
```

Step 3：桶排序（方法3）

```text
buckets = {
    3: ["the", "is"],
    2: ["sunny"],
    1: ["day"]
}

遍历顺序：3 -> 2 -> 1
- freq=3: sorted(["the", "is"]) = ["is", "the"]
- freq=2: sorted(["sunny"]) = ["sunny"]
- freq=1: sorted(["day"]) = ["day"]

result = ["is", "the", "sunny", "day"]
```

## 常见错误

### 错误1：边界条件处理错误

原始代码的问题：

```python
# 错误的逻辑
for i in freq:
    if k > int(i) and k > len(d[i]):
        res.extend(sorted(d[i]))
    elif k > 0:
        res.extend(sorted(d[i])[:k])
    k -= len(d[i])  # k可能变成负数
```

问题：

- k的判断逻辑混乱
- k -= len(d[i]) 会导致k变负数
- 没有正确处理"收集够k个就停止"

正确做法：

```python
result = []
for freq in sorted(buckets.keys(), reverse=True):
    result.extend(sorted(buckets[freq]))
    if len(result) >= k:
        return result[:k]  # 统一在这里截取
```

### 错误2：堆的比较规则错误

```python
# 错误：直接用(freq, word)会导致同频率时字典序小的被弹出
heap.append((freq, word))  # 错误！

# 错误：用(-freq, word)还是不对，因为word的比较方向没变
heap.append((-freq, word))  # 错误！

# 正确：使用自定义类实现正确的比较逻辑
class Word:
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.word > other.word  # 注意这里是大于号
```

**原因：** Python的堆是最小堆，我们需要：

1. 频率小的优先弹出（保留频率大的）
2. 同频率时，字典序**大**的优先弹出（保留字典序**小**的）

元组方法的问题：

- `(freq, word)`：同频率时 `"i" < "love"`，所以 "i" 被弹出 ❌
- `(-freq, word)`：同频率时还是 `"i" < "love"`，所以 "i" 被弹出 ❌

**举例：** words = ["i","love","leetcode","i","love","coding"], k = 1

- Counter: {"i": 2, "love": 2, ...}
- 使用自定义类：`Word("i", 2)` vs `Word("love", 2)`
- 比较结果：`"i" > "love"` 返回 False，`"love" > "i"` 返回 True
- 所以 `Word("love", 2)` 在堆顶，被弹出，保留 "i" ✅

### 错误3：忘记对同频率单词排序

```python
# 错误：直接extend不排序
result.extend(buckets[freq])  # 顺序可能是错的

# 正确：必须先排序
result.extend(sorted(buckets[freq]))
```

**原因：** defaultdict(list) 中的列表顺序是插入顺序，
不是字典序。

### 错误4：set vs list的选择

```python
# 使用set会丢失信息
d = defaultdict(set)  # set无序，排序时可能有问题

# 使用list更安全
d = defaultdict(list)
```

**原因：** 虽然set可以去重，但在Python 3.6+中dict已经保持插入顺序，
使用list更明确。

## 相关题目

- [0347. Top K Frequent Elements](./347_top_k_frequent_elements.md)
- [0451. Sort Characters By Frequency](./451_sort_characters_by_frequency.md)
- [0973. K Closest Points to Origin](./973_k_closest_points_to_origin.md)
- [0215. Kth Largest Element in an Array](./215_kth_largest_element_in_an_array.md)
- [0703. Kth Largest Element in a Stream](./703_kth_largest_element_in_a_stream.md)
