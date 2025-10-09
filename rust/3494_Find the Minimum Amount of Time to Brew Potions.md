# Find the Minimum Amount of Time to Brew Potions

[[dp]] [[prefixSum]]

You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.

 

Example 1:

Input: skill = [1,5,2,4], mana = [5,1,4,2]

Output: 110

Explanation:

| i   | skill[i] | lastFinish[i] | 完成时间        |
| :-- | :------- | :------------ | :-------------- |
| 0   | 1        | 5             | 5+1=6           |
| 1   | 5        | 30            | max(6,30)+5=35  |
| 2   | 2        | 40            | max(35,40)+2=42 |
| 3   | 4        | 60            | max(42,60)+4=64 |

As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.

Example 2:

Input: skill = [1,1,1], mana = [1,1,1]

Output: 5

Explanation:

Preparation of the 0th potion begins at time t = 0, and is completed by time t = 3.
Preparation of the 1st potion begins at time t = 1, and is completed by time t = 4.
Preparation of the 2nd potion begins at time t = 2, and is completed by time t = 5.
Example 3:

Input: skill = [1,2,3,4], mana = [1,2]

Output: 21

 

Constraints:

n == skill.length
m == mana.length
1 <= n, m <= 5000
1 <= mana[i], skill[i] <= 5000
 
## 解法：

凸包优化​

```rust
impl Solution {
    pub fn min_time(skill: Vec<i32>, mana: Vec<i32>) -> i64 {
        let mut s = vec![0];
        for &x in &skill {
            s.push(s.last().unwrap() + x);
        }
        
        // 计算凸包（Andrew 算法）
        let mut hull: Vec<(i64, i64)> = Vec::new();
        for (i, &sum) in s.iter().enumerate() {
            let p = (sum as i64, skill.get(i).unwrap_or(&0).clone() as i64);
            while hull.len() >= 2 {
                let a = hull[hull.len() - 2];
                let b = hull[hull.len() - 1];
                if (b.0 - a.0) * (p.1 - b.1) >= (b.1 - a.1) * (p.0 - b.0) {
                    hull.pop();
                } else {
                    break;
                }
            }
            hull.push(p);
        }

        let mut prev = 0i64;
        for i in 1..mana.len() {
            let pre = mana[i - 1] as i64;
            let cur = mana[i] as i64;
            let p = (pre - cur, pre);

            // 二分查找最大值
            let mut left = 0;
            let mut right = hull.len() - 1;
            while left < right {
                let mid = (left + right) / 2;
                if p.0 * hull[mid].0 + p.1 * hull[mid].1 > p.0 * hull[mid + 1].0 + p.1 * hull[mid + 1].1 {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            prev += p.0 * hull[left].0 + p.1 * hull[left].1;
        }
        prev + s.last().unwrap().clone() as i64 * mana.last().unwrap().clone() as i64
    }
}
```

改用单调栈优化​​

```rust
// 类似 Python 的第一个优化方法
impl Solution {
    pub fn min_time(skill: Vec<i32>, mana: Vec<i32>) -> i64 {
        let mut s = vec![0];
        for &x in &skill {
            s.push(s.last().unwrap() + x);
        }

        // 预处理关键点（单调栈）
        let mut pre_record = vec![0];
        for i in 1..skill.len() {
            if skill[i] > skill[pre_record[pre_record.len() - 1]] {
                pre_record.push(i);
            }
        }

        let mut suf_record = vec![skill.len() - 1];
        for i in (0..skill.len() - 1).rev() {
            if skill[i] > skill[suf_record[suf_record.len() - 1]] {
                suf_record.push(i);
            }
        }

        let mut prev = 0i64;
        for i in 1..mana.len() {
            let pre = mana[i - 1] as i64;
            let cur = mana[i] as i64;
            let record = if pre < cur { &pre_record } else { &suf_record };
            let mut max_val = i64::MIN;
            for &j in record {
                max_val = max_val.max(pre * s[j + 1] as i64 - cur * s[j] as i64);
            }
            prev += max_val;
        }
        prev + s.last().unwrap().clone() as i64 * mana.last().unwrap().clone() as i64
    }
}
```
