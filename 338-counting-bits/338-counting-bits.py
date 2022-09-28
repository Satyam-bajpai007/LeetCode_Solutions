class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        s=0
        cnt=0
        for i in range(n+1):
            s=bin(i)[2::]
            lst.append(s.count("1"))
        return lst
            