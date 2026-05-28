class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9+7
        n = len(s)

        # first -> dp[i-2]，second -> dp[i-1]
        first = 1

        # 計算第一個字元的初始狀態 (dp[1])
        if s[0] == '*':
            second = 9
        elif s[0] == '0':
            second = 0
        else:
            second = 1
        
        for i in range(1, n):
            current = 0
            curr_char = s[i]
            prev_char = s[i-1]

            # 單字元解碼情況：配合 second (dp[i-1])
            if curr_char == '*':
                current += 9 * second
            elif curr_char != '0':
                 current += 1 * second
            
            # 雙字元解碼情況：配合 first (dp[i-2])
            if prev_char == '*' and curr_char == '*':
                current += 15 * first # 11-19, 21-26
            elif prev_char == '*':
                if '0' <= curr_char <= '6':
                    current += 2 * first
                else:
                    current += 1 * first
            elif curr_char == '*':
                if prev_char == '1':
                    current += 9 * first
                elif prev_char == '2':
                    current += 6 * first
            else:
                if 10 <= int(prev_char + curr_char) <= 26:
                    current += 1 * first
            
            current %= MOD
            first = second
            second = current
        return second
