# 从后向前遍历
# 执行用时：36ms，击败84，21%
# 内存消耗：13.5MB，击败10.89%
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                for j in range(i,-1,-1):
                    n += 1 
                    if s[j-1] == ' ' :
                        return n
                    if j == 0:
                        return n                    
        return n
