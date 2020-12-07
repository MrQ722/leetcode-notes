# 
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)
        
        return not any(queue and queue[0] < 3 for queue in mp.values())

# 
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        countMap = collections.Counter(nums)
        endMap = collections.Counter()

        for x in nums:
            if (count := countMap[x]) > 0:
                if (prevEndCount := endMap.get(x - 1, 0)) > 0:
                    countMap[x] -= 1
                    endMap[x - 1] = prevEndCount - 1
                    endMap[x] += 1
                else:
                    if (count1 := countMap.get(x + 1, 0)) > 0 and (count2 := countMap.get(x + 2, 0)) > 0:
                        countMap[x] -= 1
                        countMap[x + 1] -= 1
                        countMap[x + 2] -= 1
                        endMap[x + 2] += 1
                    else:
                        return False
        
        return True

