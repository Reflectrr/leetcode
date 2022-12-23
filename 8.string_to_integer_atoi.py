class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_VAL, MIN_VAL = 2**31-1, -(2**31)
        res, index = 0, 0
        stripped = s.strip()
        if len(stripped) == 0:
            return 0
        firstChar = stripped[0]
        sign = -1 if firstChar == "-" else 1
        if firstChar == "-" or firstChar == "+":
            index = 1
        while index < len(stripped) and stripped[index].isdigit():
            nextDigit = int(stripped[index])
            if res > MAX_VAL // 10 or (res == MAX_VAL // 10 and nextDigit > 7):
                return MAX_VAL if sign == 1 else MIN_VAL
            res = res * 10 + int(stripped[index])
            index += 1
        return res * sign
