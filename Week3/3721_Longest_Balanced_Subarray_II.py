class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        
        class Node:
            __slots__ = ("l","r","mn","mx","lazy")
            def __init__(self):
                self.l = self.r = 0
                self.mn = self.mx = 0
                self.lazy = 0
        
        tr = [Node() for _ in range((n + 1) * 4)]

        def build(u: int, l: int, r: int):
            tr[u].l, tr[u].r = l, r
            tr[u].mn = tr[u].mx = tr[u].lazy = 0
            if l == r:
                return
            mid = (l + r) >> 1 # //2 找父節點
            build(u << 1, l, mid) # * 2 找左兒子
            build(u << 1 | 1, mid + 1, r) # * 2 + 1 找右兒子

        def apply(u: int, v: int):
            tr[u].mn += v
            tr[u].mx += v
            tr[u].lazy += v

        # 由父節點往子節點
        def pushdown(u: int):
            if tr[u].lazy != 0:
                apply(u << 1, tr[u].lazy) # 傳給左兒子
                apply(u << 1 | 1, tr[u].lazy) # 傳給右兒子
                tr[u].lazy = 0

        # 由子節點往父節點
        def pushup(u: int):
            tr[u].mn = min(tr[u << 1].mn, tr[u << 1 | 1].mn)
            tr[u].mx = max(tr[u << 1].mx, tr[u << 1 | 1].mx)

        def modify(u: int, l: int, r: int, v: int):
            if tr[u].l >= l and tr[u].r <= r: # 區域完全吻合
                apply(u, v)
                return

            pushdown(u)
            mid = (tr[u].l + tr[u].r) >> 1
            if l <= mid:
                modify(u << 1, l, r, v) # 範圍和左兒子重疊，遞迴進去改左邊
            if r > mid:
                modify(u << 1 | 1, l, r, v) # 範圍和右兒子重疊，遞迴進去改右邊
            pushup(u)

        def query(u: int, target: int) -> int:
            if tr[u].l == tr[u].r:
                return tr[u].l
            pushdown(u)
            if tr[u << 1].mn <= target <= tr[u << 1].mx: # target落在左半邊區域範圍
                return query(u << 1, target) # 優先往左邊找
            return query(u << 1 | 1, target)

        build(1, 0, n)

        last = {}
        now = ans = 0

        for i, x in enumerate(nums, start=1):
            det = 1 if (x & 1) else -1
            if x in last:
                modify(1, last[x], n, -det) # 把舊位置之後的所有分數扣掉
                now -= det
            last[x] = i # 更新字典
            modify(1, i, n, det) 
            now += det
            pos = query(1, now)
            ans = max(ans, i - pos)

        return ans
