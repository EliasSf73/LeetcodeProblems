class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=set()
        idx=[]
        for i in range(len(nums)):
            if target-nums[i] in seen:
                idx.append(i)
                idx.append(nums.index(target-nums[i]))
            else:
                seen.add(nums[i])
        return idx
        

