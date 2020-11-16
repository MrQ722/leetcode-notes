# 遍历2可能取的个数，组合数计算
# 执行用时：36ms，击败83.48%
# 内存消耗：13.6MB，击败5.06%
from functools import reduce
class Solution:
    def climbStairs(self, n: int) -> int:
        n2 = n // 2
        tmp = 1
        for i in range(1,n2+1):
            a = n - i
            tmp += reduce(lambda x,y:x*y, range(1,a+1))/reduce(lambda x,y:x*y, range(1,i+1))/(reduce(lambda x,y:x*y, range(1,a-i+1)) if a-i > 0 else 1)
        return int(tmp) 

# 动态规划(斐波那契数列)
# f(x) = f(x-1) + f(x-2)
# 执行用时：36ms，击败83.48%
# 内存消耗：13.5MB，击败21.84%
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:return 1
        tmp1 ,tmp2 = 1,1
        for i in range(n-1):
            n = tmp2
            tmp2 = tmp1+tmp2
            tmp1 = n
        return tmp2 

# 矩阵快速幂
# 如果一个问题可与转化为求解一个矩阵的 n 次方的形式，那么可以用快速幂来加速计算

