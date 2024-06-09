class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
        self.random=None

class Solution:
    def copyRandomList(self,head):
        if head==None:
            return None
        cur=head
        dic={}
        dic[None]=None
        while cur:
            dic[cur]=ListNode(cur.val)
            cur=cur.next
        cur=head
        while cur:
            dic[cur].next=dic[cur.next]
            dic[cur].random=dic[cur.random]
            cur = cur.next
        return dic[head]
