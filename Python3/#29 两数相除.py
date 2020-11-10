# 转换成字符串，按笔算方法进行迭代
# 执行用时：32ms，击败：98.50%
# 内存消耗：13.5MB，击败14.49%
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend = str(dividend)
        divisor = str(divisor)
        key = ''
        if dividend[0] == '-':
            dividend = dividend.strip('-')
            key = '-'
        if divisor[0] == '-':
            if key == '-':
                key = ''
                divisor = divisor.strip('-')
            else:
                key = '-'
                divisor = divisor.strip('-')
        divisor = int(divisor)
        tmp = []
        up = 0
        for i in range(len(dividend)):
            num = int(dividend[i]) + 10*up
            n = 0
            while num>=divisor:
                num -= divisor
                n += 1
            up = num
            if not tmp and n==0:
                continue
            else:
                tmp.append(str(n))
        tmp =  int(key + ''.join(tmp)) if tmp else 0
        if tmp<-2**31 or tmp>2**31-1:
            return 2**31-1
        else:
            return tmp
                        

# 位运算
def divide(self, dividend: int, divisor: int) -> int:
    sign = (dividend > 0) ^ (divisor > 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    #把除数不断左移，直到它大于被除数
    while dividend >= divisor:
        count += 1
        divisor <<= 1
    result = 0
    while count > 0:
        count -= 1
        divisor >>= 1
        if divisor <= dividend:
            result += 1 << count #这里的移位运算是把二进制（第count+1位上的1）转换为十进制
            dividend -= divisor
    if sign: result = -result
    return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1 
