class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse = True)
        min_heap = []
        total_speed = 0
        max_performance = 0

        for eff, spd in engineers:
            heapq.heappush(min_heap, spd)
            total_speed += spd

            if len(min_heap) > k: # 目前團隊人數超過k，則踢掉速度最慢的人
                total_speed -= heapq.heappop(min_heap)

            max_performance = max(max_performance, total_speed * eff)

        return max_performance % (10**9 + 7)
