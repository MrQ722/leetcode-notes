# 位运算寻找可行区间
# 执行用时：1732ms，击败：10.72%
# 内存消耗：13.4MB，击败：26.50%
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:return 0
        i = 0
        n = x
        while True:
            if n == 1:
                i = i//2
                break
            else:
                n>>=1
                i+=1
        for j in range(2**i,2**(i+1)+1):
            if j**2 > x:
                return j-1
                
# 使用自然对数进行换底
# 注意：指数函数和对数函数的参数和返回值均为浮点数，因此运算过程会存在误差
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans

# 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


# 牛顿迭代
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        
        return int(x0)
