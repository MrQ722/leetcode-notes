# 暴力解法，超出时间限制
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        x = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                n = sum(nums[i:j])
                if n >= lower and n <= upper:
                    x+=1
        return x

# 前缀+二分查找
import bisect # 二分查找
from itertools import accumulate # 返回加和后的可迭代对象


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sorted_sums = [0] # 是否可以等于lower、upper

        ans = 0
        for sums in accumulate(nums):
            left = bisect.bisect_left(prefix_sorted_sums, sums - upper)
            right = bisect.bisect_right(prefix_sorted_sums, sums - lower)
            ans += right - left
            bisect.insort(prefix_sorted_sums, sums)
        return ans

