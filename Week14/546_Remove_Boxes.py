class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(i, j, k):
            if i > j:
                return 0
            
            while i + 1 <= j and boxes[i] == boxes[i+1]:
                i += 1
                k += 1

            res = (k + 1) * (k + 1) + dp(i+1, j, 0) # 直接消掉

            for m in range(i+1, j+1):
                if boxes[m] == boxes[i]:
                    curr = dp(i+1, m-1, 0) + dp(m, j, k+1)
                    res = max(res, curr)
        
            return res
        return dp(0, len(boxes)-1, 0)
            
