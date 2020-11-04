# 单指针遍历
# 执行用时：36ms，击败86.73%
# 内存消耗：13.5MB，击败10.12%
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i<len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
        
# 双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b
