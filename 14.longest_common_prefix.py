class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for index in range(len(strs[0])):
            for s in strs:
                if len(s) == index or s[index] != strs[0][index]:
                    return res
            res += strs[0][index]
        return res
