class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx=[]
        observed=set()
        for i in range(len(nums)):
            if target-nums[i] in observed:
                idx.append(i)
                idx.append(nums.index(target-nums[i]))
            else:
                observed.add(nums[i])
        return idx

        