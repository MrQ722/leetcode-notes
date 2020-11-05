# 递归
# 执行用时：48ms，击败63.49%
# 内存消耗：13.6MB，击败8.59%
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        num = self.countAndSay(n-1)
        i = 0
        y = num[0]
        tmp = ''
        for x in num:
            if x == y:
                i+=1
            else:
                tmp = tmp + str(i) + y
                y = x
                i = 1
        tmp = tmp + str(i) + y
        return tmp


# 高赞
class Solution:
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1,n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1,len(prev_person)):
                if prev_person[j] == num:count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person
