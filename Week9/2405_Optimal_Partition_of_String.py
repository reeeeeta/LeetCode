class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        seen = set()

        for char in s:
            if char in seen:
                res += 1
                seen = {char}
            else:
                seen.add(char)
        
        return res
