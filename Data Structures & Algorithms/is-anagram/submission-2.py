class Solution:
    def isAnagram(self,s,t):
        if len(s) != len(t):
            return False
        counts=dict()
        countt=dict()
        for i in s:
            counts[i]= 1+counts.get(i,0)
        for j in t:
            countt[j] = 1+ countt.get(j,0)
        return counts==countt
          
        