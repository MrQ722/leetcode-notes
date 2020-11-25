# 回溯
# 执行用时：44ms，击败60.56%
# 内存消耗：13.5MB，击败53.68%
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        tmp = []
        if len(nums) == 1:return [nums]
        for i in range(len(nums)):
            for x in self.permute(nums[:i]+nums[i+1:]):
                tmp.append([nums[i]]+x)
        return tmp


# 回溯
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res
