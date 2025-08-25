class Solution:

    def frequencyCounter(self,s:str)->int:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        max_v=max(d.values())
        min_v=min(d.values())
        
        difference=max_v-min_v
        
        if (difference > 0):
            return difference
            
        return 0

    def beautySum(self, s: str) -> int:
        n=len(s)
        total_frequencies=0
        for i in  range(n):
            for j in range(i+1,n+1):
                substring=s[i:j]
                total_frequencies+=self.frequencyCounter(substring)

        return total_frequencies
            
