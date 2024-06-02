class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def getIntersectionNode(self,headA,headB):
        tempA=headA
        tempB=headB
        while tempA !=tempB:
            if tempA==None:
                tempA=headB
            else:
                tempA = tempA.next
            if tempB==None:
                tempB=headA
            else:
                tempB=tempB.next
        return tempA
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
print(s.getIntersectionNode(a1,b1).val)
