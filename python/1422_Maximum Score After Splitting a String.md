# Maximum Score After Splitting a String

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:

```text
Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
```

Example 2:

```text
Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
```

Example 3:

```text
Input: s = "1111"
Output: 3
```

Constraints:

```text
2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
```

看到了自己比起一年前，还是有进步。至少当时根本没有敢记录自己的方法，现在随手就写好了。。

```python
class Solution:
    def maxScore(self, s: str) -> int:
        zero, ones = 0, s.count('1')
        res = 0
        for i in s[:-1]:
            if i == '0':
                zero += 1
            else:
                ones -= 1
            res = max(res, zero + ones)
        return res
```

```rust
impl Solution {
    pub fn max_score(s: String) -> i32 {
        let mut left = 0;
        let mut right = s.chars().filter(|&c| c == '1').count() as i32;
        let mut res = 0;

        for c in s.chars().take(s.len() - 1){
            if c == '0' {
                left += 1;
            } else {
                right -= 1;
            }
            res = res.max(left + right);
        }
        res
    }
}
```

```java
class Solution {
    public int maxScore(String s) {
        int left = 0;
        int right = 0;
        int res = 0;

        for (char c: s.toCharArray()){
            if (c == '1'){
                right++;
            }
        }
        for (int i = 0; i < s.length() - 1; i++){
            if (s.charAt(i) == '0'){
                left++;
            } else {
                right--;
            }
            res = Math.max(res, left + right);
        }
        return res;   
    }
}
```

```c++
class Solution {
public:
    int maxScore(string s) {
        int left = 0;
        int right = std::count(s.begin(), s.end(), '1');
        int res = 0;
        for (size_t i = 0; i < s.length() - 1; ++i){
            if (s[i] == '0'){
                left++;
            }else{
                right--;
            }
            res = std::max(res, left + right);
        }
        return res;
    }
};
```

```go
func maxScore(s string) int {
    left, right := 0, 0
    for _, ch := range s{
        if ch == '1' {
            right++
        }
    }
    res := 0
    for i := 0; i < len(s) - 1; i++ {
        if s[i] == '0'{
            left++
        } else {
            right--
        }
        if left + right > res {
            res = left + right
        }
    }
    return res
}
```
