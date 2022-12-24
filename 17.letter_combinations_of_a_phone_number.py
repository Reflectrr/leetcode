from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        temp = [""]
        res = []
        for digit in digits:
            res = []
            newChars = digitToChar[digit]
            for prevStr in temp:
                for char in newChars:
                    res.append(prevStr + char)
            temp = res.copy()
        return res
