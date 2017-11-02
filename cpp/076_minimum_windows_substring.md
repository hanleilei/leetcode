# minimum windows substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.



```cpp
class Solution {
private:
    bool is_window_ok(int map_s[], int map_t[], std::vector<int> &vec_t){
        for (int i = 0; i < vec_t.size(); i++){
            if(map_s[vec_t[i]] < map_t[vec_t[i]]){
                return false;
            }
        }
    }

public:
    string minWindow(string s, string t) {
        const int MAX_ARRAY_LEN = 128;
        int map_t[MAX_ARRAY_LEN] = {0};
        int map_s[MAX_ARRAY_LEN] = {0};
        std::vector<int> vec_t;
        for (int i = 0; i < t.length(); i++){
            map_t[t[i]]++;
        }
        for (int i = 0; i < MAX_ARRAY_LEN; i++) {
            if(map_t[i] > 0){
                vec_t.push_back();
            }
        }
        int window_begin = 0;
        std::string result;

        for (int i = 0; i < s.length(); i++) {
            map_s[s[i]]++;
            while (window_begin < i) {
                char begin_ch = s[window_begin];
                if (map_t[begin_ch] == 0) {
                    window_begin++
                }
                else if(map_s[begin_ch] > map_t[begin_ch]){
                    map_s[begin_ch]--;
                    window_begin++;
                }else{
                    break;
                }
            }
            if (is_window_ok(map_s, map_t, vec_t)) {    
                int new_window_len = i - window_begin + 1;
                if (result == ''|| result.length() > new_window_len) {
                    result = s.substr(window_begin, new_window_len);
                }
            }
        }
    }
};
```
