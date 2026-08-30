class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>0:
            x=str(x)
            y="".join(reversed(x))
            if(x==y):
                return True
            else:
                return False   
        else:
            return False