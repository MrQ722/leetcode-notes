# 字典+列表
# 执行用时：36ms，击败79.88%
# 内存消耗：14.9MB，击败5.37%
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):return False
        tmp, value = {}, []
        for i in range(len(pattern)):
            if pattern[i] in tmp:
                if tmp[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in value:
                    return False
                tmp[pattern[i]] = s[i] 
                value.append(s[i])
        return True
