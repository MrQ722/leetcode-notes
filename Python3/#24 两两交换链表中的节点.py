# 递归，注意链表循环
# 执行用时：28ms，击败99.42%
# 内存消耗：13.5MB，击败15.11%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = head.next
        new_node = self.swapPairs(head.next.next)
        head.next = ListNode()
        node.next = head
        node.next.next = new_node
        return node
# 化简        
class Solution(object):
	def swapPairs(self, head):
		if not (head and head.next):
			return head
		tmp = head.next
		head.next = self.swapPairs(tmp.next)
		tmp.next = head
		return tmp

# 另一种交换思路，迭代实现
# 执行用时：36ms，击败89.45%
# 内存消耗：13.5MB，击败24.35%
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a, b=c.next, c.next.next
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next
        return thead.next
        
# 栈
class Solution(object):
	def swapPairs(self, head):
		if not (head and head.next):
			return head
		p = ListNode(-1)
		# 用stack保存每次迭代的两个节点
		# head指向新的p节点，函数结束时返回head.next即可
		cur,head,stack = head,p,[]
		while cur and cur.next:
			# 将两个节点放入stack中
			_,_ = stack.append(cur),stack.append(cur.next)
			# 当前节点往前走两步
			cur = cur.next.next
			# 从stack中弹出两个节点，然后用p节点指向新弹出的两个节点
			p.next = stack.pop()
			p.next.next = stack.pop()
			p = p.next.next
		# 注意边界条件，当链表长度是奇数时，cur就不为空	
		if cur:
			p.next = cur
		else:
			p.next = None
		return head.next
