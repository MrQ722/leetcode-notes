# 用内置函数
# 执行用时：40ms，击败95.91%
# 内存消耗：14MB，击败55.70%
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:return 0
        nums.sort()
        n = nums[1]-nums[0]
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] > n:
                n = nums[i]-nums[i-1]
        return n


# 桶排序
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2: return 0
        
        max_ = max(nums)
        min_ = min(nums)
        max_gap = 0
        
        each_bucket_len = max(1,(max_-min_) // (len(nums)-1))
        buckets =[[] for _ in range((max_-min_) // each_bucket_len + 1)]
        
        for i in range(len(nums)):
            loc = (nums[i] - min_) // each_bucket_len
            buckets[loc].append(nums[i])
        
        prev_max = float('inf')
        for i in range(len(buckets)):
            if buckets[i] and prev_max != float('inf'):
                max_gap = max(max_gap, min(buckets[i])-prev_max)
            
            if buckets[i]:
                prev_max = max(buckets[i])
                
        return max_gap
