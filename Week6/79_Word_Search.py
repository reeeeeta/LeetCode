class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (r<0 or r>=rows or c<0 or c>=cols or board[r][c] != word[idx]):
                return False

            # 暫時置換，避免重複使用
            temp = board[r][c]
            board[r][c] = '#' 

            found = (dfs(r+1, c, idx+1) or
                    dfs(r-1, c, idx+1) or
                    dfs(r, c+1, idx+1) or
                    dfs(r, c-1, idx+1))
            
            board[r][c] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0): # dfs 回傳True，則不用繼續找了
                    return True
        
        return False
