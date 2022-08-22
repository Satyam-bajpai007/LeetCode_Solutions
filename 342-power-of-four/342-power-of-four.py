class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        flag = False
        if n>0 and log(n,4).is_integer():
            flag = True
        return flag
            
        