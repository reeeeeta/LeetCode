class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        copy = sorted(nums)
        mid = copy[n // 2]

        def A(i):
            return (1 + 2*i) % (n | 1)

        i, j, k = 0, 0, n-1

        while j <= k:
            if nums[A(j)] > mid:
                nums[A(i)], nums[A(j)] = nums[A(j)], nums[A(i)]
                i += 1
                j += 1
            elif nums[A(j)] < mid:
                nums[A(j)], nums[A(k)] = nums[A(k)], nums[A(j)]
                k -= 1
            else:
                j += 1

