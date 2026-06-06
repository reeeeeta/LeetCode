class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie
        states = rounds + 1

        pigs = 0
        while (states ** pigs) < buckets:
            pigs += 1

        return pigs
