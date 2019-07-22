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


class Node:
    def __init__(sel f,val):
        self.val=val
        self.next=Nonezx

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


