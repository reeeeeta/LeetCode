class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # Pruning 1: 字母頻率檢查 
        if len(word) > rows * cols:
            return False
        
        board_counts = Counter(char for row in board for char in row) # ex:{'A': 2, 'B': 1}
        word_counts = Counter(word)
        
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False  # 棋盤字母不夠用，直接剪掉整個搜尋可能
        
        # Pruning 2: 起始方向優化 
        # 比較開頭和結尾字母在棋盤的數量，從較少的那一端開始找
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]

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
