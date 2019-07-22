class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,val):
        newNode=Node(val)
        if self.root is None:
            self.root=newNode
        else:
            self._insert(self.root,newNode)
    def _insert(self,startnode,newNode):
        if newNode.val==startnode.val:
            return
        elif startnode.val<newNode.val:
            if startnode.right is None:
                startnode.right=newNode
            else:
                self._insert(startnode.right,newNode)
        else:
            if startnode.left is None:
                startnode.left=newNode
            else:
                self._insert(startnode.left,newNode)
    def printdf(self):
        self._printdf(self.root)
    def _printdf(self,currNode):
        if currNode is None:
            return
        self._printdf(currNode.left)
        print(currNode.val)
        self._printdf(currNode.right)
    def printbf(self):
        if self.root is None:
            return
        q=[]
        q.append(self.root)
        while len(q) >0:
            node=q.pop(0)
            print(node.val)
            if not node.left is None:
                q.append(node.left)
            if not node.right is None:
                q.append(node.right)
    def search(self,val):
        return self._search(self.root,val)
    def _search(self,currNode,val):
        if currNode is None:
            return False
        if currNode.val==val:
            return True
        elif currNode.val<val:
           return self._search(currNode.right,val)
        else:
            return self._search(currNode.left,val)


t1=BST()
t1.insert(5)
t1.insert(7)
t1.insert(3)
t1.insert(4)
t1.insert(9)
t1.insert(2)
print(t1.search(3))
t1.printbf()