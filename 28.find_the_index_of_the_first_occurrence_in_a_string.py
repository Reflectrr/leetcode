class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # O(n*m)
        # n: len(haystack)
        # m: len(needle)
        if needle == '':
            return 0
        # search every substring of length equal to needle
        for index in range(len(haystack)-len(needle)+1):
            if haystack[index:index+len(needle)] == needle:
                return index
        return -1

