# 迭代
# 执行用时：48ms，击败72.86%
# 内存消耗：13.4MB，击败58.41%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 :return l2
        if not l2 :return l1
        if l1.val > l2.val:
            if l2.next:
                new = l2 
                key = l2
                l2 = l2.next
            else:
                l2.next = l1
                new = l2
                return new
        else: 
            if l1.next:
                new = l1 
                key = l1
                l1 = l1.next
            else:
                l1.next = l2
                new = l1
                return new
        while True:
            if l1.val > l2.val:
                if l2.next:
                    key.next = l2
                    key = l2
                    l2 = l2.next
                else:
                    l2.next = l1
                    key.next = l2
                    break
            else:
                if l1.next:
                    key.next = l1
                    key = l1
                    l1 = l1.next
                else:
                    l1.next = l2
                    key.next = l1  
                    break               
        return new

# 优化后代码
class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next



# 递归
# 执行用时：52ms，击败48.91%
# 内存消耗：13.3MB，击败80.74%
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


