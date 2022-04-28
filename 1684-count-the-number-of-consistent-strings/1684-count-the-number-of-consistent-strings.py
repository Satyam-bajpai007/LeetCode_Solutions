class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt=0
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    cnt+=1
                    break
        return len(words)-cnt
                    