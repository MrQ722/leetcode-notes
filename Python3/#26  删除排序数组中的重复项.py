# 添加一个指针，遍历列表，remove重复元素
# 执行用时：768ms，击败8.77%
# 内存消耗：14.6MB，击败8.11%
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return len(nums)
        key = nums[0]
        for i in nums[1:]:
            if i == key:
                nums.remove(i)
            else:
                key = i
        return len(nums)
 
# 用pop反向遍历
# 执行用时：60ms，击败35.35%
# 内存消耗：14.6MB，击败10.18%
 def removeDuplicates(nums):
    for num_index in range(len(nums)-1, 0, -1):
        if nums[num_index] == nums[num_index-1]:
            nums.pop(num_index)
    return len(nums)


 
