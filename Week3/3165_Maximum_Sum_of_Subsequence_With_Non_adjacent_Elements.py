class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:

        def max(a: int, b: int) -> int:
            return a if a > b else b

        class Node:
            __slots__ = "l", "r", "s00", "s01", "s10", "s11" # 0:不選 1:可選
            def __init__(self, l: int, r: int):
                self.l, self.r = l, r
                # 初始化為 0，因為負數對子序列和沒有貢獻（不選即可）
                self.s00 = self.s01 = self.s10 = self.s11 = 0

        class SegmentTree:
            def __init__(self, n: int, nums: list[int]):
                self.tr = [None] * (n << 2) # n * 4
                self.build(1, 1, n, nums)

            def build(self, u: int, l: int, r: int, nums: list[int]):
                self.tr[u] = Node(l, r)
                if l == r:
                    # 只有一個元素
                    # 左右同一點，只能選該點，所以是s11
                    self.tr[u].s11 = max(0, nums[l-1]) # 若小於0就不選，至少會是0
                    return
                mid = (l + r) >> 1
                self.build(u << 1, l, mid, nums)
                self.build(u << 1 | 1, mid + 1, r, nums)
                self.pushup(u)

            def pushup(self, u: int): #左右子樹合併
                L, R = self.tr[u << 1], self.tr[u << 1 | 1]
                # 合併四種邊界狀態，L 的右端和 R 的左端不能同時被選中
                self.tr[u].s00 = max(L.s00 + R.s10, L.s01 + R.s00)
                self.tr[u].s01 = max(L.s00 + R.s11, L.s01 + R.s01)
                self.tr[u].s10 = max(L.s10 + R.s10, L.s11 + R.s00)
                self.tr[u].s11 = max(L.s10 + R.s11, L.s11 + R.s01)

            def update(self, u: int, idx: int, val: int):
                if self.tr[u].l == self.tr[u].r:
                    self.tr[u].s11 = max(0, val) # 把舊的值丟掉，換成新的值
                    return
                mid = (self.tr[u].l + self.tr[u].r) >> 1
                if idx <= mid: self.update(u << 1, idx, val)
                else: self.update(u << 1 | 1, idx, val)
                self.pushup(u)

        n = len(nums)
        st = SegmentTree(n, nums)
        total_ans = 0
        MOD = 10**9 + 7
        
        for idx, val in queries:
            st.update(1, idx + 1, val) # 線段樹通常從 1 開始編號
            # 根節點的 s11 代表整個區間 [1, n] 且端點選取不限的最大值
            total_ans = (total_ans + st.tr[1].s11) % MOD
            
        return total_ans
