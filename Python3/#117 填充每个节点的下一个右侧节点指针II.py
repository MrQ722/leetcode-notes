# 尝试了用迭代来写
# 执行用时：56ms，击败92.97%
# 内存消耗：14.5MB，击败58.67%

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        L = [root]
        while L:
            n = len(L)
            for i in range(n):
                a = L.pop(0)
                if i == n-1:
                    a.next = None
                else:
                    a.next = L[0]
                if a.left: L.append(a.left)
                if a.right: L.append(a.right)
        return root
        
        
# 应用常数空间
# 执行用时：56ms，击败92.97%
# 内存消耗：14.5MB，击败58.67%

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        head = None
        tail = None
        while cur:
            while cur:
                if cur.left:
                    if not head:
                        head = cur.left
                        tail = cur.left
                    else:
                        tail.next = cur.left
                        tail = tail.next
                if cur.right:
                    if not head:
                        head = cur.right
                        tail = cur.right
                    else:
                        tail.next = cur.right
                        tail = tail.next
                cur = cur.next
            cur = head
            head = None
            tail = None
        return root

