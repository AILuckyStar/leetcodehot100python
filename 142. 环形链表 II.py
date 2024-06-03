class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def detectCycle(self,head):
        if head==None or head.next==None:
            return None
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break
        if fast==slow:
            fast=head
            while fast!=slow:
                fast=fast.next
                slow=slow.next
            return fast
        return None
a1=ListNode(3)
a2=ListNode(2)
a3=ListNode(0)
a4=ListNode(-4)
a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a2
s=Solution()
print(s.detectCycle(a1).val)

