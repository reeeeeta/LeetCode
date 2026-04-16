class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue = deque() # 存儲 (yi - xi, xi)
        max_val = float('-inf')

        for x, y in points:
            # 剔除過期點
            while queue and x - queue[0][1] > k:
                queue.popleft()

            # 計算yi - xi + yj + xj
            if queue:
                max_val = max(max_val, queue[0][0] + x + y)

            current_diff = y - x
            while queue and current_diff >= queue[-1][0]:
                queue.pop()

            queue.append((current_diff, x))

        return max_val
        
