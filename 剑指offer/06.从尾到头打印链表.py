# 遍历链表，list反向
# 执行用时：48ms，击败65.22%
# 内存消耗：16.2MB，击败25.06%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        return tmp[::-1]

# 栈
# 执行用时：44ms，击败81.67%
# 内存消耗：16.3MB，击败25.04%
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        return [tmp.pop() for i in range(len((tmp)))]
