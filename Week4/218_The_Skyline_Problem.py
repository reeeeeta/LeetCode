class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        keypoints = []
        for start, end, h in buildings:
            keypoints.append((start, -h, end)) # 先比高度才比右邊界
            keypoints.append((end, 0, 0))
        
        keypoints.sort()
        ans = [(0, 0)]
        heap = [(0,float('inf'))] # 紀錄目前所有還在範圍內的建築(高度, 右邊界)

        for x, h, end in keypoints:
            # 移除掃描完的建築
            while x >= heap[0][1]: # 右邊界
                heappop(heap)
            # 加入新的建築
            if h < 0:
                heappush(heap,(h, end))

            current_max_h = -heap[0][0]
            if ans[-1][1] != current_max_h: # 最後紀錄的高度不是當前高度->發生轉折
                ans.append((x,current_max_h))

        return ans[1:]
