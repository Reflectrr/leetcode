class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            temp = ""
            char = res[0]
            count = 0
            for index in range(len(res)):
                if res[index] == char:
                    count += 1
                else:
                    temp += str(count) + char
                    char = res[index]
                    count = 1
            if count != 0:
                temp += str(count) + char
            res = temp
        return res
