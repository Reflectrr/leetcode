class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(string, openParen, closeParen):
            if openParen == closeParen and openParen == n:
                res.append(string)
            if openParen < n:
                generate(string + "(", openParen + 1, closeParen)
            if closeParen < openParen:
                generate(string + ")", openParen, closeParen + 1)
            return

        generate("", 0, 0)
        return res
