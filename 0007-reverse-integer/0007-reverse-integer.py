class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        original_x=x
        pos_x= abs(x) # positive version to get digits
        # reversed= original for single digits
        if -10<x<10:
            return x
        # get digits and reverse the number for non-single digits   
        digits=[]
        
        while pos_x > 0:
            digits.append(pos_x%10) # make the digits from original number
            pos_x=pos_x//10

        digits=digits[::-1] # reverse the digits
        answer=sum( digit*10**i for i, digit in enumerate(digits))
        # beyond the domain
        if answer < (-2)**31 or answer > 2**31-1:
            return 0
        
        if original_x >0:
            return answer
        else: return -1*answer

        