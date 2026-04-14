class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False

        # 設定起點(右上角)
        row = 0
        col = n-1

        while row < m and col >= 0 :
            current = matrix[row][col]
            if target == current:
                return True
            elif target < current:
                col -= 1
            else:
                row += 1

        return False
