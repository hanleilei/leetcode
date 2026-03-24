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
    process_data(level, data, ...)

    # drill down
    self.recursion(level + 1, p1, ...)

    # reverse the current level status if needed.
    # clear status
    reverse_state(level)
```

这样看来，回溯，递归和分治算法的框架是非常相似的，区别在于：

- 分治算法需要将问题拆分成多个子问题，然后分别解决，聚合结果；
- 递归通常只处理一个子问题，或者在处理多个子问题时不需要聚合结果；
- 回溯则是在递归的基础上增加了状态重置的步骤，以便在探索不同的路径时能够回到之前的状态。
