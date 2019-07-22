# Stack
class Stack:
    def __init__(self):
        self.data=[]
    def push(self,val):
        self.data.append(val)
    def pop(self):
        return self.data.pop()
    def __str__(self):
        return str(self.data)
    def getsize(self):
        return len(self.data)
    def isempty(self):
        return len(self.data)==0

# s1=Stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)
# s1.push(4)
# print(s1.getsize())
# print(s1.pop())
# print(s1.isempty())
# print(s1)



# queue
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.size=0
    def enqueue(self,val):
        newNode = Node(val)
        if self.end==None:
            self.start = newNode
            self.end = newNode
        else:
            self.end.next=newNode
            self.end=newNode
        self.size+=1
    def dequeue(self):
        if self.start==None:
            pass
        elif self.start==self.end:
            self.start=None
            self.end=None
            self.size-=1
        else:
            self.start=self.start.next
            self.size-=1

    def __str__(self):
        s=""
        current=self.start
        while current!=None:
            s+=str(current.val)+"->"
            current=current.next
        return s
    def count(self):
        return self.size
    def __len__(self):
        return self.size
# q1=Queue()
# q1.enqueue(1)
# q1.enqueue(2)
# q1.enqueue(3)
# q1.enqueue(4)
# q1.dequeue()
# print(q1.count())
# print(len(q1))
# print(q1)
#
# arr=[1,2,3]
# arr2=arr
# arr3=list(arr)
# print(arr==arr2)
# print(arr is arr2)
# print(arr==arr3)
# print(arr is arr3)

class Queueusingstack:
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
    def enque(self,val):
        self.s1.push(val)
    def deque(self):
        if self.s2.isempty():
            while not self.s1.isempty():
                elem=self.s1.pop()
                self.s2.push(elem)
        return self.s2.pop()
    def __str__(self):
        return str(self.s2.data[::-1]+self.s1.data)
# q1=Queueusingstack()
# q1.enque(1)
# q1.enque(2)
# q1.enque(3)
# q1.enque(4)
# q1.deque()
# print(q1)





