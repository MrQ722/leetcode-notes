# 自己的想法是从二叉树的根部开始嵌套，但是camera的安装位置的可能性很多，从根部无法保证最小化
# 本答案来自leetcode的思路
# 想知道在哪里放camera，需要来按照某种顺序来遍历图，遍历的同时在每一个位置时，以某种规则来决定是否放置。
# 所以想到用dfs遍历，用greedy来决定。开始遍历后，首先会一条路走到leaf。
# 将这个leaf标记val为1，并把这个val返回，告诉上一层也就是这个leaf的parent：有一个child是leaf。所以，此parent必须放一个camera。下一步是为这个parent的val标记为2，用2代表放置camera，并将这个2返回给这个parent的parent，称他为parent_g。所以parent_g通过其得到的返回值，知道他的孩子parent是有camera，自己可以被cover，所以将自己的val赋值0，代表自己一种‘属性’，被自己的child节点放置的camera cover到了的属性。
# 在此过程中，greedy体现在我们在parent放置camera来cover其leaf，而没有在leaf上直接放置camera。
# 执行用时：56ms，击败82.08%
# 内存消耗13.6MB，击败62.81%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cameras = 0
        self.dfs_greedy(root)
        return self.cameras + int(root.val == 1)
    def dfs_greedy(self, root):
        if not root:
            return 0
        left = self.dfs_greedy(root.left)
        right = self.dfs_greedy(root.right)
        if left == 0 and right == 0:
            root.val = 1
        elif left == 1 or right == 1:
            root.val = 2
            self.cameras = self.cameras + 1
        else: #left == 2 or right == 2:
            root.val = 0
        return root.val

