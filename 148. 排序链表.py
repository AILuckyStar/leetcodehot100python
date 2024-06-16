class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        dummpy = ListNode(-1)
        dummpy.next = head
        length = 0
        sonlen = 1
        while head:
            length += 1
            head = head.next
        while sonlen < length:
            pre = dummpy
            head = dummpy.next
            while head:
                head1 = head
                partlen = sonlen
                while partlen and head:  # 正常完事儿head就到下一个头了
                    head = head.next
                    partlen -= 1
                if partlen != 0:  # 第一个头的链表长度不够，直接上一层
                    break
                head2 = head
                partlen = sonlen
                while partlen and head:  # 找下一个头1，或者现在的头2长度不够
                    head = head.next
                    partlen -= 1
                partlen1 = sonlen
                partlen2 = sonlen - partlen
                #有用 因为链表没截断
                while partlen1 and partlen2:
                    if head1.val<head2.val:
                        pre.next=head1
                        head1=head1.next
                        partlen1-=1
                    else:
                        pre.next=head2
                        head2=head2.next
                        partlen2-=1
                    pre=pre.next
                # 连接剩余，并走到尾部
                if partlen1:
                    pre.next=head1
                    while partlen1:
                        pre=pre.next
                        partlen1-=1
                else:
                    pre.next=head2
                    while partlen2:
                        pre=pre.next
                        partlen2-=1
                pre.next=head
            sonlen*=2
        return dummpy.next

