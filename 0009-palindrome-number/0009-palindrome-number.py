class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_original=x
        digits=[] # create digits from x
        # return False for negative numbers
        if x<0 :
            return False
        # return True for 0<=x<10: single digits
        elif x<10:
            return True
        # identify digits and reverse them
        else:
            print('x:',x)
            while x>0:
                digits.append(x%10)
                print('digits:',digits)
                x=x//10
                print('x:',x)
        answer=0
        digits=digits[::-1]
        for i in range(len(digits)):
            answer+= digits[i]* 10**i
            print('answer:',answer)
        print('x_original:',x_original)  
        return answer==x_original


        # return answer==x

