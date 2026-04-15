class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]

        num_left = self.beautifulArray((n+1)//2)
        num_right = self.beautifulArray(n//2)

        res = []

        # 奇數放左，偶數放右
        for i in num_left:
            res.append(2 * i - 1)
        for i in num_right:
            res.append(2 * i)
            
        return res
