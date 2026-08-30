class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix =""
        current=""
        dummy=0
        for i in range(0,len(strs)):
            current=strs[0][i]
            for j in range(0,len(strs)):
                if current!=strs[j][i]:
                    current=""
                    break
                
            prefix = prefix+current 
        return(prefix)




        