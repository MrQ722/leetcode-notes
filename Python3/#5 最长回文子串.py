# 没想到什么好方法，就直接遍历了，算是中心扩散法，比纯粹的暴力解法好一些，时间复杂度N2
# 执行用时： 1152ms，击败73.68%
# 内存消耗： 13.6MB，击败48.74%

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s :
            return s
        num = []
        for i in range(len(s)):
            if i+2 <len(s) and s[i] == s[i+2]:
                num.append(self.helper(i,i+2,s))
            if i+1 <len(s) and s[i] == s[i+1]:
                num.append(self.helper(i,i+1,s))
        if not num:
            return s[0]
        start = max(num)[1] 
        L = max(num)[0]   
        print(num)
        return   s[start:start+L]   
    def helper(self,i,j,s):
        a = i-1
        b = j+1
        while a >= 0 and b < len(s):
            if s[a] == s[b]:
                a -= 1
                b += 1
            else:
                break
        return (b-a-1,a+1)

# 还有动态规划、Manancher算法
