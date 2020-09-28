# 选取最短的字符串，由长到短去匹配
# 执行用时：48ms，击败37.27%
# 内存消耗：13.3MB，击败83.01%

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        short = strs[0]
        for i in strs:
            if len(i) < len(short):
                short = i
        for i in range(len(short),0,-1):
            a = 0
            for k in strs:
                if short[0:i] not in k[0:i]:
                    a = 1
                    break
            if a == 0:
                return short[0:i]
        return ''
