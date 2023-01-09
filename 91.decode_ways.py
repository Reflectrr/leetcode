class Solution:
    def numDecodings(self, s: str) -> int:
        resMap = {}

        def helper(index) -> int:
            res = 0
            if index in resMap:
                return resMap[index]
            elif index == len(s):
                return 1
            elif s[index] == "0":
                return 0
            elif len(s) - index == 1:
                res = 1
            elif len(s) - index >= 2:
                num = int(s[index : index + 2])
                if num == 10 or num == 20:
                    res = helper(index + 2)
                elif (num >= 11 and num <= 19) or (num >= 21 and num <= 26):
                    res = helper(index + 1) + helper(index + 2)
                else:
                    res = helper(index + 1)
            resMap[index] = res
            return res

        return helper(0)
