# list排序，一次遍历
# 执行用时：52ms，击败75.16%
# 内存消耗：23.3MB，击败8.10%
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[0]
        for i in range(1,len(nums)):
            if x == nums[i]:
                return x
            else:
                x = nums[i]

# 哈希表
class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)
        return -1

# 原地交换
# Python 中，a,b=c,d 操作的原理是先暂存元组(c,d) ，然后 “按左右顺序” 赋值给 a 和 b 。
class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

