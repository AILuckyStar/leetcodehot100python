class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def myreverse(self,head,tail):
        pre=tail.next
        p=head
        while pre != tail:
        #while p!=tail.next : tail.next在变
            pnext=p.next
            p.next=pre
            pre=p
            p=pnext
        return head,tail


    def reverseKGroup(self,head,k):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = dummy
        while head:
            for _ in range(k):
                if tail.next:
                    tail = tail.next
                else:
                    return dummy.next
            tail, head = self.myreverse(head, tail)
            pre.next = head
            pre = tail
            head = tail.next
        return dummy.next



