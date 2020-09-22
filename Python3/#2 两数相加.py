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
    
   # 简化后代码
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        dummy = p = ListNode(None)          
        s = 0               # 初始化进位 s 为 0
        while l1 or l2 or s:
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)  
            p.next = ListNode(s % 10)       # p.next 指向新链表, 用来创建一个新的链表
            p = p.next                      # p 向后遍历
            s //= 10                        # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
            l1 = l1.next if l1 else None    # 如果l1存在, 则向后遍历, 否则为 None
            l2 = l2.next if l2 else None    # 如果l2存在, 则向后遍历, 否则为 None
        return dummy.next   # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点

