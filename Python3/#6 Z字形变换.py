# 感觉不难，一次遍历就行
# 执行用时：84ms，击败32.06%
# 内存消耗：13.4MB，击败46.36%

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1:
            return s
        n = 2*numRows-2
        new = ''
        for i in range(numRows):
            for j in range(i,len(s),n):
                new +=s[j]
                if i != 0 and i != numRows-1 and (j+n-2*i)<len(s):
                    new += s[j+n-2*i]
        return new


# 高赞答案：模仿了Z字排列

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

