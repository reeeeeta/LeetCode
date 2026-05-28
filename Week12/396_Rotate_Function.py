class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        array_sum = sum(nums)

        curr_f = 0
        for i in range(n):
            curr_f += i * nums[i]
        
        max_f = curr_f
        for j in range(1, n):
            curr_f = curr_f + array_sum - n * nums[n-j]
            if curr_f > max_f:
                max_f = curr_f 
        
        return max_f
