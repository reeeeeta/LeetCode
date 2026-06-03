class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n-1): # 達到最後一格就不用檢查了
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest # 更新下一跳的邊界
                if current_end >= n-1:
                    break

        return jumps
