# add two numbers

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

###### 问题的关键在于，如果某个链表为空，则返回另一个链表。否则就返货两个链表的相应值的和

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        cur = ret

        sum = 0
        while True:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next

            cur.val = sum % 10
            sum /= 10
            if l1 != None or l2 != None or sum != 0:
                cur.next = ListNode(0)
                cur = cur.next
            else:
                break

        return ret
```



下面，我们可以查看一下Python中表示链表的方法：

```Python
class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            print 'linklist is empty.'
            return

        elif key <0  or key > self.getlength():
            print 'the given key is error'
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):

        if self.is_empty():
            print 'linklist is empty.'
            return

        elif key <0  or key > self.getlength():
            print 'the given key is error'
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):

        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):

        self.head = 0


    def append(self,item):

        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getitem(self,index):

        if self.is_empty():
            print 'Linklist is empty.'
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print 'target is not exist!'

    def insert(self,index,item):

        if self.is_empty() or index<0 or index >self.getlength():
            print 'Linklist is empty.'
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p


    def delete(self,index):

        if self.is_empty() or index<0 or index >self.getlength():
            print 'Linklist is empty.'
            return

        if index ==0:
            q = self.head.next

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next

    def index(self,value):

        if self.is_empty():
            print 'Linklist is empty.'
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1


l = LinkList()
l.initlist([1,2,3,4,5])
print l.getitem(4)
l.append(6)
print l.getitem(5)

l.insert(4,40)
print l.getitem(3)
print l.getitem(4)
print l.getitem(5)

l.delete(5)
print l.getitem(5)

l.index(5)

```
此外，下面的代码来自于伯乐在线：

```python
class Node():
    __slots__=['_item','_next']
    def __init__(self,item):
        self._item=item
        self._next=None
    def getItem(self):
        return self._item
    def getNext(self):
        return self._next
    def setItem(self,newitem):
        self._item=newitem
    def setNext(self,newnext):
        self._next=newnext

class SingleLinkedList():   
    def __init__(self):
        self._head=None  #初始化为空链表
    def isEmpty(self): #检查链表是否为空
        return self._head==None
    def size(self):
        current=self._head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    def travel(self):
        current=self._head
        while current!=None:
            print current.getItem()
            current=current.getNext()
    def add(self,item):  #在链表前端添加元素
        temp=Node(item)
        temp.setNext(self._head)
        self._head=temp

    def append(self,item):  #在链表尾部添加元素
        temp=Node(item)
        if self.isEmpty():
            self._head=temp   #若为空表，将添加的元素设为第一个元素
        else:
            current=self._head
            while current.getNext()!=None:
                current=current.getNext()   #遍历链表
            current.setNext(temp)   #此时current为链表最后的元素
    def search(self,item):  搜索元素是否在链表中
        current=self._head
        founditem=False
        while current!=None and not founditem:
            if current.getItem()==item:
                founditem=True
            else:
                current=current.getNext()
        return founditem
    def index(self,item): # 元素在链表中的位置
        current=self._head
        count=0
        found=None
        while current!=None and not found:
            count+=1
            if current.getItem()==item:
                found=True
            else:
                current=current.getNext()
        if found:
            return count
        else:
            raise ValueError,'%s is not in linkedlist'%item                
    def remove(self,item): #链表中删除元素
        current=self._head
        pre=None
        while current!=None:
            if current.getItem()==item:
                if not pre:
                    self._head=current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre=current
                current=current.getNext()                        
    def insert(self,pos,item): #链表中插入元素
        if posself.size():
            self.append(item)
        else:
            temp=Node(item)
            count=1
            pre=None
            current=self._head
            while count
```
