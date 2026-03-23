class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        sz = 2 ** n
        ans = [[-1] * sz for _ in range(sz)]
        val = 0

        def f(x, y, sz):
            nonlocal val
            if sz == 1:
                ans[x][y] = val
                val += 1
                return

            half = sz // 2
            f(x, y+half, half)
            f(x+half, y+half, half)
            f(x+half, y, half)
            f(x, y, half)

        f(0, 0, sz)
        return ans
