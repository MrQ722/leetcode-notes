# 递归
# 考虑深层复制问题，copy.deepcopy()
# 执行用时：44ms，击败：44.25%
# 内存消耗：13.6MB，击败11.14%
import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:return [[]]
        last = self.subsets(nums[:-1])
        tmp = copy.deepcopy(last)
        for x in last:
            x.append(nums[-1])
        tmp.extend(last)
        return tmp  
        
# 另一种递归
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res  



# 迭代
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
