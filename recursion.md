# recursion

一般来说，就是间接的调用自身：

```python
def recursive_function(params):
    # 基本情况（终止条件）
    if base_case_condition:
        # process result
        return base_case_value  

    # 处理当前层的逻辑
    modified_params = modify_params(params)

    # 递归情况
    recursive_function(modified_params + 1)
```

注意：

1. 不要人肉递归（每次调用都要新建一个函数栈）
2. 找到最近最简单的方法，将其拆解为更小的子问题（可重复解决的问题）- 最近重复性
3. 数学归纳法思维（假设函数能正确处理更小的输入）
4. 明确递归的终止条件，防止无限递归

```python
def recursion(level, param1, param2, ..):
    # recursion terminator
    if level > max_level:
        print_result
        return
    
    # process login in current level
    process_data(level, data)

    # drill down
    self.recursion(level + 1, p1, ...)

    # reverse the current level status if needed.
    reverse_state(level)
```