# 将int变成str，翻转后再变成int
# 执行用时：48ms，击败45.56%
# 内存消耗：13.4MB，击败25.57%

class Solution:
    def reverse(self, x: int) -> int: 
        old = str(x)      
        if x < 0:
            new = old[0] + old[:0:-1]
        else:
            new = old[::-1]
        if int(new) < -2**31 or int(new) > 2**31 -1:
            return 0
        return int(new)
        
# 优化方案：二进制按位运算
# # 执行用时：44ms，击败69.61%
# 内存消耗：13.4MB，击败47.37%

class Solution:
    def reverse(self, x: int) -> int: 
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if x>0 else 1<<31 # 按位移动，能快一些？
        while y != 0:
            res = res*10 +y%10
            if res > boundry :
                return 0
            y //=10
        return res if x >0 else -res
