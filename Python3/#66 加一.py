# 计算进位
# 执行用时：32ms，击败：95.88%
# 内存消耗：13.4MB，击败：22.52%
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 1
        for i in range(len(digits)-1,-1,-1):
            x = (digits[i]+n)//10
            digits[i] = (digits[i]+n)%10
            n = x
            if n == 0: 
                break
            if n == 1 and i == 0:
                digits.insert(0,1)
        return digits
