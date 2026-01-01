

```python
def divide_conquer(problem, param1, param2,...):
    
    # recursion terminator
    if problem is None:
        print_result
        return
    
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems
    subresult1 = divide_conquer(subproblems[0], p1, ...)
    subresult2 = divide_conquer(subproblems[1], p1, ... )
    subresult3 = divide_conquer(subproblems[2], p1, ...)
    ...
    subresultN = divide_conquer(subproblems[N], p1, ...)

    # process and generate the final result
    result = process_result(subresult1, subresult2,..., subresultN)
```
