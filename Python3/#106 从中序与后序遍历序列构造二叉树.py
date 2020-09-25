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
        
# 简化后
# 执行用时：208ms，击败33.60%
# 内存消耗：85.5MB，击败47.39%

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder :
            return None
        tree = TreeNode(postorder[-1])
        index = inorder.index(tree.val)
        tree.left = self.buildTree(inorder[:index],postorder[:index])
        tree.right = self.buildTree(inorder[index+1:],postorder[index:-1])
        return tree

# 简单起见，递归的时候每次我都开辟了新的数组，这个其实是没有必要的
# 我们可以通过四个变量来记录inorder和postorder的起始位置即可
# 执行用时：100ms，击败76.24%
# 内存消耗：17.4MB，击败93.68%

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def dfs(inorder, in_start, in_end, postorder, post_start, post_end):
            if in_start > in_end: return None
            if in_start == in_end: return TreeNode(inorder[in_start])
            if post_start == post_end: return TreeNode(inorder[in_start])
            root = TreeNode(postorder[post_end])
            i = inorder.index(root.val)
            root.left = dfs(inorder, in_start, i - 1, postorder, post_start, post_start + i - 1 - in_start)
            root.right = dfs(inorder, i + 1, in_end, postorder, post_start + i - 1 - in_start + 1, post_end - 1)
            return root
        n = len(inorder)
        return dfs(inorder, 0, n - 1, postorder, 0, n - 1)
