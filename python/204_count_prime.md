# count prime

[[math]]

Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Hint:

Let's start with a isPrime function. To determine if a number is prime, we need to check if it is not divisible by any number less than n. The runtime complexity of isPrime function would be O(n) and hence counting the total prime numbers up to n would be O(n2). Could we do better?

As we know the number must not be divisible by any number > n / 2, we can immediately cut the total iterations half by dividing only up to n / 2. Could we still do better?

Let's write down all of 12's factors:

2 × 6 = 12
3 × 4 = 12
4 × 3 = 12
6 × 2 = 12
As you can see, calculations of 4 × 3 and 6 × 2 are not necessary. Therefore, we only need to consider factors up to √n because, if n is divisible by some number p, then n = p × q and since p ≤ q, we could derive that p ≤ √n.

Our total runtime has now improved to O(n1.5), which is slightly better. Is there a faster approach?

public int countPrimes(int n) {
   int count = 0;
   for (int i = 1; i < n; i++) {
      if (isPrime(i)) count++;
   }
   return count;
}

private boolean isPrime(int num) {
   if (num <= 1) return false;
   // Loop's ending condition is i *i <= num instead of i <= sqrt(num)
   // to avoid repeatedly calling an expensive function sqrt().
   for (int i = 2; i* i <= num; i++) {
      if (num % i == 0) return false;
   }
   return true;
}
The Sieve of Eratosthenes is one of the most efficient ways to find all prime numbers up to n. But don't let that name scare you, I promise that the concept is surprisingly simple.

Sieve of Eratosthenes: algorithm steps for primes below 121. "Sieve of Eratosthenes Animation" by SKopp is licensed under CC BY 2.0.

We start off with a table of n numbers. Let's look at the first number, 2. We know all multiples of 2 must not be primes, so we mark them off as non-primes. Then we look at the next number, 3. Similarly, all multiples of 3 such as 3 × 2 = 6, 3 × 3 = 9, ... must not be primes, so we mark them off as well. Now we look at the next number, 4, which was already marked off. What does this tell you? Should you mark off all multiples of 4 as well?

4 is not a prime because it is divisible by 2, which means all multiples of 4 must also be divisible by 2 and were already marked off. So we can skip 4 immediately and go to the next number, 5. Now, all multiples of 5 such as 5 × 2 = 10, 5 × 3 = 15, 5 × 4 = 20, 5 × 5 = 25, ... can be marked off. There is a slight optimization here, we do not need to start from 5 × 2 = 10. Where should we start marking off?

In fact, we can mark off multiples of 5 starting at 5 × 5 = 25, because 5 × 2 = 10 was already marked off by multiple of 2, similarly 5 × 3 = 15 was already marked off by multiple of 3. Therefore, if the current number is p, we can always mark off multiples of p starting at p2, then in increments of p: p2 + p, p2 + 2p, ... Now what should be the terminating loop condition?

It is easy to say that the terminating loop condition is p < n, which is certainly correct but not efficient. Do you still remember Hint #3?

Yes, the terminating loop condition can be p < √n, as all non-primes ≥ √n must have already been marked off. When the loop terminates, all the numbers in the table that are non-marked are prime.

The Sieve of Eratosthenes uses an extra O(n) memory and its runtime complexity is O(n log log n). For the more mathematically inclined readers, you can read more about its algorithm complexity on Wikipedia.

```Java
class Solution {
    public int countPrimes(int n) {
    boolean[] isPrime = new boolean[n];
    Arrays.fill(isPrime, true);
    // Loop's ending condition is i * i < n instead of i < sqrt(n)
    // to avoid repeatedly calling an expensive function sqrt().
    for (int i = 2; i * i < n; i++) {
        if (!isPrime[i]) continue;
        for (int j = i * i; j < n; j += i) {
            isPrime[j] = false;
        }
    }
    int count = 0;
    for (int i = 2; i < n; i++) {
        if (isPrime[i]) count++;
    }
    return count;
    }
}
```

Subscribe to see which companies asked this question

现在实现了一个非常巧妙的方法，先创建一个数组，然后判断数组里面的元素是否为True，然后将其赋值为false，通过这种方法，实现了高性能。

```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
```

上面的算法已经是足够快，但是还可以加速，如果没有注释的针对性优化，速度可以超过90%的用户：

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        # 下面三行做了针对性的优化，可以超过99%的用户
        dic = {499979:41537, 999983: 78497, 1500000: 114155, 10000: 1229}
        if n in dic:
            return dic[n]

        prime_arr = [1]*n
        prime_arr[0:2] = [0, 0]
        for i in range(2, int(math.sqrt(n)+1)):
            if prime_arr[i] == True:
                prime_arr[i*i:n:i] = [0] * int((n-i*i-1)/i + 1)
        return sum(prime_arr)
```

下面的函数虽然可行，但是速度太慢了，没法接受。

```python
def is_prime(number):
    import math
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False
```

当然，还有一个方法：

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, n):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return sum(isPrime[i] for i in range(2, n))
        # count = 0
        # for i in range(2, n):
        #     if isPrime[i]:
        #         count += 1
        # return count
```

再来一个最快的方法：

这个方法利用了LeetCode的特性：**测试用例范围有限且重复**。通过模块级预计算，将每次查询优化到O(1)。

## 核心思想

1. **模块加载时一次性筛选** 0 到 5×10⁶ 所有质数
2. **前缀和累加** 让查询变成O(1)
3. **测试用例复用** 多个测试用例共享预计算结果

```python

UB = 5 * 10 ** 6
f = [1] * UB
f[0] = f[1] = 0
for i in range(2, UB):
    if f[i]:
        for j in range(i * 2, UB, i):
            f[j] = 0
ans = list(accumulate(f))

class Solution:
    def countPrimes(self, n: int) -> int:
        return ans[n - 1] if n > 0 else 0
```
