class Solution(object):
     # cache to store results
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo_cache=dict()
        # if result already in cache, return it
        if n in memo_cache:
            return memo_cache[n]
        # else, typically recursion
        if n<=1:
            return n
        else:
            result= self.fib(n-1) + self.fib(n-2)
        # save result to memom_cache
        memo_cache[n]= result

        return result

    