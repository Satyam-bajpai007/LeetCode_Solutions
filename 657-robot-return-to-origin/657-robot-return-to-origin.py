class Solution:
    def judgeCircle(self, moves: str) -> bool:
        lst=[]
        lst[:0]=moves
        print(lst)
        if lst.count('R')==lst.count('L') and lst.count('U')==lst.count('D'):
            return True
        return False
        