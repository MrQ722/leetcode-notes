# 穷举所有情况
# 执行用时：60ms，击败71.78%
# 内存消耗：13.6MB，击败5.15%
class Solution:
    def intToRoman(self, num: int) -> str:
        s = str()
        a = num // 1000
        for i in range(a):
            s+='M'
        num = num - a*1000
        a = num // 100
        print(num,a)
        if a < 5:
            if a == 4:
                s+='CD'
            else:
                for i in range(a):
                    s+='C'
        elif a == 5:
            s+='D'
        else:
            if a == 9:
                s+='CM'
            else:
                s+='D'
                for i in range(a-5):
                    s+='C'
        num = num - a*100
        a = num // 10
        if a < 5:
            if a == 4:
                s+='XL'
            else:
                for i in range(a):
                    s+='X'
        elif a == 5:
            s+='L'
        else:
            if a == 9:
                s+='XC'
            else:
                s+='L'
                for i in range(a-5):
                    s+='X'
        a = num - a*10
        if a < 5:
            if a == 4:
                s+='IV'
            else:
                for i in range(a):
                    s+='I'
        elif a == 5:
            s+='V'
        else:
            if a == 9:
                s+='IX'
            else:
                s+='V'
                for i in range(a-5):
                    s+='I'
        return s
# 简单写法（暴力匹配）
class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"] # 1000，2000，3000
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # 100~900
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # 10~90
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # 1~9
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]

作者：z1m
链接：https://leetcode-cn.com/problems/integer-to-roman/solution/tan-xin-ha-xi-biao-tu-jie-by-ml-zimingmeng/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 贪心哈希表
class Solution:
    def intToRoman(self, num: int) -> str:
        # 使用哈希表，按照从大到小顺序排列
        hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key  # 比如输入4000，count 为 4
                res += hashmap[key] * count 
                num %= key
        return res
