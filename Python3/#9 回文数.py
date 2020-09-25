# 简单
# 执行用时：88ms，击败59.84%
# 内存消耗：13.2MB，击败88.27%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)//2):
            if x[i] != x[-1-i]:
                return False
        return True
