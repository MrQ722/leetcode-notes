# 问题挺简单，就是简单的回溯问题，但是其中有些测试样例比较恶心，多测试了好几次
# 执行用时：40ms，击败73.48%
# 内存消耗: 13.3MB, 击败61.52%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
           return root
        newRoot = TreeNode()
        def invert(new,old):
            new.val = old.val
            if old.left != None:
                new.right = TreeNode()
                invert(new.right,old.left) 
            if old.right != None:
                new.left = TreeNode()
                invert(new.left,old.right)
        invert(newRoot,root)
        return newRoot

# 看到一个更简洁的递归，不需要再函数内部再构造函数
# 注意37行，必须在一行写，保证交换同时进行，佩服
# 执行用时：40ms，击败73.48%
# 内存消耗: 13.4MB, 击败21.97%

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
