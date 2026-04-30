class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1 and maxDoubles > 0:
            if target & 1: # 奇數
                moves += 2 # 1 步減法 + 1 步除法
            else:
                moves += 1
            target //= 2
            maxDoubles -= 1
        return moves + (target - 1)
