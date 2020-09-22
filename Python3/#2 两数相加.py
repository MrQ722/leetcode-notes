# 链表问题
# 按位相加，考虑进位
# 考察链表从末尾插入的方法：新建指针probe
# 执行用时：68ms，击败91.02%
# 内存消耗：13.4MB，击败45.69%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        up = 0
        a = 0
        b = 0
        down = (l1.val+l2.val)%10 + up
        up = (l1.val+l2.val)//10
        old = ListNode(down)
        probe = old
        while True:
            l1 = l1.next
            l2 = l2.next
            if l1 == None:
                l1 = ListNode(0)
                a = 1
            if l2 == None:
                l2 = ListNode(0)
                b = 1
            if a == 1 and b == 1 and up == 0:
                break
            down = (l1.val+l2.val+up)%10
            up = (l1.val+l2.val+up)//10
            new = ListNode(down)
            probe.next = new
            probe = probe.next
        return old
