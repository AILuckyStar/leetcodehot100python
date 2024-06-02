class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def isPalindrome(self,head):
        copy = []
        cur=head
        while cur !=None:
            copy.append(cur.val)
            cur=cur.next
        return copy==copy[::-1]
