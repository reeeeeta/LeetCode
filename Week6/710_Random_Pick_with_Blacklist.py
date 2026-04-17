class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.w = n - len(blacklist)
        self.mapping = {}

        black_set = set(blacklist)
        last = n - 1

        for b in blacklist:
            if b < self.w:
                while last in black_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        idx = random.randint(0, self.w-1)
        return self.mapping.get(idx, idx)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
