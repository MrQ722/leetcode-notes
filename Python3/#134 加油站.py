# 双指针
# 执行用时：40ms，击败86.47%
# 内存消耗：14MB，击败73.12%
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 环的长度
        mod = len(gas)

        # 起始点假设为 0，当前在 0 节点。
        start, cur = 0, 0

        # 把 0 节点的油都灌进去。
        oil = gas[0]

        # 当 cur + 1 == start 时说明到了终点，所以没有考虑终点到起点（两者相邻）所用的油。
        while (cur + 1) % mod != start:

            # 如果油不够开往下一节点。
            if oil < cost[cur]:
                # 说明以 start 为起始节点不行，将 start 前一位假设为起始节点。
                start = (start - 1) % mod
                # 新的起始点里面的油全都抱走，同时要计算从新的起始点
                # 到旧的的起始点（它的下一节点）所消耗的油。
                oil += gas[start] - cost[start]

            # 如果够。
            else:
                # 把消耗的油减掉。
                oil -= cost[cur]
                # 去下一个节点。
                cur = (cur + 1) % mod
                # 把新节点的油抱走。
                oil += gas[cur]
        
        # 返回时记得判断一下在终点时的油能否开到起点。
        return start if oil - cost[cur] >= 0 else -1


# 穷举法
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        L = len(gas)
        for i in range(L):
            ret = 0
            for j in range(i, L+i):
                if j >= L:
                    j -= L
                ret += gas[j]-cost[j]
                if ret < 0:
                    break
            else:
                return i
        return -1
