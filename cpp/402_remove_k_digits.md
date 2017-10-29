# remove k digits

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

从高到低遍历，如果对应的数字大于下一位数字，就把该位数字去掉，得到的数字最小

```cpp
class Solution {
public:
    std::string removeKdigits(std::string num, int k) {
        std::vector<int> S;
        std::string result = "";                        //store the result
        for (int i =0; i < num.length(); i++){          //scan num
            int number = num[i] -'0';                   //change to std
            while(S.size()!=0 && k>0 && S[S.size()-1] > number){
                S.pop_back();       //when stack is not empty, top of stack greater than number
                k--;
            }
            if (number > 0 || S.size() != 0){
                S.push_back(number);
            }            
        }
        while(S.size()!=0 && k>0){ // handle num = 12345
            S.pop_back();
            k--;
        }
        for(int i = 0; i< S.size(); i++){ //handle
            result.append(1, '0'+S[i]);
        }
        if(result == ""){
            result = "0";//若result为空，result即为0
        }
        return result;
    }
};
```
当然有看到一个解法，更是巧妙，注意for循环里面的while循环，可以作为向后遍历。

```cpp
class Solution {
public:
    string removeKdigits(string num, int k) {
        string res = "";
        int n = num.size(), keep = n - k;
        for (char c : num) {
            while (k && res.size() && res.back() > c) {
                res.pop_back();
                --k;
            }
            res.push_back(c);
        }
        res.resize(keep);
        while (!res.empty() && res[0] == '0') res.erase(res.begin());
        return res.empty() ? "0" : res;
    }
};

```
