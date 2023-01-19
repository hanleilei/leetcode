# Strong Password Checker II

A password is said to be **strong** if it satisfies all the following criteria:

- It has at least `8` characters.
- It contains at least **one lowercase** letter.
- It contains at least **one uppercase** letter.
- It contains at least **one digit**.
- It contains at least **one special character**. The special characters are the characters in the following string: `"!@#$%^&*()-+"`.
- It does **not** contain `2` of the same character in adjacent positions (i.e., `"aab"` violates this condition, but `"aba"` does not).

Given a string `password`, return `true` *if it is a **strong** password*. Otherwise, return `false`.

**Example 1:**

**Input:** password = "IloveLe3tcode!"
**Output:** true
**Explanation:** The password meets all the requirements. Therefore, we return true.

**Example 2:**

**Input:** password = "Me+You--IsMyDream"
**Output:** false
**Explanation:** The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.

**Example 3:**

**Input:** password = "1aB!"
**Output:** false
**Explanation:** The password does not meet the length requirement. Therefore, we return false.

**Constraints:**

- `1 <= password.length <= 100`
- `password` consists of letters, digits, and special characters: `"!@#$%^&*()-+"`.

直接用题目的含义实现：

```python
import string
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        return any([i for i in password if i in string.ascii_lowercase]) and \
                any([i for i in password if i in string.ascii_uppercase]) and \
                any([i for i in password if i in string.digits]) and \
                any([i for i in password if i  in "!@#$%^&*()-+"]) and \
                len(password) > 7 and \
                all([password[i] != password[i+1] for i in range(len(password) - 1)])
```

换个思路，挨个计算，然后求和

```python
import string
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        if n < 8: return False
        rec = [0] * 4
        special = "!@#$%^&*()-+"
        for i in range(n):
            if i != n - 1 and password[i] == password[i+1]:
                return False
            if password[i] in string.ascii_lowercase and rec[0] == 0:
                rec[0] += 1
            elif password[i] in string.ascii_uppercase and rec[1] == 0:
                rec[1] += 1
            elif password[i] in string.digits and rec[2] == 0:
                rec[2] += 1
            elif password[i] in special and rec[3] == 0:
                rec[3] += 1
        return sum(rec) == 4
```

再来一个cpp的版本：

```cpp
class Solution {
public:
    bool strongPasswordCheckerII(string password) {
        int n = password.size();
        if(n<8){
            return false;
        }
        vector<int> res(4, 0);
        string special = "!@#$%^&*()-+";
        for(int i=0;i<n;i++){
            if(i!=n-2&&password[i]==password[i+1]){
                return false;
            }
            if(password[i]>='a'&&password[i]<='z'&&res[0]==0){
                res[0]++;
            }else if(password[i]>='A'&&password[i]<='Z'&&res[1]==0){
                res[1]++;
            }else if(password[i]>='0'&&password[i]<='9'&&res[2]==0){
                res[2]++;
            }else if(special.find(password[i])!=special.npos&&res[3]==0){
                res[3]++;
            }
        }
        return accumulate(res.begin(), res.end(), 0)==4;
    }
};
```