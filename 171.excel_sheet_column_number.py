class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for char in columnTitle:
            res *= 26
            res += ord(char) - ord("A") + 1
        return res
