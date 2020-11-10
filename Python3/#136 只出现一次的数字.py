# 位运算基础
# 任何数和0异或运算仍然是原来的数
# 任何数和其自身做异或运算结果是0、
# 异或运算满足交换律和结合率
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
