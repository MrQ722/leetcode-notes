# 自己写的第一版答案，运行时间76ms，消耗内存14MB
# 思路很简单，将字符串变成列表从头进行索引，统计出所有连续无重复字符串的长度，选取其中最大值输出
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        l = []; num = []
        if len(s) < 2:
            num.append(len(s))
        else:
            l.append(s[0])
            for i in range(1,len(s)):
                if s[i] in l:
                    num.append(len(l))
                    a = l.index(s[i])
                    del l[:a+1]
                    l.append(s[i])
                else:
                    l.append(s[i])
            num.append(len(l))
        return max(num)

    # 考虑尽量在遍历一次的情况下尽量少建立list，并且尽量少索引
    # 运行时间92ms，消耗内存13.8MB
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        num = 0
        i, j = 0, 0
        while j < len(s) :
            if s[j] in s[i:j]:
                if j-i > num:
                    num = j-i
                i = i + s[i:j].index(s[j]) + 1
                j += 1
            else:
                j += 1
        if j-i > num:
            num = j-i
        return num
    
# 考虑不使用list，直接在字符串上操作
# 运行时间72ms，消耗内存13.5MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = 0
        i, j = 0, 0
        while j < len(s) :
            if s[j] in s[i:j]:
                if j-i > num:
                    num = j-i
                i = i + s[i:j].index(s[j]) + 1
                j += 1
            else:
                j += 1
        if j-i > num:
            num = j-i
        return num
