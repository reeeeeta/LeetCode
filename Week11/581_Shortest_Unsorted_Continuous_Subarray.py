class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_val = float('-inf')
        min_val = float('inf')
        left = -1
        right = -1
        n = len(nums)

        for i in range(n):
            if nums[i] < max_val:
                right = i
            else:
                max_val = nums[i]

            j = n - 1 - i
            if nums[j] > min_val:
                left = j
            else:
                min_val = nums[j]

        return 0 if left == -1 else (right - left + 1)
