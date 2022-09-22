class Solution:
    def grayCode(self, n: int) -> List[int]:
        lst=[]
        for i in range(1<<n):
            val = (i ^ (i>>1))
            # val = bin(val)[2::]
            # val = val.zfill(n)
            lst.append(val)
        return lst