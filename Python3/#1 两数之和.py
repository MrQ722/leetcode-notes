# 自己写的第一版答案，运行时间6336ms，消耗内存14.6MB。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = 0
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    a = 1
                    break
            if a == 1:
                break
        return [i,j]
