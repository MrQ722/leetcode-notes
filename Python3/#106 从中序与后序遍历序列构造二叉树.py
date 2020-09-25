# 结论：前序/后序+中序序列可以唯一确定一棵二叉树
# 看完结论后，自己写的递归
# 执行用时：480ms，击败5.22%
# 内存消耗：86.9MB，击败5.01%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder :
            return inorder
        tree = TreeNode(postorder[-1])
        index = [i for i in range(len(inorder)) if inorder[i] == tree.val]
        newin = inorder[:index[0]]
        newpost = postorder[:len(newin)]
        if len(newin) == 1:
            tree.left = TreeNode(newin[0])
        elif len(newin) > 1:
            tree.left = self.buildTree(newin,newpost)
        newin = inorder[index[0]+1:]
        newpost = postorder[-len(newin)-1:-1]
        if len(newin) == 1:
            tree.right = TreeNode(newin[0])
        elif len(newin) > 1:
            tree.right = self.buildTree(newin,newpost)
        return tree
        
#
