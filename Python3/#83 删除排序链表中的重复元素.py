# 执行用时：52ms，击败54.04%
# 内存消耗：13.5MB，击败24.34%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:return head
        node = head
        while node.next:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
