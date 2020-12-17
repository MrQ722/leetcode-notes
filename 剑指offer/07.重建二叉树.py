# 递归
# 执行用时：192ms，击败45.17%
# 内存消耗：86.9MB，击败5.07%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:return None
        tree = TreeNode(preorder[0])
        node = tree
        head = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:head+1],inorder[:head])
        node.right = self.buildTree(preorder[1+head:],inorder[1+head:])
        return tree
