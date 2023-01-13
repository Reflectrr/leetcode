class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        partition = []

        def backtrack(currIndex):
            if currIndex == len(s):
                res.append(partition.copy())
            for index in range(currIndex+1, len(s)+1):
                if self.isPalindrom(s[currIndex:index]):
                    partition.append(s[currIndex:index])
                    backtrack(index)
                    partition.pop()
        backtrack(0)
        return res

    def isPalindrom(self, string):
        left, right = 0, len(string)-1
        while right > left:
            if string[left]!= string[right]:
                return False
            left += 1
            right -= 1
        return True

