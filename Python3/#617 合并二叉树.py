# 简单的递归算法，但是感觉写的有点儿啰嗦
# 执行用时：104ms，击败80.10%
# 内存消耗：14.4MB，击败68.24%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            if t1:
                return t1
            else:
                return t2
        else:
            t1.val += t2.val
            self.helper(t1,t2)
            return t1
    def helper(self,node1,node2):
        if node1.left:
            if node2.left:
                node1.left.val += node2.left.val
                self.helper(node1.left, node2.left)
        else:
            if node2.left:
                node1.left = node2.left        
        if node1.right:
            if node2.right:
                node1.right.val += node2.right.val
                self.helper(node1.right, node2.right)
        else:
            if node2.right:
                node1.right = node2.right
        
# 精简代码
# 执行用时：100ms，击败91.61%
# 内存消耗：14.4MB，击败73.88%

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and t2:
            return t2               
        if t1 and t2:
            t1.val = t2.val+t1.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
        return t1
