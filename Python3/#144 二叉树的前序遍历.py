# 递归
# 执行用时：56ms，击败8.19%
# 内存消耗13.5MB，击败5.69%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root):
            if not root:return
            sub.append(root.val)
            preorder(root.left)
            preorder(root.right)
        sub = []
        preorder(root)
        return sub
        
# 迭代
# 执行用时：56ms，击败8.19%
# 内存消耗13.5MB，击败5.69%
