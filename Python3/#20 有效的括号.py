# 栈和字典的应用
# 执行用时：44ms，击败56.35%
# 内存消耗：13.2MB，击败89.63%

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        data = {'(':')','[':']','{':'}'}
        for i in range(len(s)):
            if s[i] in ['(','[','{']:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if data[stack.pop()] != s[i]:
                    return False
        if stack:
            return False
        else:
            return True
