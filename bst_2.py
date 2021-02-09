import sys


class Node:
    def __init__(self,data):
        self.l=self.r=None
        self.data=data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data > root.data:
                cur=self.insert(root.r,data)
                root.r=cur
            else:
                cur=self.insert(root.l,data)
                root.l=cur
        return root

    def levelOrder(self,root):
        if root==None:
           return
        else:
            print(root.data,end=" ")
            stack.append(root.l)
            stack.append(root.r)
            while len(stack) >0:
                self.levelOrder(stack.pop(0))

stack=[]

T=int(input())
tr=Solution()
root=None
for _ in range (T):
    data=int(input())
    root=tr.insert(root,data)
tr.levelOrder(root)
