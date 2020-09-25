# 跟第7题想法类似
class Solution:
    def myAtoi(self, str: str) -> int:
        num = ['0','1','2','3','4','5','6','7','8','9']
        flag = 0
        sub = 0
        pn = 0
        bond = (1<<31)-1
        for i in range(len(str)):
            if str[i] == ' ' and flag == 0:
                continue
            if str[i] == '+' and flag == 0:
                flag = 1
                continue
            if str[i] == '-' and flag == 0:
                pn = 1
                bond = bond+1
                flag = 1
                continue
            if str[i] not in num:
                break
            flag = 1
            sub = sub*10 + int(str[i])
            if sub > bond:
                sub = bond
                break
        return sub if pn == 0 else -sub

# 正则化表达式：
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647    
        INT_MIN = -2147483648
        str = str.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(str)   #查找匹配的内容
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)    #返回值
        
# 简化后
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
