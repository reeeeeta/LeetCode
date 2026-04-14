class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s: return ""
        res = []
        count = 0
        i = 0

        for j, char in enumerate(s):
            count += 1 if char == '1' else -1

            if count == 0:
                inner_optimized = self.makeLargestSpecial(s[i+1:j])
                res.append('1' + inner_optimized + '0')

                i = j + 1

        res.sort(reverse=True) # 大的在前
        return "".join(res)
