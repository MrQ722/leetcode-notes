# 递归
# 执行用时：56ms，击败9.12%
# 内存消耗：13.3MB，击败65.62%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    

# 迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        sub = []
        while stack or root:
            while root:               
                stack.append(root)
                if root.left:          
                    root = root.left 
                else:
                    root = root.right     
            s = stack.pop()
            sub.append(s.val)
            if stack and s == stack[-1].left: 
                root = stack[-1].right
        return sub
