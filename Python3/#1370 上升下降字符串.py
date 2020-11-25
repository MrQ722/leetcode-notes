# 用unicode索引字符
# 执行用时:220ms,击败5.06%
# 内存消耗：13.9MB，击败5.00%
class Solution:
    def sortString(self, s: str) -> str:
        tmp = ''
        s = list(s)
        s.sort()
        while s:
            for i in range(ord(s[0]),ord(s[-1])+1):
               if chr(i) in s:
                   tmp += chr(i)
                   s.remove(chr(i))
            if s:
                for i in range(ord(s[-1]),ord(s[0])-1,-1):
                    if chr(i) in s:
                        tmp += chr(i)
                        s.remove(chr(i))  
        return tmp


# 桶计数
class Solution:
    def sortString(self, s: str) -> str:
        num = [0] * 26
        for ch in s:
            num[ord(ch) - ord('a')] += 1
        
        ret = list()
        while len(ret) < len(s):
            for i in range(26):
                if num[i]:
                    ret.append(chr(i + ord('a')))
                    num[i] -= 1
            for i in range(25, -1, -1):
                if num[i]:
                    ret.append(chr(i + ord('a')))
                    num[i] -= 1

        return "".join(ret)
