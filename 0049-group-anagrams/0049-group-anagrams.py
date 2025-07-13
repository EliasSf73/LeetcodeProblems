class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps=dict()
        for a in strs:
            kee= ''.join(sorted(list(a)))
            if kee in maps:
                maps[kee].append(a)
            else:
                maps[kee]=[a]
        return [k for k in maps.values()]

       


