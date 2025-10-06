class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n=len(nums)
        # base cases
        if n<=1:
            return nums[0]
        # empty list to store maximum sums    
        maximas=[0]*n
        maximas[0]= nums[0]
        maximas[1]=max(nums[0],nums[1]) # choose maximum if only 2 houses
        for i in range(2,n):
            maximas[i]= max( maximas[i-1], nums[i]+ maximas[i-2])
        return maximas[n-1]
        
            

            