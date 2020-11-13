# 分奇偶进行迭代
# 执行用时：52ms，击败：82.75%
# 内存消耗：15.4MB，击败：36.27%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head
        nextList = head.next
        nextNode1 = head
        nextNode2 = head.next
        while nextNode1.next and nextNode2.next:
            if nextNode2.next:
                nextNode1.next = nextNode2.next
                nextNode1 = nextNode1.next
            if nextNode1.next:
                nextNode2.next = nextNode1.next
                nextNode2 = nextNode2.next
        if nextNode1.next:nextNode1.next=None
        if nextNode2.next:nextNode2.next=None
        nextNode1.next = nextList
        return head



