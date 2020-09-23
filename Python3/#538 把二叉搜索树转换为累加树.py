# 递归
# 自己想了一种递归方法，但是有一种情况无法满足，看答案了
# 处理特殊情况，根节点为空，直接返回；
# 定义变量 total，存储节点值的累加值；
# 反向中序遍历二叉搜索树：
# 递归右子树，将节点值累加到 total；
# 然后处理当前节点，先将值累加到 total，然后将 total 作为新值赋给当前节点值；
# 最后递归左子树，同样将值累加到 total，然后更新值。
# 执行用时：72ms，击败95.66%
# 内存消耗：15.5 MB，击败42.17%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.total = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            if root.right:
                dfs(root.right)
            self.total += root.val
            root.val = self.total
            if root.left:
                dfs(root.left)
        dfs(root)
        return root



