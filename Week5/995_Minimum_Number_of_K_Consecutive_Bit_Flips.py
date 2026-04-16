class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        is_flipped = [0] * n
        cur_window_flips = 0
        ans = 0

        for i in range(n):
            if i >= k:
                cur_window_flips -= is_flipped[i-k]

            # num[i]=0，翻偶數次 or num[i]=1，翻奇數次 -> 翻轉
            if (nums[i] + cur_window_flips) % 2 == 0:
                if i + k > n:
                    return -1

                ans += 1
                cur_window_flips += 1
                is_flipped[i] = 1 # 標記為翻轉的起點

        return ans

