# 从高到低考虑
# 先对peolpe排序，从后往前插入
# 执行用时：112ms，击败82.47%
# 内存消耗：13.9MB，击败40.35%
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        pointer = [0]
        people.sort()
        for i in range(len(people)):
            if people[pointer[-1]][0] != people[i][0]:
                pointer.append(i)
        pointer.append(len(people))
        tmp = []
        for i in range(-1,-len(pointer),-1):
            for j in range(pointer[i-1],pointer[i]):
                tmp.insert(people[j][1],people[j])
        return tmp
        
# 简化写法
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1])) # 注意lambda的使用方法
        n = len(people)
        ans = list()
        for person in people:
            ans[person[1]:person[1]] = [person]
        return ans


# 从低到高考虑
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans


            
