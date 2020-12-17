# 直接用python内置函数，join+split
# 执行用时：40ms，击败56.33%
# 内存消耗：14.8MB，击败5.46%             
class Solution:
    def replaceSpace(self, s: str) -> str:
        return '%20'.join(s.split(' '))
 
# 一次遍历迭代
# 执行用时：36ms，击败79.85%
# 内存消耗：14.8MB，击败5.46%        
class Solution:
    def replaceSpace(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i] == ' ':
                s = s[:i]+'%20'+s[i+1:]
                i+=3
            else:
                i+=1
        return s

                
