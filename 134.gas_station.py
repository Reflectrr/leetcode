class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        curr = 0
        start = 0

        for index in range(len(gas)):
            curr += gas[index] - cost[index]
            if curr < 0:
                start = index + 1
                curr = 0
        return start 
