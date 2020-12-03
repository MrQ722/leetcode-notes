# 对小于n的数进行求余
# 超时
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:return 0
        x = 0
        for i in range(2,n):
            for j in range(2,i):
                if i%j == 0:
                    x-=1
                    break
            x+=1
        return x
# 添加记忆
# 超时
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:return 0
        x = 0
        tmp = []
        for i in range(2,n):
            if i in tmp:
                continue
            k = 2
            while k*i<n:
                tmp.append(k*i)
                k+=1
            x+=1
        return x
# 埃氏筛
# 执行用时：3020ms，击败8.91%
# 内存消耗：24.8MB，击败61.08%
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:return 0
        tmp = [1]*n
        x = 0
        for i in range(2,n):
            if tmp[i] == 1:
                x+=1
            k = i
            while k*i<n:
                tmp[k*i] = 0
                k+=1
        return x
