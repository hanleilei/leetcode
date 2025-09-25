# Next Palindrome Using Same Digits

## Statement

Given a numeric string, `num_str`, representing a palindrome (composed only of digits). Return the smallest palindrome larger than `num_str` that can be created by rearranging its digits. If no such palindrome exists, return an empty string `""`.

Consider the following example to understand the expected output for a given numeric string:

- input string = `"123321"`

- The valid palindromes made from the exact digits are `"213312"`, `"231132"`, `"312213"`, `"132231"`, `"321123"`.

- We return the palindrome `"132231"` because it is the smallest palindrome larger than the input string `"123321"`.

**Constraints:**

- 1≤ `num_str.length` ≤105

- `num_str` is a palindrome.

## Examples

"1234321" -> "1324231"

## Solution

1. Start from the middle of the number and find the first digit (from right to left) that is smaller than the digit next to it.

2. If no such digit exists, there is no higher palindrome possible, return an empty string.

3. Otherwise, find the smallest digit on the right that is larger than this digit and swap them.

4. Reverse the part after the swapped digit to get the next greater sequence for the left half.

5. Mirror the updated left half (with the middle digit if length is odd) to form a new palindrome and return it if it’s greater than the original. 

```python
def find_next_permutation(digits):
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i == -1:
        return False

    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    return True

def find_next_palindrome(num_str):
    n = len(num_str)

    if n == 1:
        return ""

    half_length = n // 2
    left_half = list(num_str[:half_length])

    if not find_next_permutation(left_half):
        return ""

    if n % 2 == 0:
        next_palindrome = ''.join(left_half + left_half[::-1])
    else:
        middle_digit = num_str[half_length]
        next_palindrome = ''.join(left_half + [middle_digit] + left_half[::-1])

    if next_palindrome > num_str:
        return next_palindrome
    return ""
```
