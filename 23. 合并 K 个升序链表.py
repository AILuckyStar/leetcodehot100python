class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def merge2(self,head1,head2):
        dummy=ListNode(-1)
        pre=dummy
        while head1 and head2:
            if head1.val<head2.val:
                pre.next=head1
                head1=head1.next
            else:
                pre.next=head2
                head2=head2.next
            pre=pre.next
        pre.next=head1 if head1 else head2
        return dummy.next
    def mergeKList(self,lists):
        partcount=len(lists)
        if partcount < 1:
            return None
        while partcount>1:
            idx=0
            for i in range(0,partcount,2):
                if i==partcount-1:
                    lists[idx]=lists[i]
                    idx+=1
                else:
                    lists[idx]=self.merge2(lists[i],lists[i+1])
                    idx+=1
            partcount=idx
        return lists[0]

