class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(max_sum: int) -> bool:
            subarray_count = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > max_sum:
                    subarray_count += 1
                    curr_sum = num
            return subarray_count <= k

        # 對答案的範圍進行二分搜尋
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high)//2
            if canSplit(mid):
                high = mid
            else:
                low = mid + 1
        
        return low

