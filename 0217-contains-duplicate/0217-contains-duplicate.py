
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked=set()
        for a in nums:
            if a in checked:
                return True
            checked.add(a)
        return False
      
        