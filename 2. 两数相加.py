class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def addTowNumbers(self,l1,l2):
        tmp = dum = ListNode(0)
        carry = 0
        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum = l1.val + carry
                l1 = l1.next
            else:
                sum = l2.val + carry
                l2 = l2.next
            ans = sum % 10
            carry = sum // 10
            tmp.next = ListNode(ans)
            tmp = tmp.next
        if carry:
            tmp.next = ListNode(carry)
        return dum.next

