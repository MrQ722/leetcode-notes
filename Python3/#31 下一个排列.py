# 两遍扫描
# 从后向前遍历，寻找变小的第一个点，与该点后比这个点大的最小的点交换，交换后对改点后排列反向
# 执行用时：32ms，击败：96.93%
# 内存消耗：13.4MB，击败：25.06%
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 1
        for i in range(-1,-len(nums),-1):
            if nums[i-1] >= nums[i]:
                n += 1
            else:
                break
        if n == len(nums):
            nums.sort()
        else:
            for i in range(-1,-n-1,-1):
                if nums[i] > nums[-n-1]:
                    nums[i],nums[-n-1] = nums[-n-1],nums[i]
                    break
            nums[-n:] = nums[-n:][::-1]

