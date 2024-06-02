class ListNode:
    def __init__(self,x):
        self.val=x
        self.next =None
class Solution:
    def reveseList(self,head):
        pre=None
        cur=head
        while cur!=None:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        return pre
a1 = ListNode(2)
a2=ListNode(6)
c=ListNode(4)
b1=ListNode(1)
a1.next=a2
a2.next=c
b1.next=c
d=ListNode(7)
c.next=d
s=Solution()
p=s.reveseList(a1)
while p:
    print(p.val)
    p=p.next
