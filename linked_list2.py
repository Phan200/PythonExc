class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def insert(self,head,data):
        p=Node(data)
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while start.next!=None:
                start=start.next
            start.next=p
        return head
    def display(self,head):
        cur=head
        while cur:
            print(cur.data,end=" ")
            cur= cur.next
    def removeDuplicates(self,head):
        arr=[]
        cur=head
        while cur:
            if cur.data not in arr:
                arr.append(cur.data)

            while 1:
                if cur.next != None and cur.next.data in arr:
                    cur.next=cur.next.next
                    continue
                else: break
            cur=cur.next

        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);