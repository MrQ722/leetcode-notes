# 遍历数组，将奇数偶数分别记录，然后重组
# 执行用时：380ms，击败：5.22%
# 内存消耗：16MB，击败：5.35%
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd,even = [],[]
        for x in A:
            if x % 2 == 1:
                odd.append(x)
            else:
                even.append(x)
        tmp = []
        for i in range(len(odd)):
            tmp.append(even[i])
            tmp.append(odd[i])
        return tmp

# 稍微修改一下
# 执行用时：308ms，击败：15.06%
# 内存消耗：16MB，击败：7.89%
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        tmp = [None]*len(A)
        i,j = 0,1
        for x in A:
            if x % 2 == 1:
                tmp[j] = x
                j+=2
            else:
                tmp[i] = x
                i+=2
        return tmp

# 高赞
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x:x%2)
        ans=[0]*len(A)
        ans[::2],ans[1::2]=A[:int(len(A)/2)],A[int(len(A)/2):]
        return ans
