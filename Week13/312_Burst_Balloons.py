class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)
        dp = [[0] * n for _ in range(n) ]

        for length in range(2,n): # 區間長度 = right - left = 2 - 0 = 2
            for left in range(0, n - length):
                right = left + length

                for i in range(left + 1, right):
                    coins = arr[left] * arr[i] * arr[right]
                    total = dp[left][i] + dp[i][right] + coins

                    if total > dp[left][right]:
                        dp[left][right] = total

        return dp[0][n-1]
