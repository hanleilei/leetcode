# Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

```
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
```

Example 2:

```
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> st;
        st.push_back(-1);

        int res = 0;

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                st.push_back(i);
            } else {
                st.pop_back();

                if (st.empty()) {
                    st.push_back(i);
                } else {
                    res = max(res, i - st.back());
                }
            }
        }

        return res;
    }
};
```

```cpp
class Solution {
public:
    int longestValidParentheses(std::string s) {
        int n = (int)s.size();
        vector<char> is_valid(n, 0);
        stack<int> st; // 未配对的左括号的下标

        for (int i = 0; i < n; ++i) {
            if (s[i] == '(') {
                st.push(i); // 保存左括号的下标
            } else if (!st.empty()) {
                int j = st.top(); // 右括号与栈顶的左括号配对
                st.pop();

                is_valid[i] = 1;
                is_valid[j] = 1;
            }
        }

        int ans = 0, cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (is_valid[i]) {
                ++cnt; // 连续 True 的个数
                ans = std::max(ans, cnt);
            } else {
                cnt = 0; // 重置计数器
            }
        }

        return ans;
    }
};
```
