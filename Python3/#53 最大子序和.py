# 暴力解法
# 超出时间限制
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = nums[0]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if sum(nums[i:j])>sub:
                    sub = sum(nums[i:j])
        return sub
        
# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])
        return max(nums)

        
