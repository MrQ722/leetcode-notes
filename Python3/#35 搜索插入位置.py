# 执行用时：44ms，击败48.02%
# 内存消耗：14MB，击败42.81%
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] < target and nums[i+1] > target:
                return i+1
 
 
# 二分查找
# 执行用时：40ms，击败72.81%
# 内存消耗：14.1MB，击败27.53%
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if nums[size - 1] < target:
            return size
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
