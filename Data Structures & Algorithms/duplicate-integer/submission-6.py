class Solution:
    def hasDuplicate( self, nums ):
        done = list()
        for num in nums:
            if num in done:
                return True
            done.append(num)
        return False 
