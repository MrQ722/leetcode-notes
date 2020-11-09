# 加和后进位
# 执行用时：48ms，击败：44.67%
# 内存消耗：13.5MB，击败：23.22%
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num = str(int(a)+int(b))
        n = 0
        tmp = []
        for i in range(-1,-len(num)-1,-1):
            x = (int(num[i]) + n)//2
            tmp.insert(0,str((int(num[i]) + n)%2))
            n = x
        if n == 1:
            tmp.insert(0,'1')
        return ''.join(tmp)


# 强制转换成十进制
# 执行用时：44ms，击败：66.23%
# 内存消耗：13.5MB，击败：16.04%
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        return bin(a+b)[2:]
# 简化
class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2)) # 转化成十进制
        
# 位运算
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


