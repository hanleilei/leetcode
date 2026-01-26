# Preimage Size of Factorial Zeroes Function

[[binarysearch]]

## Problem Description

Let `f(x)` be the number of zeroes at the end of `x!`. Recall that `x! = 1 * 2 * 3 * ... * x` and by convention, `0! = 1`.

- For example, `f(3) = 0` because `3! = 6` has no zeroes at the end, while `f(11) = 2` because `11! = 39916800` has two zeroes at the end.

Given an integer `k`, return *the number of non-negative integers* `x` *that have the property that* `f(x) = k`.

**Example 1:**

**Input:** k = 0
**Output:** 5
**Explanation:** 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.

**Example 2:**

**Input:** k = 5
**Output:** 0
**Explanation:** There is no x such that x! ends in k = 5 zeroes.

**Example 3:**

**Input:** k = 3
**Output:** 5

**Constraints:**

- `0 <= k <= 10^9`

---

## Key Insights

### Understanding Trailing Zeros in Factorials

The number of trailing zeros in `n!` is determined by the number of times 10 is a factor in the product. Since `10 = 2 × 5`, we need pairs of 2s and 5s. There are always more 2s than 5s in factorials, so we only need to count 5s.

**Formula to count trailing zeros in n!:**

```
f(n) = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ⌊n/625⌋ + ...
```

**Example:** For n = 11:

- ⌊11/5⌋ = 2
- ⌊11/25⌋ = 0
- Total: f(11) = 2

### Why Binary Search?

**Observation 1:** `f(x)` is a monotonically non-decreasing function

- If x₁ < x₂, then f(x₁) ≤ f(x₂)

**Observation 2:** The answer is either 0 or 5

- `f(x)` increases by 1 every 5 consecutive numbers (except at multiples of 25, 125, etc.)
- When f(x) = k exists, there are exactly 5 consecutive values of x where f(x) = k
- Some values of k are "skipped" (e.g., k = 5 is impossible because f(4) = 0 and f(5) = 1)

---

## Solution Approaches

### Approach 1: Binary Search with Trailing Zero Count (Optimal)

**Algorithm:**

1. Use binary search to find if any x exists where f(x) = k
2. Calculate trailing zeros using the formula
3. If found, return 5; otherwise return 0

**Time Complexity:** O(log²k) - binary search O(log k) × counting zeros O(log k)
**Space Complexity:** O(1)

```python
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_trailing_zeros(n: int) -> int:
            """Count trailing zeros in n!"""
            count = 0
            power_of_5 = 5
            while power_of_5 <= n:
                count += n // power_of_5
                power_of_5 *= 5
            return count
        
        # Binary search for x where f(x) = k
        left, right = 0, 5 * k
        
        while left <= right:
            mid = left + (right - left) // 2
            zeros = count_trailing_zeros(mid)
            
            if zeros == k:
                return 5  # Found k, so there are exactly 5 values
            elif zeros < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return 0  # k is not achievable
```

### Approach 2: Cleaner Binary Search Implementation

**Alternative implementation** with separate helper function:

```python
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailing_zeros(n: int) -> int:
            """Calculate number of trailing zeros in n!"""
            result = 0
            while n > 0:
                n //= 5
                result += n
            return result
        
        def binary_search(target: int) -> bool:
            """Check if any x exists where f(x) = target"""
            left, right = 0, 5 * target
            
            while left <= right:
                mid = (left + right) // 2
                zeros = trailing_zeros(mid)
                
                if zeros == target:
                    return True
                elif zeros < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return False
        
        return 5 if binary_search(k) else 0
```

### Approach 3: Binary Search with Early Bounds

**Optimization:** Use tighter bounds for binary search

```python
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_zeros(n: int) -> int:
            """Count trailing zeros in n!"""
            count = 0
            divisor = 5
            while divisor <= n:
                count += n // divisor
                divisor *= 5
            return count
        
        # Use binary search to find lower bound
        left, right = 0, 5 * (k + 1)
        
        while left < right:
            mid = left + (right - left) // 2
            zeros = count_zeros(mid)
            
            if zeros < k:
                left = mid + 1
            else:
                right = mid
        
        # Check if f(left) equals k
        return 5 if count_zeros(left) == k else 0
```

---

## Detailed Explanation

### Why is the answer always 0 or 5?

Consider how `f(x)` changes:

| x | x! | Trailing Zeros f(x) |
|---|----|--------------------|
| 0-4 | 1, 1, 2, 6, 24 | 0 |
| 5-9 | 120, 720, 5040, 40320, 362880 | 1 |
| 10-14 | ... | 2 |
| 15-19 | ... | 3 |
| 20-24 | ... | 4 |
| 25-29 | ... | 6 (skips 5!) |

**Key Observation:**

- For most ranges, f(x) increases by 1 for every 5 consecutive numbers
- At multiples of 25, 125, etc., f(x) jumps by more than 1
- This creates "gaps" - some values of k are impossible

### Why use upper bound `5 * k`?

Since f(x) ≥ x/5 approximately, if f(x) = k, then x ≈ 5k. Using 5k as upper bound is safe and efficient.

---

## Key Takeaways

1. **Trailing zeros** in n! = count of factor 5 in n! = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ...
2. **Binary search** is applicable because f(x) is monotonically increasing
3. **Answer is binary**: either 0 (impossible k) or 5 (exactly 5 values)
4. **Some k values are unreachable** due to jumps at multiples of 25, 125, etc.

## Related Problems

- LeetCode 172: Factorial Trailing Zeroes (prerequisite problem)
- LeetCode 233: Number of Digit One
- LeetCode 1015: Smallest Integer Divisible by K

---

## Complexity Analysis

| Metric | Value | Explanation |
|--------|-------|-------------|
| Time | O(log²k) | Binary search O(log k) × counting O(log k) |
| Space | O(1) | Only constant variables |

```python
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        start, end = 0, 5 * k
        while end >= start:
            mid = start + (end - start) // 2
            n = 5
            nums = 0
            while n <= mid:
                nums += mid // n
                n *= 5
            if nums == k:
                return 5
            if nums < k:
                start = mid + 1
            else:
                end = mid - 1
        return 0
```
