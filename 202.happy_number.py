class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            newNum = 0
            while n:
                newNum += (n % 10) ** 2
                n = n // 10
            n = newNum
        return True
