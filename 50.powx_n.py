class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res, curr = 1, x
        nAbs = abs(n)
        while nAbs:
            lsb = nAbs & 1
            if lsb:
                res *= curr
            curr *= curr
            nAbs >>= 1
        return res if n > 0 else 1/res

