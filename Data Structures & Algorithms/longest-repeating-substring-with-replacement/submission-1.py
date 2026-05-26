class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashSet= dict()
        res=0
        l=0 
        for r in range (len(s)):
            hashSet[s[r]] = 1+ hashSet.get(s[r],0)

            while (r-l+1) - max(hashSet.values())>k:
                hashSet[s[l]] -=1
                l+=1
            
            res= max(res, r-l+1)
        return res
