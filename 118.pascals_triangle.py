class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        for level in range(1,numRows+1):
            curr = []
            for index in range(level):
                prevLevel = res[-1] if res else []
                if index == 0 or index == level-1:
                    curr.append(1)
                else:
                    curr.append(prevLevel[index-1]+prevLevel[index])
            res.append(curr)
        return res


