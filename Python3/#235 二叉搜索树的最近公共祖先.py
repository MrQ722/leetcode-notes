# 最早的思路是从根部开始寻找p和q，记录找到前的节点值保存在两个list中，然后寻找其中最靠近列表末端的相同参数
# 发现二叉树左边的小于根部，右边的大于根部，因此可以简便写一个递归就可以完成、
# 执行用时：108ms，击败32.19%
# 内存消耗：17.3MB，击败68.45%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if min(p.val,q.val) < root.val < max(p.val,q.val):
            return root
        if p.val == root.val:
            return p
        if q.val == root.val:
            return q
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
 

# 简化后
class Solution:    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p ,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p ,q)
        else:
            return root
