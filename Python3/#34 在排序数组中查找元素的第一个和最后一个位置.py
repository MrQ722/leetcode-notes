# 双指针
# 执行用时：44ms，击败50.53%
# 内存消耗：14.2MB，击败73.99%
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:return [-1,-1]
        i,j = 0,len(nums)-1
        while True:
            if nums[i] != target:
                i+=1
            if nums[j] != target:
                j-=1
            if i>j:
                return [-1,-1]
            if nums[i] == target and nums[j] == target:
                return [i,j]

# 二分查找
class Solution(object):
    def searchRange(self,nums, target):
        def left_func(nums,target):
            n = len(nums)-1
            left = 0
            right = n
            while(left<right):
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid-1
                if nums[mid] == target:
                    right = mid
                if nums[mid] < target:
                    left = mid+1
            return left
        a =  left_func(nums,target)
        b = left_func(nums,target+1)
        if  a == len(nums) or nums[a] != target:
            return [-1,-1]
        else:
            return [a,b-1]
