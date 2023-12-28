class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [(gas[i] - cost[i]) for i in range(len(gas))]
        total = 0
        start = 0
        min = 0
        
        if sum(diff) < 0:
            return -1
        else:
            for i in range(len(diff)):
                total += diff[i]
                if total < min:
                    start = i + 1
                    min = total
        return start
                    