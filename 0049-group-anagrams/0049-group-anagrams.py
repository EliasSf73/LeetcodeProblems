class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps=dict()
        
        for word in strs:
            kee=''.join(sorted(list(word)))
            if kee in maps:
                maps[kee].append(word)
            else:
                maps[kee]=[word]
        return [x for x in maps.values()]
