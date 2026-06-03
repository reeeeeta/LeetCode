class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                # 最後一步放了 num，前面的數字總和 = i - num
                # 前面要湊出 i - num，那它的組合數就是 dp[i - num]
                if i >= num:
                    dp[i] += dp[i - num]
                else:
                    # 因 nums 排序過，後面更大的數字一定也放不進去，直接結束
                    break
        return dp[target]
