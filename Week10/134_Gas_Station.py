class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0 # gas - cost
        curr_tank = 0
        start_station = 0
        
        for i in range(len(gas)):  
            net_gas = gas[i] - cost[i]
            total_tank += net_gas
            curr_tank += net_gas
            if curr_tank < 0:
                start_station = i + 1
                curr_tank = 0

        return start_station if total_tank >= 0 else -1
