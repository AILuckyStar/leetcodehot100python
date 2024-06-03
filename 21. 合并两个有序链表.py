class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def mergeTowLists(self,list1,list2):
        cur=dum=ListNode(0)
        while list1 and list2:
            if list1.val<=list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        cur.next=list1 if list2==None else list2
        return dum.next
