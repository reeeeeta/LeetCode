class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(list(set(arr2))) # set()：去除重複數字
        dp = {-1: 0} # {當前位置的結尾數字: 達到此狀態的最少操作次數}

        for x in arr1:
            next_dp = {}
            for prev_val, ops in dp.items():
                # 不換 x
                if x > prev_val:
                    if x not in next_dp or ops < next_dp[x]:
                        next_dp[x] = ops
                # 從 arr2 換 x
                idx = bisect.bisect_right(arr2, prev_val)
                if idx < len(arr2):
                    replace_val = arr2[idx]
                    if replace_val not in next_dp or ops + 1 < next_dp[replace_val]:
                        next_dp[replace_val] = ops + 1
                
            if not next_dp:
                return -1
            dp = next_dp

        return min(dp.values())
