# 字典用于记录
# 重点在于如何判断元素相同,使用sorted
# 执行用时：48ms，击败96.90%
# 内存消耗：17.4MB，击败20.01%
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char = {}
        for x in strs:
            y = ''.join(sorted(x))
            if y in char:
                char[y].append(x)
            else:
                char[y] = [x]
        return [char[x] for x in char]

# 使用collections.defaultdict(list)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {collections.defaultdict(list)}

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())


# 字符计数
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)
        
        return list(mp.values())
