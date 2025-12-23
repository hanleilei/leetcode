# Linked List

## 头插法

头插法是一种构建链表的方法，新节点总是插入到链表的头部，也就是 dummy 节点的后面。

```python
dummy.next = ListNode(val, dummy.next) # 头插法
```

等价于：

```python
# 创建新节点，其next指向当前dummy.next
new_node = ListNode(val, dummy.next)
# 将新节点设为dummy的下一个节点
dummy.next = new_node
```
