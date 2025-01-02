# Count Vowel Strings in Ranges

[[prefixSum]]

You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].
Example 2:

Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].

Constraints:

1 <= words.length <= 105
1 <= words[i].length <= 40
words[i] consists only of lowercase English letters.
sum(words[i].length) <= 3 * 105
1 <= queries.length <= 105
0 <= li <= ri < words.length

自己想出来的方法，注意边界条件，需要在count数组的前面加一个0，这样可以避免判断是否越界。

```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        count = [0]

        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                count.append(1)
            else:
                count.append(0)
        for i in range(1, len(count)):
            count[i] += count[i-1]
        return [count[e + 1] - count[s] for s, e in queries]
```

注意这里构造前缀和数组的方式很巧妙，用一个cur变量来记录当前的前缀和，然后将cur添加到前缀和数组中。

```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        cur = 0
        vowelSet = set(['a', 'e', 'i', 'o', 'u'])
        for s in words:
            if s[0] in vowelSet and s[-1] in vowelSet:
                cur += 1
            prefix.append(cur)
        return [prefix[e + 1] - prefix[s] for s, e in queries]
```

这里使用extend方法来构建前缀和数组，extend方法可以将一个可迭代对象中的元素逐个添加到列表中。

```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        count = [0]  # 前缀和数组

        # 构建前缀和数组
        count.extend(count[-1] + (w[0] in vowels and w[-1] in vowels) for w in words)
        
        # 计算每个查询的结果
        return [count[e + 1] - count[s] for s, e in queries]
```

```java
class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        int[] prefixSum = new int[words.length + 1];

        // 构建前缀和数组
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            prefixSum[i + 1] = prefixSum[i] + 
                (vowels.contains(word.charAt(0)) && vowels.contains(word.charAt(word.length() - 1)) ? 1 : 0);
        }

        // 使用数组来存储结果
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int start = queries[i][0];
            int end = queries[i][1];
            result[i] = prefixSum[end + 1] - prefixSum[start];
        }

        return result;
    }
}
```

```go
func vowelStrings(words []string, queries [][]int) []int {
    vowels := map[rune]struct{}{
        'a': {}, 'e': {}, 'i': {}, 'o': {}, 'u': {},
    }
    prefixSum := make([]int, len(words)+1)

    // 构建前缀和数组
    for i, word := range words {
        if _, ok1 := vowels[rune(word[0])]; ok1 {
            if _, ok2 := vowels[rune(word[len(word)-1])]; ok2 {
                prefixSum[i+1] = prefixSum[i] + 1
                continue
            }
        }
        prefixSum[i+1] = prefixSum[i]
    }

    // 计算每个查询的结果
    result := make([]int, len(queries))
    for i, query := range queries {
        result[i] = prefixSum[query[1]+1] - prefixSum[query[0]]
    }

    return result
}
```

```rust
impl Solution {
    pub fn vowel_strings(words: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        // 定义元音集合
        let vowels: std::collections::HashSet<char> = ['a', 'e', 'i', 'o', 'u'].iter().cloned().collect();

        // 构建前缀和数组
        let mut prefix_sum = vec![0; words.len() + 1];
        for (i, word) in words.iter().enumerate() {
            let first_char = word.chars().next().unwrap();
            let last_char = word.chars().last().unwrap();
            prefix_sum[i + 1] = prefix_sum[i] + 
                if vowels.contains(&first_char) && vowels.contains(&last_char) { 1 } else { 0 };
        }

        // 计算每个查询的结果
        queries.iter()
            .map(|query| {
                let start = query[0] as usize;
                let end = query[1] as usize;
                prefix_sum[end + 1] - prefix_sum[start]
            })
            .collect()
    }
}
```
