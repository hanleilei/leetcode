# Count Pairs That Form a Complete Day I

# Count Pairs That Form a Complete Day I

Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.

A complete day is defined as a time duration that is an exact multiple of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

## Example 1

```text
Input: hours = [12,12,30,24,24]

Output: 2

Explanation:

The pairs of indices that form a complete day are (0, 1) and (3, 4).
```

## Example 2

```text
Input: hours = [72,48,24,3]

Output: 3

Explanation:

The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).
```

## Constraints

```text
1 <= hours.length <= 100
1 <= hours[i] <= 109
```

```python
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        h = 24
        res = 0
        count = [0] * h
        for t in hours:
            res += count[(h - t % h) % h]
            count[t % h] += 1
        return res    
```

```rust
impl Solution {
    pub fn count_complete_day_pairs(hours: Vec<i32>) -> i64 {
        const h: usize = 24;
        let mut res = 0;
        let mut cnt = vec![0;h];
        for t in hours{
            let t = t as usize % h;
            res += cnt[(h - t) % h];
            cnt[t] += 1;
        }
        res
    }
}
```

```go
func countCompleteDayPairs(hours []int) (ans int64) {
    const h = 24
    cnt := [h]int{}

    for _, t := range hours{
        ans += int64(cnt[(h - t % h) % h])
        cnt[t%h]++
    }
    return 
}
```

```java
class Solution {
    public long countCompleteDayPairs(int[] hours) {
        final int h = 24;
        long ans = 0;
        int[] cnt = new int[h];
        for (int t: hours){
            ans += cnt[(h - t % h) % h];
            cnt[t% h]++;
        }
        return ans;
    }
}
```

```cpp
class Solution {
public:
    long long countCompleteDayPairs(vector<int>& hours) {
        const int h = 24;
        long long ans = 0;
        int cnt[h]{};
        for (int t: hours){
            ans += cnt[(h - t % h) % h];
            cnt[t% h]++;
        }
        return ans;
    }
};

```
