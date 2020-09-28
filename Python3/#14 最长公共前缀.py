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

    
    
# zip(*iterables)
# 创建一个聚合了来自每个可迭代对象中的元素的迭代器。 返回一个元组的迭代器，其中的第 i 个元组包含来自每个参数序列或可迭代对象
# 的第 i 个元素。 当所输入可迭代对象中最短的一个被耗尽时，迭代器将停止迭代。 当只有一个可迭代对象参数时，它将返回一个单元组的
# 迭代器。 不带参数时，它将返回一个空迭代器。
# 执行用时：40ms，击败81.61%
# 内存消耗：13.3MB，击败78.27%

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:     
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break           
        return s 

    
# find()函数
# 取一个单词 s，和后面单词比较，看 s 与每个单词相同的最长前缀是多少！遍历所有单词。

class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res

    
# 按字典排序数组，比较第一个，和最后一个单词，有多少前缀相同。

class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        s.sort()
        n = len(s)
        a = s[0]
        b = s[n-1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res

