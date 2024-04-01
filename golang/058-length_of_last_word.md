# length of last world

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

字符串操作之抖机灵

```go
func lengthOfLastWord(s string) int {
    s = strings.TrimRight(s, " ")
        
    return len(s) -1 - strings.LastIndex(s, " ")
}
```

```go
func lengthOfLastWord(s string) int {
    n := len(s)
    count := 0
    for i := n - 1; i >= 0; i-- {
        if count == 0 && s[i] == ' '{
            continue
        } else {
            if s[i] == ' ' {
                break
            }
            count++
        }
    }
    return count
}
```
