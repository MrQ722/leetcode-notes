# 字典
# 执行用时：56ms，击败86.97%
# 内存消耗：13.4MB，击败63.64%

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = 0
        for i in range(len(s)):
            if i == len(s)-1:
                n += dic[s[i]]
                break
            if dic[s[i]] < dic[s[i+1]]:
                n -= dic[s[i]]
            else:
                n += dic[s[i]]
        return n
        

# 简写

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))
