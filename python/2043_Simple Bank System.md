# Simple Bank System

[[design]] [[array]]

You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has `n` accounts numbered from 1 to n. The initial balance of each account is stored in a **0-indexed** integer array `balance`, with the (i + 1)th account having an initial balance of `balance[i]`.

Execute all the valid transactions. A transaction is **valid** if:

1. The given account number(s) are between 1 and n, and
2. The amount of money withdrawn or transferred from is less than or equal to the balance of the account.

## Class Interface

Implement the `Bank` class:

- **`Bank(long[] balance)`** Initializes the object with the 0-indexed integer array balance.
- **`boolean transfer(int account1, int account2, long money)`** Transfers money dollars from account1 to account2. Return true if successful.
- **`boolean deposit(int account, long money)`** Deposit money dollars into the account. Return true if successful.
- **`boolean withdraw(int account, long money)`** Withdraw money dollars from the account. Return true if successful.

## Examples

### Example 1

```text
Input:
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]

Output:
[null, true, true, true, false, false]

Explanation:
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // return true, account 3 has $20, valid to withdraw $10
                         // Account 3: $20 - $10 = $10
bank.transfer(5, 1, 20); // return true, account 5 has $30, valid to transfer $20
                         // Account 5: $30 - $20 = $10, Account 1: $10 + $20 = $30
bank.deposit(5, 20);     // return true, always valid to deposit
                         // Account 5: $10 + $20 = $30
bank.transfer(3, 4, 15); // return false, account 3 has $10, invalid to transfer $15
bank.withdraw(10, 50);   // return false, account 10 does not exist
```

## Constraints

- `n == balance.length`
- `1 <= n, account, account1, account2 <= 10^5`
- `0 <= balance[i], money <= 10^12`
- At most 10^4 calls will be made to each function

## 解题思路

这是一道设计题，核心是模拟银行系统的基本操作。需要注意：

1. **账户编号**：题目中账户编号从1开始，但数组索引从0开始
2. **有效性检查**：每个操作都需要检查账户是否存在和余额是否充足
3. **原子性**：转账操作要么完全成功，要么完全失败

## 解法一：直接模拟

```python
class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)
    
    def _is_valid_account(self, account: int) -> bool:
        """检查账户号是否有效"""
        return 1 <= account <= self.n
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """转账操作"""
        # 检查两个账户是否都有效
        if not self._is_valid_account(account1) or not self._is_valid_account(account2):
            return False
        
        # 检查转出账户余额是否充足
        if self.balance[account1 - 1] < money:
            return False
        
        # 执行转账
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True
    
    def deposit(self, account: int, money: int) -> bool:
        """存款操作"""
        if not self._is_valid_account(account):
            return False
        
        self.balance[account - 1] += money
        return True
    
    def withdraw(self, account: int, money: int) -> bool:
        """取款操作"""
        if not self._is_valid_account(account):
            return False
        
        # 检查余额是否充足
        if self.balance[account - 1] < money:
            return False
        
        self.balance[account - 1] -= money
        return True
```

## 解法二：优化版（减少重复代码）

```python
class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # 使用短路求值优化条件检查
        if (1 <= account1 <= self.n and 1 <= account2 <= self.n and 
            self.balance[account1 - 1] >= money):
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False
    
    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n:
            self.balance[account - 1] += money
            return True
        return False
    
    def withdraw(self, account: int, money: int) -> bool:
        if (1 <= account <= self.n and 
            self.balance[account - 1] >= money):
            self.balance[account - 1] -= money
            return True
        return False
```

## 解法三：函数式风格

```python
class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)
    
    def _validate_and_execute(self, account: int, money: int, operation: str, target_account: int = None) -> bool:
        """通用的验证和执行函数"""
        if not (1 <= account <= self.n):
            return False
        
        if target_account is not None and not (1 <= target_account <= self.n):
            return False
        
        if operation in ['withdraw', 'transfer'] and self.balance[account - 1] < money:
            return False
        
        if operation == 'deposit':
            self.balance[account - 1] += money
        elif operation == 'withdraw':
            self.balance[account - 1] -= money
        elif operation == 'transfer':
            self.balance[account - 1] -= money
            self.balance[target_account - 1] += money
        
        return True
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        return self._validate_and_execute(account1, money, 'transfer', account2)
    
    def deposit(self, account: int, money: int) -> bool:
        return self._validate_and_execute(account, money, 'deposit')
    
    def withdraw(self, account: int, money: int) -> bool:
        return self._validate_and_execute(account, money, 'withdraw')
```

## 解法四：

```python
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance        
        self.size = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.size or account2 > self.size:
            return False
        if self.balance[account1-1] >= money:
            self.balance[account1-1] -= money
            self.balance[account2-1] += money   
            return True     
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account > self.size: return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.size: return False
        if self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        return False
```

## 复杂度分析

| 操作 | 时间复杂度 | 空间复杂度 |
|------|------------|------------|
| 初始化 | O(1) | O(n) |
| transfer | O(1) | O(1) |
| deposit | O(1) | O(1) |
| withdraw | O(1) | O(1) |

## 关键要点

1. **索引转换**：账户号 `account` 对应数组索引 `account - 1`
2. **边界检查**：确保账户号在 `[1, n]` 范围内
3. **余额验证**：转账和取款前检查余额是否充足
4. **原子操作**：每个操作要么完全成功，要么完全失败
5. **代码简洁性**：使用短路求值减少条件检查的复杂度

## 易错点

1. **忘记账户号从1开始**：`account` 对应 `balance[account-1]`
2. **转账时只检查一个账户**：需要同时验证转出和转入账户
3. **余额检查时机**：必须在修改余额之前检查
4. **边界条件处理**：账户号为0或超出范围的情况

## 相关题目

- [146. LRU Cache](146_LRU_cache.md) - 数据结构设计
- [208. Implement Trie](208_implement_trie.md) - 树结构设计
- [380. Insert Delete GetRandom O(1)](380_insert_delete_getrandom.md) - 数据结构设计

这道题考查的是系统设计能力和边界条件处理，推荐掌握直接模拟法，代码简洁易懂。
