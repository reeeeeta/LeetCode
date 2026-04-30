class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key= lambda x:x[1])
        max_heap = []
        total_time = 0
        
        for duration, lastDay in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)

            if total_time > lastDay:
                total_time += heapq.heappop(max_heap) # 彈出的是負值

        return len(max_heap)
