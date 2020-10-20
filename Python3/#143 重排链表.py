# 遍历所有链表节点，再重新赋值，有点儿笨
# 执行用时：104ms，击败89.55%
# 内存消耗：22.7MB，击败25.05%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head:
            node = head
            val = []
            while node.next:
                node = node.next
                val.append(node.val)
            node = head.next
            for i in range(len(val)):
                if i%2 == 0:
                    node.val = val[-i//2-1]
                else:
                    node.val = val[i//2]
                node = node.next


# 可以考虑用栈
# 把节点压入栈中, 再弹出来

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head: return None
        p = head
        stack = []
        # 把所有节点压入栈中
        while p:
            stack.append(p)
            p = p.next
        # 长度
        n = len(stack)
        # 找到中点前一个位置 
        count = (n - 1) // 2
        p = head
        while count:
            # 弹出栈顶
            tmp = stack.pop()
            # 与链头拼接
            tmp.next = p.next
            p.next  = tmp
            # 移动一个位置
            p = tmp.next
            count -= 1
        stack.pop().next = None


